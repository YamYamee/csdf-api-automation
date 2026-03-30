import os
from github import Github
from notion_client import Client
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 환경 변수 설정
g = Github(os.getenv("GITHUB_TOKEN"))
notion = Client(auth=os.getenv("NOTION_TOKEN"))
ai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
DATABASE_ID = os.getenv("NOTION_DATABASE_ID_2")

repo = g.get_repo("boto/botocore")

def get_aws_info_from_ai(service_slug):
    """서비스 ID(예: ec2)를 주면 전체 이름, 요약, 카테고리를 반환합니다."""
    try:
        prompt = f"""
        AWS Service ID: {service_slug}
        
        이 서비스에 대해 다음 형식을 지켜서 한국어로 답해줘.
        1. Full Name: (서비스의 공식 전체 명칭)
        2. Category: (Compute, Storage, Database, ML, Security 등 대표 카테고리 하나)
        3. Summary: (서비스의 역할을 설명하는 간결한 한 문장)
        """
        
        response = ai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AWS expert who categorizes and summarizes services accurately."},
                {"role": "user", "content": prompt}
            ]
        )
        # 결과 파싱 (간단하게 줄 단위로 분리)
        lines = response.choices[0].message.content.strip().split('\n')
        info = {}
        for line in lines:
            if "Full Name:" in line: info['full_name'] = line.split("Full Name:")[1].strip()
            if "Category:" in line: info['category'] = line.split("Category:")[1].strip()
            if "Summary:" in line: info['summary'] = line.split("Summary:")[1].strip()
        return info
    except:
        return {"full_name": service_slug, "category": "General", "summary": "정보를 가져오지 못했습니다."}

def save_to_notion(display_name, description, category):
    try:
        notion.pages.create(
            parent={"database_id": DATABASE_ID},
            properties={
                "이름": {"title": [{"text": {"content": display_name}}]},
                "설명": {"rich_text": [{"text": {"content": description}}]},
                "카테고리": {"select": {"name": category}}
            }
        )
        print(f" ✅ 저장 완료: {display_name} [{category}]")
    except Exception as e:
        print(f" ❌ 저장 실패: {display_name} | {e}")

def run_sync():
    data_path = "botocore/data"
    print("🔎 AWS 서비스 폴더 탐색 시작...")
    
    try:
        # botocore/data의 하위 폴더 리스트만 가져옴
        contents = repo.get_contents(data_path)
        
        for content in contents:
            if content.type == "dir":
                service_slug = content.name  # 예: ec2, s3, lambda
                
                print(f" > 분석 중: {service_slug}...", end="\r")
                
                # AI에게 서비스 정보를 한꺼번에 물어봄
                info = get_aws_info_from_ai(service_slug)
                
                # 노션 저장 (카테고리 포함)
                save_to_notion(info['full_name'], info['summary'], info['category'])

        print("\n✨ AWS 서비스 목록화 작업이 모두 끝났습니다!")

    except Exception as e:
        print(f"❌ 에러 발생: {e}")

if __name__ == "__main__":
    run_sync()