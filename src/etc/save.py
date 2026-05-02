import os
import csv
import time

# 1. 경로 설정 (C:\azure 폴더 기준)
REPO_ROOT = r"C:\azure"
SEARCH_PATH = os.path.join(REPO_ROOT, "specification")
OUTPUT_FILE = "azure_spec_paths_local.csv"

def get_api_paths_local():
    found_paths = []
    
    print(f"--- [로컬 탐색 시작] ---")
    print(f"탐색 경로: {SEARCH_PATH}")
    
    # os.walk는 하위 모든 폴더를 가장 빠르게 탐색합니다.
    # root: 현재 탐색 중인 폴더 경로
    # dirs: 해당 폴더 안에 있는 하위 폴더 리스트
    # files: 해당 폴더 안에 있는 파일 리스트
    for root, dirs, files in os.walk(SEARCH_PATH):
        # 현재 폴더 목록(dirs)에서 stable이나 preview가 있는지 확인
        for d in dirs:
            name_lower = d.lower()
            if name_lower in ["stable", "preview"]:
                # 전체 절대 경로 생성
                full_path = os.path.join(root, d)
                
                # C:\azure 부분을 떼어내고 상대 경로만 추출 (예: specification/...)
                rel_path = os.path.relpath(full_path, REPO_ROOT)
                
                # 윈도우 경로 구분자(\)를 API 스타일인 (/)로 변경
                clean_path = rel_path.replace("\\", "/")
                
                found_paths.append(clean_path)
                print(f"   >> [찾음] {clean_path}")
                
                # 효율을 위해 stable/preview를 찾은 경우 그 안의 하위 폴더는 더 이상 뒤지지 않음
                # (예: stable 폴더 안에 또 stable이 있는 경우는 거의 없으므로)
                # 이 옵션은 필요에 따라 끄거나 켤 수 있습니다.
                # if name_lower in ["stable", "preview"]:
                #     dirs.remove(d) 

    return found_paths

def save_to_csv(paths, filename):
    if not paths:
        print("\n[알림] 찾은 경로가 없습니다. 저장소에 specification 폴더가 있는지 확인하세요.")
        return

    # 경로 정렬 (가나다순)
    sorted_paths = sorted(list(set(paths)))

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Folder Path"])
        for path in sorted_paths:
            writer.writerow([path])
            
    print(f"\n--- [완료] ---")
    print(f"총 {len(sorted_paths)}개의 경로를 '{filename}'에 저장했습니다.")

if __name__ == "__main__":
    start_time = time.time()
    
    # 1. 로컬 경로 존재 확인
    if os.path.exists(SEARCH_PATH):
        # 2. 탐색 실행
        results = get_api_paths_local()
        # 3. CSV 저장
        save_to_csv(results, OUTPUT_FILE)
    else:
        print(f"!! 에러: {SEARCH_PATH} 경로를 찾을 수 없습니다.")
        print("정상적으로 git sparse-checkout이 완료되었는지 확인하세요.")
    
    duration = time.time() - start_time
    print(f"소요 시간: {round(duration, 2)}초")