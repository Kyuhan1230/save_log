import json
import random
import string
import datetime
import logging.config
# Logger 설정값 호출
path = './logging_study/'
config = json.load(open(path + 'logger.json'))
config['handlers']['file_rotate']['filename'] = None    # Rotating File 기본 저장 경로 -->  None


class Sample:
    def __init__(self, num):
        self.num = num
        # logger 설정값 - File이름 변경
        config['handlers']['file_rotate']['filename'] = path + f'Model_{num}.log'
        # logger 설정값 - Handler 이름 __name__ 적용
        key1 = list(config['loggers'].keys())[1]
        config['loggers'][__name__] = config['loggers'].pop(key1)
        # logger 설정값 적용
        logging.config.dictConfig(config)
        logger = logging.getLogger(__name__)

        self.logger = logger
        self.result = None

    def set_letter(self):
        """매우 긴 문자열 생성"""
        length = 941230
        result = ""
        for i in range(length):
            result += random.choice(string.ascii_letters)

        self.result = result

    def do_something(self):
        self.set_letter()
        self.logger.debug(self.result)

    def run(self):
        self.logger.info("Is working well?")
        self.logger.debug(f"{datetime.datetime.now().strftime('%X'), self.num}")
        self.do_something()
