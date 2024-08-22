#!/opt/homebrew/Caskroom/miniforge/base/envs/oparcels/bin/python
import os
import shutil

base_dir = '../../Data/originals/mld'
des_dir = os.path.join(base_dir, 'mld_gz')

for year in range(1997,2025):
    folder_name = f'mld.hycom_030.{year}'
    folder_path = os.path.join(base_dir, folder_name)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # 4. 해당 폴더 내의 모든 파일을 이동
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                shutil.move(file_path, des_dir)
                print(f"Moved: {file_path} to {des_dir}")
        # 5. 폴더가 비었으면 폴더 삭제
        try:
            os.rmdir(folder_path)
            print(f"Deleted folder: {folder_path}")
        except OSError as e:
            print(f"Error deleting folder {folder_path}: {e}")
