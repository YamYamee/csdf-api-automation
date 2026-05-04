import json
import pandas as pd
import re
import os
from urllib.parse import urlparse

def deep_extract(data, key_map):
    """딕셔너리나 리스트를 재귀적으로 탐색하며 필요한 키값을 모두 찾아냄"""
    results = {k: "n/a" for k in key_map}
    
    def search(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in key_map and results[k] == "n/a":
                    results[k] = str(v)
                search(v)
        elif isinstance(obj, list):
            for item in obj:
                search(item)
    
    search(data)
    return results

def parse_azure_log_final(file_path):
    parsed_data = []
    # 추출하고 싶은 핵심 키워드들
    target_keys = [
        'tenantId', 'displayName', 'createdDateTime', 
        'technicalNotificationMails', 'city', 'street', 
        'code', 'message', 'id', 'type'
    ]

    with open(file_path, 'r', encoding='utf-8-sig') as f:
        for line in f:
            parts = [p.strip() for p in line.split(' | ')]
            if len(parts) < 5: continue
            
            time, method, url, status, body = parts[0], parts[1], parts[2], parts[3], parts[4]
            
            # 1. 일단 정규표현식으로 '생 데이터'에서 1차 갈취 (JSON 깨짐 대비)
            # 예: "displayName":"성균관대..." 추출
            regex_extract = {}
            for key in target_keys:
                match = re.search(f'"{key}"\s*:\s*"?([^",}}]+)"?', body, re.I)
                regex_extract[key] = match.group(1) if match else "n/a"

            # 2. JSON 파싱 시도 (온전한 경우 더 정확한 매핑)
            json_extract = {k: "n/a" for k in target_keys}
            try:
                json_obj = json.loads(body)
                json_extract = deep_extract(json_obj, target_keys)
            except:
                pass # 잘린 JSON은 정규표현식 결과에 의존

            # 3. 데이터 우선순위 결정 (JSON 우선, 없으면 정규표현식)
            final = {k: (json_extract[k] if json_extract[k] != "n/a" else regex_extract[k]) for k in target_keys}

            # 4. 결과 조립
            parsed_data.append({
                "Time": time,
                "Method": method,
                "Status": status,
                "Tenant_ID": final['tenantId'],
                "Entity_Name": final['displayName'],
                "Created_At": final['createdDateTime'],
                "Tech_Contact": final['technicalNotificationMails'],
                "Address": f"{final['city']} {final['street']}".strip(),
                "Error_Summary": f"[{final['code']}] {final['message']}" if final['code'] != "n/a" else "n/a",
                "Sub_ID": re.search(r'subscriptions/([a-z0-9-]+)', url + final['id'], re.I).group(1) if re.search(r'subscriptions/([a-z0-9-]+)', url + final['id'], re.I) else "n/a",
                "Resource_Type": final['type'],
                "URL": url
            })

    return pd.DataFrame(parsed_data)

# 실행
df = parse_azure_log_final('azure_raw_logs.txt')
if not os.path.exists('data'): os.makedirs('data')
df.to_csv("data/analyzed_evidence_final.csv", index=False, encoding='utf-8-sig')

print("\n✅ [포렌식 정밀 파싱 완료]")
# 데이터가 실제로 뽑혔는지 샘플 확인
print(df[df['Entity_Name'] != 'n/a'][['Time', 'Entity_Name', 'Tech_Contact', 'Error_Summary']].head())