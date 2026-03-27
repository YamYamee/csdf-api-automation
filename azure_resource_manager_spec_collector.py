# GitHub에서 Azure REST API 스펙을 최신 버전으로 가져와 노션 페이지에 업데이트하는 스크립트

import os
import json
from dotenv import load_dotenv
from github import Github
from notion_client import Client

load_dotenv()

# 클라이언트 초기화
notion = Client(auth=os.getenv("NOTION_TOKEN"))
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo("Azure/azure-rest-api-specs")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def get_latest_api_spec(service_name):
    """GitHub에서 해당 서비스의 최신 stable API 스펙(JSON)을 찾아 내용을 반환"""
    try:
        # 1. specification 폴더에서 서비스 폴더 찾기 (소문자로 매칭)
        # 예: specification/compute
        base_path = f"specification/{service_name.lower()}/resource-manager"
        
        # 2. Microsoft.Service 형식의 하위 폴더 찾기
        contents = repo.get_contents(base_path)
        rp_folder = next((c for c in contents if c.type == "dir" and "Microsoft." in c.name), contents[0])
        
        # 3. stable 버전 폴더로 진입
        stable_path = f"{rp_folder.path}/stable"
        versions = repo.get_contents(stable_path)
        
        # 최신 버전 폴더 선택 (가장 마지막 이름)
        latest_version = sorted([v.name for v in versions if v.type == "dir"])[-1]
        
        # 4. JSON 파일 읽기 (보통 서비스명.json)
        json_files = repo.get_contents(f"{stable_path}/{latest_version}")
        spec_file = next(f for f in json_files if f.name.endswith(".json"))
        
        # 파일 내용 다운로드 및 파싱
        file_content = spec_file.decoded_content.decode('utf-8')
        return json.loads(file_content), latest_version
    except Exception as e:
        print(f"      ⚠️ GitHub 탐색 실패 ({service_name}): {e}")
        return None, None

def update_notion_page_content(page_id, spec_data, version):
    """노션 페이지 본문에 API 정보를 표 형태로 추가"""
    try:
        paths = spec_data.get("paths", {})
        # 주요 API 5개만 추출
        main_apis = list(paths.keys())[:5]
        
        children = [
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": f"📑 최신 API 정보 ({version})" }}]}
            }
        ]
        
        # API 경로들을 불렛 리스트로 추가
        for path in main_apis:
            methods = ", ".join(paths[path].keys()).upper()
            summary = paths[path].get("get", {}).get("summary", "설명 없음")
            children.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": f"{path} [{methods}]\n- {summary}"}}]
                }
            })

        # 노션 페이지 본문(Children) 업데이트
        notion.blocks.children.append(block_id=page_id, children=children)
        return True
    except Exception as e:
        print(f"      ❌ 노션 본문 업데이트 실패: {e}")
        return False

def run_github_sync():
    print("🔍 노션 데이터베이스 읽는 중...")
    # 지난번에 겪은 query 메서드 에러 방지를 위해 request 방식 사용
    response = notion.request(path=f"databases/{DATABASE_ID}/query", method="POST", body={})
    
    for page in response.get("results", []):
        page_id = page["id"]
        # 이름 가져오기 (이미 Microsoft. 가 제거된 상태라면 다시 붙여서 검색해야 할 수도 있음)
        name = page["properties"]["이름"]["title"][0]["plain_text"]
        
        print(f"🚀 {name} 서비스의 API 스펙 분석 시작...")
        
        # GitHub에서 데이터 가져오기
        spec_data, version = get_latest_api_spec(name)
        
        if spec_data:
            if update_notion_page_content(page_id, spec_data, version):
                print(f"   ✅ {name} 업데이트 완료 (버전: {version})")
        else:
            print(f"   ⏩ {name} 스킵 (GitHub 데이터를 찾을 수 없음)")

if __name__ == "__main__":
    run_github_sync()