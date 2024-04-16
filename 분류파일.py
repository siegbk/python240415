import os
import shutil

# 다운로드 폴더 경로
downloads_path = r'c:\Users\student\Downloads'

# 파일을 이동할 하위 폴더
images_folder = os.path.join(downloads_path, 'images')
data_folder = os.path.join(downloads_path, 'data')
docs_folder = os.path.join(downloads_path, 'docs')
archive_folder = os.path.join(downloads_path, 'archive')

# 하위 폴더가 없으면 생성
os.makedirs(images_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 다운로드 폴더 내의 모든 파일을 분류 및 이동
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    
    # 파일인지 확인
    if os.path.isfile(file_path):
        # 파일 확장자를 소문자로 변환
        file_extension = os.path.splitext(filename)[1].lower()
        
        # 확장자에 따라 파일을 이동할 폴더를 지정
        if file_extension in ['.jpg', '.jpeg']:
            destination_folder = images_folder
        elif file_extension in ['.csv', '.xlsx']:
            destination_folder = data_folder
        elif file_extension in ['.txt', '.doc', '.pdf']:
            destination_folder = docs_folder
        elif file_extension == '.zip':
            destination_folder = archive_folder
        else:
            # 이외의 확장자는 다른 폴더로 이동하지 않음
            continue
        
        # 파일을 지정된 폴더로 이동
        shutil.move(file_path, os.path.join(destination_folder, filename))
        print(f"{filename}을 {destination_folder}로 이동했습니다.")

print("파일 분류 작업이 완료되었습니다.")
