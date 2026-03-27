import os
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

# 변수명을 client로 변경하여 패키지명과 구분
client = Client(auth=os.getenv("NOTION_TOKEN"))
db_id = os.getenv("NOTION_DATABASE_ID")

def clean_name_string(raw_name):
    # 'Microsoft.Compute - registered by default' -> 'Compute'
    name = raw_name.split(' -')[0].strip()
    name = name.replace("Microsoft.", "")
    return name

def cleanup_notion_database():
    print("🔄 노션 데이터베이스 이름 정리 시작...")
    
    try:
        has_more = True
        start_cursor = None
        update_count = 0

        while has_more:
            # 1. query 메서드 호출 확인
            response = client.databases.query(
                **{
                    "database_id": db_id,
                    "start_cursor": start_cursor,
                }
            )
            
            for page in response.get("results", []):
                page_id = page["id"]
                props = page["properties"]
                
                # '이름' 속성에서 텍스트 추출 (속성명이 다르면 여기서 에러남)
                title_data = props.get("이름", {}).get("title", [])
                if not title_data:
                    continue
                
                current_name = title_data[0]["plain_text"]
                new_name = clean_name_string(current_name)
                
                if current_name != new_name:
                    client.pages.update(
                        page_id=page_id,
                        properties={
                            "이름": {"title": [{"text": {"content": new_name}}]}
                        }
                    )
                    print(f"   ✨ 변경: {current_name} ➔ {new_name}")
                    update_count += 1
            
            has_more = response.get("has_more", False)
            start_cursor = response.get("next_cursor")

        print(f"\n✨ 완료! 총 {update_count}개 수정됨.")

    except Exception as e:
        print(f"\n❌ 에러 발생: {e}")
        # 어떤 메서드들이 있는지 확인용 (디버깅)
        print("사용 가능한 메서드들:", dir(client.databases))

if __name__ == "__main__":
    cleanup_notion_database()