from logger import *

config.setFormat("%Y-%m-%d %H:%M:%S")

log = Log.init("example.log")

log.clean()
log.info("Test")