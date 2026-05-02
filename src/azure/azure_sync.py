import json
import pandas as pd
import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.utils.sync_utils import set_safe_limit, get_changed_files, get_raw_content

REPO = "Azure/azure-rest-api-specs"
BASE_BRANCH = "main" # Azure는 main 사용
DATA_DIR = Path(__file__).parent.parent.parent / "data"
CHECKPOINT = DATA_DIR / "azure_last_sha.txt"
MASTER_CSV = DATA_DIR / "azure_api_specs_complete.csv"

def run_sync():
    set_safe_limit()
    if not CHECKPOINT.exists(): return print("❌ 체크포인트 파일 없음")
    
    last_sha = CHECKPOINT.read_text().strip()
    print(f"🚀 Azure Sync 시작: {last_sha} -> {BASE_BRANCH}")

    changed_files = get_changed_files(REPO, last_sha, base_branch=BASE_BRANCH)
    targets = [f for f in changed_files if "resource-manager" in f and "stable" in f and f.endswith('.json')]
    
    if not targets: return print("ℹ️ Azure: 변경사항 없음")

    new_data = []
    for file_path in targets:
        spec = get_raw_content(REPO, file_path, base_branch=BASE_BRANCH)
        if not spec or 'paths' not in spec: continue
        
        service_info = "/".join(file_path.split('/')[:-3])
        version = file_path.split('/')[-2]

        for endpoint, methods in spec['paths'].items():
            for method, info in methods.items():
                if method.lower() in ['get', 'post', 'put', 'delete', 'patch']:
                    new_data.append({
                        "Service_Path": service_info,
                        "Version": version,
                        "Endpoint": endpoint,
                        "Method": method.upper(),
                        "Parameters": json.dumps(info.get('parameters', []), ensure_ascii=False),
                        "Response": json.dumps(info.get('responses', {}), ensure_ascii=False),
                        "Source_File": file_path,
                        "Snapshot_Date": datetime.date.today().isoformat()
                    })

    if new_data:
        df_new = pd.DataFrame(new_data)
        (DATA_DIR / "snapshots").mkdir(parents=True, exist_ok=True)
        df_new.to_csv(DATA_DIR / f"snapshots/azure_diff_{datetime.date.today()}.csv", index=False)
        
        if MASTER_CSV.exists():
            df_master = pd.read_csv(MASTER_CSV)
            df_master = pd.concat([df_new, df_master]).drop_duplicates(subset=['Service_Path', 'Endpoint', 'Method'], keep='first')
            df_master.to_csv(MASTER_CSV, index=False, encoding='utf-8-sig')
        else:
            df_new.to_csv(MASTER_CSV, index=False, encoding='utf-8-sig')
        print(f"✅ Azure 업데이트 완료 ({len(new_data)}건)")

if __name__ == "__main__":
    run_sync()