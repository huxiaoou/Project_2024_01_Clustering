import logging
from logzero import logger as logger0
from loguru import logger as logger1
from decorator import SFG

# logging
logging.basicConfig(encoding='utf-8', level=logging.DEBUG, format="%(asctime)s.%(msecs)06d [%(levelname)s] %(message)s", datefmt="%Y%m%d %H:%M%S")

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# log zero
logger0.debug("hello")
logger0.info("info")
logger0.warning("warn")
logger0.error("error")

# loguru
logger1.add("a.log")
logger1.debug('This is debug information')
logger1.info(f'This is info information {SFG("Green text")}')
logger1.warning('This is warn information')
logger1.error('This is error information')
