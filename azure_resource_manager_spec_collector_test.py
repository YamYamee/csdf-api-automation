import os
import json
from dotenv import load_dotenv
from github import Github
from notion_client import Client

# 환경 변수 로드
load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo("Azure/azure-rest-api-specs")

# 설정 데이터
CATEGORY = "compute"
SERVICE_NAME = "Compute"
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def create_table_row(cells):
    """노션 테이블 행 생성"""
    return {
        "type": "table_row",
        "table_row": {
            "cells": [[{"type": "text", "text": {"content": str(cell)}}] for cell in cells]
        }
    }

def create_notion_table(header, rows):
    """노션 테이블 블록 생성"""
    table_rows = [create_table_row(header)]
    for row in rows:
        table_rows.append(create_table_row(row))
    
    return {
        "object": "block",
        "type": "table",
        "table": {
            "table_width": len(header),
            "has_column_header": True,
            "children": table_rows
        }
    }

def find_compute_page_id():
    """라이브러리 search 메서드로 Compute 페이지 ID 찾기"""
    print("Searching for 'Compute' page in Notion...")
    response = notion.search(query="Compute")
    results = response.get("results", [])
    
    for page in results:
        props = page.get("properties", {})
        title_list = props.get("이름", {}).get("title", []) or \
                     props.get("Name", {}).get("title", []) or \
                     props.get("title", {}).get("title", [])
        
        if title_list and title_list[0].get("plain_text") == "Compute":
            return page["id"]
    return None

def generate_notion_blocks(spec):
    """Swagger JSON을 노션 블록으로 변환 (번호 매기기 추가)"""
    all_blocks = []
    paths = spec.get("paths", {})
    
    version = spec.get('info', {}).get('version', 'N/A')
    all_blocks.append({
        "object": "block",
        "type": "heading_1",
        "heading_1": {"rich_text": [{"text": {"content": f"{SERVICE_NAME} API Full Documentation"}}]}
    })
    all_blocks.append({
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": [{"text": {"content": f"API Version: {version}"}}]}
    })
    all_blocks.append({"object": "block", "type": "divider", "divider": {}})

    count = 0
    for path, methods in paths.items():
        if count >= 30: break # 개수를 조금 더 늘려 30개까지 가져오게 설정했습니다.
        for method_type, details in methods.items():
            count += 1 # 번호 카운트 증가
            op_id = details.get("operationId", "N/A")
            summary = details.get("description", details.get("summary", "No description")).split('.')[0].replace('\n', ' ')

            # 🚀 1. API 제목 (번호 포함: 1. Operation, 2. Operation...)
            all_blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {"rich_text": [{"text": {"content": f"{count}. Operation: {op_id}"}}]}
            })
            all_blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": [{"text": {"content": f"Description: {summary}"}}]}
            })

            # 2. 기본 정보 테이블
            all_blocks.append(create_notion_table(
                ["Field", "Details"],
                [["Method", method_type.upper()], ["Endpoint", path]]
            ))

            # 3. 파라미터 테이블
            params = details.get("parameters", [])
            if params:
                p_rows = []
                for p in params[:5]: 
                    name = p.get("name", p.get("$ref", "").split("/")[-1])
                    p_in = p.get("in", "Ref")
                    req = "Yes" if p.get("required") else "No"
                    p_rows.append([name, p_in, req])
                
                all_blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": "Parameters:"}, "annotations": {"bold": True}}]}
                })
                all_blocks.append(create_notion_table(["Name", "In", "Required"], p_rows))

            # 4. 응답 테이블
            responses = details.get("responses", {})
            if responses:
                res_rows = []
                for code, res_info in responses.items():
                    res_desc = res_info.get("description", "No description").replace("\n", " ").strip()
                    res_schema = res_info.get("schema", {}).get("$ref", "N/A").split("/")[-1]
                    res_rows.append([code, res_schema, res_desc])
                
                all_blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": "Responses:"}, "annotations": {"bold": True}}]}
                })
                all_blocks.append(create_notion_table(["Code", "Schema", "Description"], res_rows))

            all_blocks.append({"object": "block", "type": "divider", "divider": {}})

    return all_blocks

def upload_blocks_to_notion(page_id, blocks):
    """청크 업로드"""
    print(f"Uploading {len(blocks)} blocks to Notion...")
    chunk_size = 40 
    for i in range(0, len(blocks), chunk_size):
        chunk = blocks[i:i + chunk_size]
        try:
            notion.blocks.children.append(block_id=page_id, children=chunk)
            print(f" - Progress: {min(i + chunk_size, len(blocks))}/{len(blocks)} blocks uploaded.")
        except Exception as e:
            print(f"❌ Error at index {i}: {e}")

def run_sync():
    page_id = find_compute_page_id()
    if not page_id:
        print("❌ 'Compute' page not found.")
        return
    print(f"✅ Found Compute Page ID: {page_id}")

    try:
        provider_folder = f"Microsoft.{SERVICE_NAME}"
        base_path = f"specification/{CATEGORY.lower()}/resource-manager/{provider_folder}"
        contents = repo.get_contents(base_path)
        
        stable_path = f"{base_path}/stable" if any(c.name == "stable" for c in contents) else f"{base_path}/Compute/stable"
        versions = repo.get_contents(stable_path)
        v_names = sorted([v.name for v in versions if v.type == "dir" and "-" in v.name])
        latest_v = v_names[-1]
        
        files = repo.get_contents(f"{stable_path}/{latest_v}")
        json_file = next(f for f in files if f.name.endswith(".json") and "openapi" not in f.name)
        
        spec = json.loads(json_file.decoded_content.decode('utf-8'))
        print(f"📄 Spec Loaded: {json_file.name}")

        blocks = generate_notion_blocks(spec)
        upload_blocks_to_notion(page_id, blocks)
        
        print("\n✨ All operations completed successfully with numbering!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_sync()