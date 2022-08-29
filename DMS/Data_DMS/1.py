import logging
import time
import traceback


logger = logging.getLogger(__name__)
formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = logging.FileHandler(str(time.time()) + '.txt')
fh.setFormatter(formatter1)
logger.addHandler(fh)
logger.error(traceback.format_exc())
logger.info(123)