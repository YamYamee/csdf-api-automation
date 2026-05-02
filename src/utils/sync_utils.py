import sys
import csv
import requests
from pathlib import Path

def set_safe_limit():
    """Windows 환경의 CSV 필드 크기 제한 해결"""
    limit = sys.maxsize
    while True:
        try:
            csv.field_size_limit(limit)
            break
        except OverflowError:
            limit = int(limit / 10)

def get_changed_files(repo_full_name, last_sha, base_branch="main", token=None):
    """GitHub Compare API를 사용하여 변경된 파일 목록 추출"""
    headers = {"Authorization": f"token {token}"} if token else {}
    # 브랜치 명칭(base_branch)을 동적으로 받음
    url = f"https://api.github.com/repos/{repo_full_name}/compare/{last_sha}...{base_branch}"
    
    print(f"🔍 [DEBUG] API 호출: {url}")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ [ERROR] API 실패({response.status_code}): {response.text}")
        return []
    
    data = response.json()
    files = [f['filename'] for f in data.get('files', []) if f['status'] in ['added', 'modified']]
    
    print(f"🔍 [DEBUG] 발견된 변경 파일 수: {len(files)}")
    return files

def get_raw_content(repo_full_name, file_path, base_branch="main"):
    """Raw 파일 내용 가져오기"""
    url = f"https://raw.githubusercontent.com/{repo_full_name}/{base_branch}/{file_path}"
    res = requests.get(url)
    if res.status_code != 200:
        print(f"⚠️ [WARN] 파일 로드 실패: {file_path}")
        return None
    return res.json()