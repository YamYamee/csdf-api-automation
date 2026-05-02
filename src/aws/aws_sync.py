import json
import pandas as pd
import datetime
import sys
from pathlib import Path

# 프로젝트 루트를 path에 추가
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.utils.sync_utils import set_safe_limit, get_changed_files, get_raw_content

REPO = "boto/botocore"
BASE_BRANCH = "develop" # AWS는 develop 사용
DATA_DIR = Path(__file__).parent.parent.parent / "data"
CHECKPOINT = DATA_DIR / "aws_last_sha.txt"
MASTER_CSV = DATA_DIR / "aws_api_specs_complete.csv"

def resolve_shapes(shape_name, shapes_dict, depth=0):
    if depth > 10 or not shape_name or shape_name not in shapes_dict:
        return {"type": "referenced", "name": shape_name}
    shape_info = shapes_dict[shape_name].copy()
    if shape_info.get("type") == "structure":
        shape_info["resolved_members"] = {
            m: resolve_shapes(i.get("shape"), shapes_dict, depth+1) 
            for m, i in shape_info.get("members", {}).items()
        }
    return shape_info

def run_sync():
    set_safe_limit()
    if not CHECKPOINT.exists(): return print("❌ 체크포인트 파일 없음")
    
    last_sha = CHECKPOINT.read_text().strip()
    print(f"🚀 AWS Sync 시작: {last_sha} -> {BASE_BRANCH}")

    changed_files = get_changed_files(REPO, last_sha, base_branch=BASE_BRANCH)
    targets = [f for f in changed_files if "service-2.json" in f]
    
    if not targets: return print("ℹ️ AWS: 변경사항 없음")

    new_data = []
    for file_path in targets:
        spec = get_raw_content(REPO, file_path, base_branch=BASE_BRANCH)
        if not spec: continue
        
        metadata = spec.get('metadata', {})
        operations = spec.get('operations', {})
        shapes = spec.get('shapes', {})
        service_id = metadata.get('serviceId', file_path.split('/')[2]).replace(" ", "_").lower()

        for op_name, op_info in operations.items():
            new_data.append({
                "Service_Path": service_id,
                "Version": file_path.split('/')[-2],
                "Endpoint": op_info.get('http', {}).get('requestUri', '/'),
                "Method": op_info.get('http', {}).get('method', 'POST'),
                "Parameters": json.dumps(resolve_shapes(op_info.get('input', {}).get('shape'), shapes), ensure_ascii=False),
                "Response": json.dumps(resolve_shapes(op_info.get('output', {}).get('shape'), shapes), ensure_ascii=False),
                "Source_File": file_path,
                "Snapshot_Date": datetime.date.today().isoformat()
            })

    if new_data:
        df_new = pd.DataFrame(new_data)
        (DATA_DIR / "snapshots").mkdir(parents=True, exist_ok=True)
        df_new.to_csv(DATA_DIR / f"snapshots/aws_diff_{datetime.date.today()}.csv", index=False)
        
        if MASTER_CSV.exists():
            df_master = pd.read_csv(MASTER_CSV)
            df_master = pd.concat([df_new, df_master]).drop_duplicates(subset=['Service_Path', 'Endpoint', 'Method'], keep='first')
            df_master.to_csv(MASTER_CSV, index=False, encoding='utf-8-sig')
        else:
            df_new.to_csv(MASTER_CSV, index=False, encoding='utf-8-sig')
        print(f"✅ AWS 업데이트 완료 ({len(new_data)}건)")

if __name__ == "__main__":
    run_sync()