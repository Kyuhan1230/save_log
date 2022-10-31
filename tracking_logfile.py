"""Rotating된 Log File을 지정된 폴더로 옮기기"""
# Import Lib
import os
import shutil
import time
from pathlib import Path


def get_file_names(dir_path, file_format='.csv'):
    """경로 내의 파일을 수정된 날짜 순으로 가져오기"""
    paths = sorted(Path(dir_path).iterdir(), key=os.path.getmtime)
    str_paths = [str(i) for i in paths if file_format in str(i)]
    return str_paths


def create_folder(dir_path, folder_name):
    """경로 내에 지정된 이름으로 폴더를 생성하기"""
    print("입력된 저장용 폴더: ", dir_path + folder_name)
    if not os.path.exists(dir_path + folder_name):
        os.makedirs(dir_path + folder_name)
    else:
        print("이미 해당 이름의 저장용 폴더가 생성되어 있습니다.")
    return dir_path + folder_name


def move_file(dir_path, file_format='.log.', now=None):
    """경로 내의 Log 파일의 이름을 읽고, 지정한 폴더로 옮기기"""
    if now is None:
        now = time.strftime("%Y%M%d_%H%M%S")
    file_names = get_file_names(dir_path='./logging_study', file_format=file_format)

    i = 0
    for f in file_names:
        front, _ = f.split(file_format)
        _, model_name = front.split('\\')

        create_folder(dir_path=dir_path, folder_name=model_name)

        where = dir_path + f'{model_name}/{model_name}_{now}_{i}.log'
        shutil.move(f, where)

        i += 1
