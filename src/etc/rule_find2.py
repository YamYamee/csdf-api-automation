import os
import pandas as pd

REPO_ROOT = r"C:\azure"

def deep_analysis(csv_file):
    df = pd.read_csv(csv_file)
    detailed_results = []

    for path in df['Folder Path']:
        full_path = os.path.join(REPO_ROOT, path)
        if not os.path.exists(full_path): continue

        # 1. 파일 구성 확인
        files = os.listdir(full_path)
        has_json = any(f.endswith('.json') for f in files)
        has_tsp = any(f.endswith('.tsp') for f in files)
        
        # 2. 부모 폴더에 readme.md가 있는지 확인 (Azure 스펙의 특징)
        parent_path = os.path.dirname(full_path)
        has_readme = os.path.exists(os.path.join(parent_path, "readme.md"))

        # 3. 서비스명 추출 (Microsoft.X)
        parts = path.split('/')
        provider = next((p for p in parts if p.startswith("Microsoft.")), "Unknown")

        detailed_results.append({
            "Path": path,
            "Provider": provider,
            "Has_JSON": has_json,
            "Has_TSP": has_tsp,
            "Has_Readme": has_readme
        })

    detail_df = pd.DataFrame(detailed_results)

    # 결과 분석 출력
    print("--- [심화 분석 결과] ---")
    print(f"TypeSpec(.tsp) 도입 서비스 수: {detail_df['Has_TSP'].sum()}")
    print(f"Readme.md 미보유 경로 수: {len(detail_df) - detail_df['Has_Readme'].sum()}")
    
    # Provider별 버전 밀도 계산
    density = detail_df.groupby('Provider').size().sort_values(ascending=False)
    print("\n[버전 밀도 Top 5 서비스]")
    print(density.head(5))

    return detail_df

# 실행
# detail_df = deep_analysis("azure_spec_paths_local.csv")