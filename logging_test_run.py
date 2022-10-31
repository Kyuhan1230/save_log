import time
from logging_sample_class import *

i = 0

while i < 10000:
    for k in range(3):
        Sample(k).run()
        time.sleep(.5)
        print(k, i)
    i += 1

    # 스케쥴러를 이용하여 오래된 파일을 계속 백업한다고 가정할 때
    if i % 10 == 0:
        from tracking_logfile import *
        file_path = './logging_study/'
        move_file(dir_path=file_path, file_format='.log.')
