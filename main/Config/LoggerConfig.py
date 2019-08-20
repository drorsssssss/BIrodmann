import logging


class LoggerConfig:
    def get_logger(self):
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%y-%m-%d %H:%M:%S',level=logging.INFO)
        return logging.getLogger(__name__)
