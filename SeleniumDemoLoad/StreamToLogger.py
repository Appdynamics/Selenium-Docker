import sys
import logging

logger = logging.getLogger('STDERR')

class StreamToLogger(object):

    @staticmethod
    def setLevel(log_level):
        logger.setLevel(log_level)

    @staticmethod
    def addHandler(logHandler):
        logger.addHandler(logHandler)

    """def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.line_bug = ''"""

    @staticmethod
    def write(buf):
        for line in buf.rstrip().splitlines():
            logger.info(line.rstrip())
