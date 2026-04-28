import os
import json
import csv
import pandas as pd
from pathlib import Path
from tqdm import tqdm
import sys

# --- 설정 ---
BASE_DIR = Path("C:/azure/specification")
DATA_DIR = Path("C:/azure/data")
OUTPUT_CSV = DATA_DIR / "azure_api_specs_complete.csv"

# CSV 필드 크기 제한 해제 (대용량 데이터 보존용)
csv.field_size_limit(sys.maxsize)

def resolve_refs(obj, root_data, base_path, depth=0):
    """$ref 참조를 재귀적으로 해결하여 실제 값으로 치환"""
    if depth > 15: return obj # 무한 루프 방지
    
    if isinstance(obj, dict):
        if '$ref' in obj:
            ref_path = obj['$ref']
            try:
                # 1. 내부 참조 (#/definitions/...)
                if ref_path.startswith('#'):
                    parts = ref_path.strip('#/').split('/')
                    target = root_data
                    for part in parts:
                        target = target.get(part, {})
                    return resolve_refs(target, root_data, base_path, depth + 1)
                
                # 2. 외부 파일 참조 (./common.json#...)
                else:
                    file_part = ref_path.split('#')[0]
                    fragment = ref_path.split('#')[1] if '#' in ref_path else ""
                    target_file = (base_path.parent / file_part).resolve()
                    
                    if target_file.exists():
                        with open(target_file, 'r', encoding='utf-8') as f:
                            ext_data = json.load(f)
                        
                        if fragment:
                            parts = fragment.strip('/').split('/')
                            for part in parts:
                                ext_data = ext_data.get(part, {})
                        return resolve_refs(ext_data, ext_data, target_file, depth + 1)
            except:
                return obj
        return {k: resolve_refs(v, root_data, base_path, depth + 1) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [resolve_refs(item, root_data, base_path, depth + 1) for item in obj]
    return obj

def get_latest_date_dir(stable_dir):
    try:
        sub_dirs = [d for d in stable_dir.iterdir() if d.is_dir()]
        return sorted(sub_dirs, key=lambda x: x.name)[-1] if sub_dirs else None
    except: return None

def main():
    if not DATA_DIR.exists(): DATA_DIR.mkdir(parents=True)
    all_api_data = []
    
    print(f"🚀 스캔 및 $ref 해결 시작 (시간이 다소 소요될 수 있습니다)...")
    stable_paths = list(BASE_DIR.glob("**/stable"))

    for s_path in tqdm(stable_paths, desc="Parsing APIs"):
        latest_dir = get_latest_date_dir(s_path)
        if not latest_dir: continue
            
        service_info = "/".join(latest_dir.relative_to(BASE_DIR).parts[:-2])
        version = latest_dir.name

        for json_file in latest_dir.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    raw_data = json.load(f)
                
                # [핵심] 참조 해결
                full_data = resolve_refs(raw_data, raw_data, json_file)
                
                paths = full_data.get('paths', {})
                for endpoint, methods in paths.items():
                    for method, info in methods.items():
                        all_api_data.append({
                            "Service_Path": service_info,
                            "Version": version,
                            "Endpoint": endpoint,
                            "Method": method.upper(),
                            "Parameters": json.dumps(info.get('parameters', []), ensure_ascii=False),
                            "Response": json.dumps(info.get('responses', {}), ensure_ascii=False),
                            "Source_File": str(json_file.relative_to(BASE_DIR))
                        })
            except: continue

    if all_api_data:
        df = pd.DataFrame(all_api_data)
        df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
        print(f"\n✅ 저장 완료! {len(df)}개 API -> {OUTPUT_CSV}")

if __name__ == "__main__":
    main()