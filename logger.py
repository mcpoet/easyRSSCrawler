#coding=utf-8

import time
import os, sys
from datetime import datetime
import logging

logging.basicConfig(filename = os.path.join(os.getcwd(), 'logging/all.log'), level = logging.INFO, 
					format = ('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# log = logging.getLogger('root.test')  
# log.setLevel(logging.INFO)    

logger = logging.getLogger('crawlerlogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
# infoL = logging.FileHandler('info.log')
# infoL.setLevel(logging.INFO)
# debugL = logging.FileHandler('debug.log')
# debugL.setLevel(logging.DEBUG)
# warnL = logging.FileHandler('warning.log')
# warnL.setLevel(logging.WARN)

# 再创建一个handler，用于输出到控制台
# consoleH = logging.StreamHandler()
# consoleH.setLevel(logging.DEBUG)

# 定义handler的输出格式
# logger.setFormatter(formatter)
# infoL.setFormatter(formatter)
# debugL.setFormatter(formatter)
# warnL.setFormatter(formatter)

# 给logger添加handler
# logger.addHandler(infoL)
# logger.addHandler(debugL)
# logger.addHandler(warnL)

if __name__ == '__main__':	
	while 1:
		logging.info("Info logging")
		logging.debug("Debug logging")
		logging.warn("Warning aaaa logging")
		logger.info("Innnnnnnformation ... ")
		print "would pring also print ?"
		time.sleep(2)
