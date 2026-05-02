import pandas as pd
import os

# 1. 데이터 로드
file_path = "azure_spec_paths_local.csv"
df = pd.read_csv(file_path)

def analyze_stable_path_variability(df):
    results = []
    
    for path in df['Folder Path']:
        if 'stable' not in path.lower():
            continue
            
        parts = path.split('/')
        # 'stable' 인덱스 찾기
        try:
            stable_idx = [p.lower() for p in parts].index('stable')
        except ValueError:
            continue
            
        # stable 이전까지의 경로 추출
        prefix_parts = parts[:stable_idx]
        depth_to_stable = len(prefix_parts)
        
        # 경로 패턴 일반화 (구체적인 이름 대신 유형으로 변환)
        # 예: specification/compute/resource-manager/Microsoft.Compute -> spec/SERVICE/MODE/PROVIDER
        template = []
        for i, p in enumerate(prefix_parts):
            if i == 0: template.append("spec")
            elif p.startswith("Microsoft."): template.append("{Provider}")
            elif p in ["resource-manager", "data-plane"]: template.append(f"{{Mode:{p}}}")
            else: template.append("{Service/Group}")
        
        template_str = "/".join(template)
        
        results.append({
            "Full Path": path,
            "Prefix": "/".join(prefix_parts),
            "Depth to Stable": depth_to_stable,
            "Template": template_str,
            "Service": prefix_parts[1] if len(prefix_parts) > 1 else "root"
        })

    return pd.DataFrame(results)

# 분석 실행
var_df = analyze_stable_path_variability(df)

# 2. 주요 패턴 요약
print("--- [1. 가장 흔한 경로 패턴 Top 5] ---")
print(var_df['Template'].value_counts().head(5))

print("\n--- [2. 경로 깊이별 분포 (Stable까지 몇 단계인가?)] ---")
print(var_df['Depth to Stable'].value_counts().sort_index())

print("\n--- [3. 변칙적인(Minority) 패턴 사례] ---")
# 상위 패턴이 아닌 데이터들만 추출
top_patterns = var_df['Template'].value_counts().head(2).index
anomalies = var_df[~var_df['Template'].isin(top_patterns)]
print(anomalies[['Template', 'Full Path']].head(10))

# 3. 자동화를 위한 가이드 데이터 저장
var_df.to_csv("stable_path_analysis.csv", index=False)