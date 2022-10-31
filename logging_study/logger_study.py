import logging
"""
Log Levels
    - DEBUG: 프로그램 작동에 대한 상세한 정보를 가지는 로그. 문제의 원인을 파악할 때에만 이용.
    - INFO: 프로그램 작동이 예상대로 진행되고 있는지 트래킹하기 위해 사용.
    - WARNING: 예상치 못한 일이나 추후 발생 가능한 문제를 표시하기 위함.
    - ERROR: 심각한 문제로 인해 프로그램이 의도한 기능을 수행하지 못하고 있는 상황을 표시.
    - CRITICAL: 더욱 심각한 문제로 인해 프로그램 실행 자체가 언제라도 중단될 수 있음을 표시.
"""
# Setting Up Logger
logger = logging.getLogger(__name__)   # 로거의 이름: 로거가 생성된 네임스페이스를 따라 짓는 것이 관례
logger.setLevel(logging.DEBUG)

# Log Formatting
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

# Set Handler
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# Critical Event
formatter_critical = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
handler_critical = logging.FileHandler("log_event.log")
handler_critical.setLevel(logging.CRITICAL)
handler_critical.setFormatter(formatter_critical)

# 각 핸들러를 로거에 추가
logger.addHandler(handler)
logger.addHandler(handler_critical)

logger.info("Is working well?")
logger.critical("It's not working well.")
