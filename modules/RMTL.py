#Custom modules
import logging.config

logger = logging.getLogger(__name__)

def main():
    logger.info("read RMTL CSV")

def readRMTLCSV():
    logger.info("read RMTL CSV")

def readTargetFile():
    logger.info("read Target File")

def export():
    logger.info("Output Processed Target file")

def run(config):
    logger.info("run")
if __name__ == '__main__':
    main()