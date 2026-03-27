import os
import json
from dotenv import load_dotenv
from github import Github

# 환경 변수 로드
load_dotenv()
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo("Azure/azure-rest-api-specs")

# 설정 데이터
CATEGORY = "compute"
SERVICE_NAME = "Compute"

def generate_markdown_tables(spec):
    """
    Swagger JSON 전체를 순회하며 상세 마크다운 문서를 생성합니다.
    """
    md_content = f"# 📘 {SERVICE_NAME} API Full Documentation\n"
    md_content += f"> **추출된 API 버전:** {spec.get('info', {}).get('version', 'N/A')}\n\n"
    
    paths = spec.get("paths", {})
    api_count = 0

    for path, methods in paths.items():
        for method_type, details in methods.items():
            api_count += 1
            op_id = details.get("operationId", "N/A")
            summary = details.get("description", details.get("summary", "설명 없음")).split('.')[0].replace('\n', ' ')

            # 1. 제목 및 설명
            md_content += f"## 🚀 {op_id}\n"
            md_content += f"**Description:** {summary}\n\n"

            # 2. 기본 정보 표
            md_content += "#### 📌 Base Information\n"
            md_content += "| Field | Details |\n| :--- | :--- |\n"
            md_content += f"| **Method** | `{method_type.upper()}` |\n"
            md_content += f"| **Endpoint** | `{path}` |\n"
            md_content += f"| **Tags** | {', '.join(details.get('tags', ['N/A']))} |\n\n"

            # 3. URI 파라미터 표
            params = details.get("parameters", [])
            if params:
                md_content += "#### 🛠️ URI Parameters\n"
                md_content += "| Name | In | Required | Type | Description |\n"
                md_content += "| :--- | :---: | :---: | :---: | :--- |\n"
                for p in params:
                    if "$ref" in p:
                        ref_name = p["$ref"].split("/")[-1]
                        md_content += f"| {ref_name} | (Ref) | - | - | 공통 정의 참조 |\n"
                    else:
                        name = p.get("name", "-")
                        p_in = p.get("in", "-")
                        req = "✅" if p.get("required") else "❌"
                        p_type = p.get("type", p.get("schema", {}).get("type", "object"))
                        p_desc = p.get("description", "-").replace("\n", " ").strip()
                        md_content += f"| **{name}** | {p_in} | {req} | `{p_type}` | {p_desc} |\n"
                md_content += "\n"

            # 4. Request Body (POST, PUT, PATCH 등)
            # Swagger 2.0에서는 parameters 안에 'in': 'body'가 있음
            body_param = next((p for p in params if p.get("in") == "body"), None)
            if body_param:
                md_content += "#### 📦 Request Body\n"
                md_content += "| Name | Required | Type/Schema | Description |\n"
                md_content += "| :--- | :---: | :--- | :--- |\n"
                schema = body_param.get("schema", {})
                ref = schema.get("$ref", "CustomObject").split("/")[-1]
                b_desc = body_param.get("description", "상세 스키마 참조").replace("\n", " ")
                md_content += f"| (Body Content) | ✅ | `{ref}` | {b_desc} |\n\n"

            # 5. 응답 표
            responses = details.get("responses", {})
            md_content += "#### ✅ Responses\n"
            md_content += "| Code | Schema | Description |\n"
            md_content += "| :---: | :--- | :--- |\n"
            for code, res in responses.items():
                res_desc = res.get("description", "-").replace("\n", " ").strip()
                res_schema = res.get("schema", {}).get("$ref", "N/A").split("/")[-1]
                md_content += f"| **{code}** | `{res_schema}` | {res_desc} |\n"
            
            md_content += "\n---\n\n"

    return md_content, api_count

def run_sync():
    provider_folder = SERVICE_NAME if SERVICE_NAME.startswith("Microsoft.") else f"Microsoft.{SERVICE_NAME}"
    base_path = f"specification/{CATEGORY.lower()}/resource-manager/{provider_folder}"
    
    print(f"🎯 GitHub 경로 탐색 시작: {base_path}")
    
    try:
        # 1. stable 폴더 찾기
        contents = repo.get_contents(base_path)
        stable_path = None
        if any(c.name == "stable" for c in contents):
            stable_path = f"{base_path}/stable"
        else:
            for c in contents:
                if c.type == "dir" and c.name not in ["examples", "preview"]:
                    sub = repo.get_contents(c.path)
                    if any(sc.name == "stable" for sc in sub):
                        stable_path = f"{c.path}/stable"
                        break
        
        if not stable_path:
            print("❌ stable 폴더를 찾을 수 없습니다.")
            return

        # 2. 최신 버전 JSON 로드
        versions = repo.get_contents(stable_path)
        v_names = sorted([v.name for v in versions if v.type == "dir" and "-" in v.name])
        latest_v = v_names[-1]
        
        target_dir = f"{stable_path}/{latest_v}"
        files = repo.get_contents(target_dir)
        json_file = next(f for f in files if f.name.endswith(".json") and "openapi" not in f.name)
        
        print(f"📄 최신 API 명세 로드: {json_file.name} ({latest_v})")
        content = json_file.decoded_content.decode('utf-8')
        spec = json.loads(content)

        # 3. 전체 데이터 마크다운 변환
        print("⚙️ 모든 API 엔드포인트 분석 및 표 생성 중...")
        md_text, total_apis = generate_markdown_tables(spec)

        # 4. 파일 저장
        output_file = f"azure_api_{SERVICE_NAME.lower()}_docs.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md_text)
            
        print(f"\n✨ 완료!")
        print(f"✅ 총 {total_apis}개의 API 엔드포인트 문서화 성공")
        print(f"📂 저장 위치: {os.path.abspath(output_file)}")

    except Exception as e:
        print(f"❌ 작업 중 에러 발생: {e}")

if __name__ == "__main__":
    run_sync()