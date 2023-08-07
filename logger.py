import timeit
import logging

logger = logging.getLogger(__name__)
f_handler = logging.FileHandler('file.log')
f_format = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)5s() - %(levelname)s - %(message)s - %(msecs)dms',
                             datefmt="%d-%b-%y %H:%M:%S")
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)
logger.setLevel(logging.DEBUG)
