# https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-services-resource-providers
# 위 사이트에서 Azure Resource Providers 정보를 크롤링하여 노션에 저장하는 스크립트

import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from notion_client import Client
from openai import OpenAI

# .env 로드
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

notion = Client(auth=NOTION_TOKEN)
ai_client = OpenAI(api_key=OPENAI_KEY)

def get_llm_summary(full_name, category):
    """LLM에게는 정확한 분석을 위해 전체 이름을 전달합니다."""
    try:
        response = ai_client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "You are an Azure expert. Summarize the role of the given Resource Provider in one concise sentence. Answer in Korean."},
                {"role": "user", "content": f"Category: {category}\nFull Service Name: {full_name}"}
            ]
        )
        return response.choices[0].message.content
    except Exception:
        return ""

def save_to_notion(display_name, description, category):
    """노션에는 'Microsoft.'이 제거된 이름을 저장합니다."""
    try:
        notion.pages.create(
            parent={"database_id": DATABASE_ID},
            properties={
                "이름": {"title": [{"text": {"content": display_name}}]},
                "설명": {"rich_text": [{"text": {"content": description}}]},
                "카테고리": {"select": {"name": category}}
            }
        )
        print(f"   ✅ 저장 완료: {display_name}")
    except Exception as e:
        print(f"   ❌ 저장 실패: {e}")

def run_sync():
    url = "https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-services-resource-providers"
    print(f"🔎 Connecting to: {url}")
    
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    content_area = soup.find('main')
    if not content_area:
        print("❌ 본문을 찾을 수 없습니다.")
        return

    elements = content_area.find_all(['h2', 'table'])
    current_category = "General"

    for element in elements:
        if element.name == 'h2':
            raw_title = element.get_text(strip=True)
            current_category = raw_title.split(' resource providers')[0].split(' resource provider')[0].strip()
            print(f"\n📂 Category: {current_category}")
            
        elif element.name == 'table':
            rows = element.find_all('tr')[1:]
            for row in rows:
                cols = row.find_all('td')
                if not cols: continue
                
                # 원본 이름 (예: Microsoft.Compute)
                full_name = cols[0].get_text(strip=True)
                
                # 저장용 이름 (Microsoft. 제거)
                display_name = full_name.replace("Microsoft.", "")
                
                print(f"   > Processing: {display_name}...", end="\r")
                
                summary = get_llm_summary(full_name, current_category)
                save_to_notion(display_name, summary, current_category)

if __name__ == "__main__":
    run_sync()