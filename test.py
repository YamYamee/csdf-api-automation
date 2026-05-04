import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))

# 검색 테스트에서 찾은 Page ID를 사용합니다.
PAGE_ID = "33073fa2-3f8b-81d4-992d-ec01ee8c91a3"

def get_page_description(page_id):
    print(f"페이지 정보 가져오는 중... (ID: {page_id})")
    
    try:
        # 라이브러리의 표준 pages.retrieve 메서드 사용
        # 이 메서드는 페이지의 제목, 설명, 카테고리 등 '속성' 데이터를 반환합니다.
        page_info = notion.pages.retrieve(page_id=page_id)
        
        # 페이지의 모든 속성(Properties) 추출
        properties = page_info.get("properties", {})
        
        # '설명' 속성 확인 (사진에 있던 이름 기준)
        description_prop = properties.get("설명", {})
        
        # '설명'은 rich_text 타입이므로 내부 리스트에서 텍스트를 꺼내옵니다.
        rich_text_list = description_prop.get("rich_text", [])
        
        if rich_text_list:
            # 전체 텍스트 합치기 (여러 줄일 경우 대비)
            full_description = "".join([item.get("plain_text", "") for item in rich_text_list])
            print("성공: 설명을 가져왔습니다.")
            print(f"내용: {full_description}")
            return full_description
        else:
            print("알림: '설명' 필드가 비어있습니다.")
            return ""

    except Exception as e:
        print(f"에러 발생: {e}")
        return None

if __name__ == "__main__":
    description = get_page_description(PAGE_ID)
    if description is not None:
        print("\n설명 데이터 추출 완료. 이 데이터를 기반으로 다음 작업을 수행할 수 있습니다.")