import json
import csv
import pandas as pd
from pathlib import Path
from tqdm import tqdm
import sys

# --- 설정 ---
# Botocore 저장소 내의 'data' 폴더 경로를 지정하세요.
BASE_DIR = Path("C:/aws/data")
DATA_DIR = Path("C:/Users/cartc/Documents/GitHub/csdf-azure-api-automation/data")
OUTPUT_CSV = DATA_DIR / "aws_api_specs_complete.csv"

def set_safe_limit():
    max_int = sys.maxsize
    while True:
        try:
            csv.field_size_limit(max_int)
            return
        except OverflowError:
            max_int = int(max_int / 10)

set_safe_limit()

def resolve_shapes(shape_name, shapes_dict, depth=0):
    """AWS의 Shape 참조 구조를 재귀적으로 해석"""
    if depth > 10 or not shape_name or shape_name not in shapes_dict:
        return {"type": "referenced", "name": shape_name}

    shape_info = shapes_dict[shape_name].copy()
    
    if shape_info.get("type") == "structure":
        members = shape_info.get("members", {})
        resolved_members = {}
        for m_name, m_info in members.items():
            target_shape = m_info.get("shape")
            resolved_members[m_name] = resolve_shapes(target_shape, shapes_dict, depth + 1)
        shape_info["resolved_members"] = resolved_members
    
    elif shape_info.get("type") == "list":
        member_shape = shape_info.get("member", {}).get("shape")
        if member_shape:
            shape_info["resolved_item"] = resolve_shapes(member_shape, shapes_dict, depth + 1)

    return shape_info

def main():
    if not DATA_DIR.exists(): DATA_DIR.mkdir(parents=True)
    all_api_data = []
    
    print(f"🚀 AWS API 스펙 수집 시작 (Azure 필드명 매핑)...")

    if not BASE_DIR.exists():
        print(f"❌ 경로를 찾을 수 없습니다: {BASE_DIR}")
        return

    service_dirs = [d for d in BASE_DIR.iterdir() if d.is_dir()]

    for s_dir in tqdm(service_dirs, desc="Parsing Services"):
        # 최신 버전 폴더 선택
        version_dirs = sorted([v for v in s_dir.iterdir() if v.is_dir()], key=lambda x: x.name)
        if not version_dirs: continue
        
        latest_version_dir = version_dirs[-1]
        service_2_file = latest_version_dir / "service-2.json"
        
        if not service_2_file.exists(): continue

        try:
            with open(service_2_file, 'r', encoding='utf-8') as f:
                service_def = json.load(f)
            
            metadata = service_def.get('metadata', {})
            operations = service_def.get('operations', {})
            shapes = service_def.get('shapes', {})
            
            service_id = metadata.get('serviceId', s_dir.name).replace(" ", "_").lower()

            for op_name, op_info in operations.items():
                input_shape = op_info.get('input', {}).get('shape')
                output_shape = op_info.get('output', {}).get('shape')
                
                resolved_input = resolve_shapes(input_shape, shapes) if input_shape else {}
                resolved_output = resolve_shapes(output_shape, shapes) if output_shape else {}

                # --- Azure 필드명과 통일 ---
                all_api_data.append({
                    "Service_Path": service_id,
                    "Version": latest_version_dir.name,
                    "Endpoint": op_info.get('http', {}).get('requestUri', '/'),
                    "Method": op_info.get('http', {}).get('method', 'POST'),
                    "Parameters": json.dumps(resolved_input, ensure_ascii=False),
                    "Response": json.dumps(resolved_output, ensure_ascii=False),
                    "Source_File": str(service_2_file.relative_to(BASE_DIR))
                })
        except: continue

    if all_api_data:
        df = pd.DataFrame(all_api_data)
        df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
        print(f"\n✅ 저장 완료! {len(df)}개 API -> {OUTPUT_CSV}")

if __name__ == "__main__":
    main()