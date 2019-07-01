import logging

class Logger():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter('%(message)s')
        console_handler.setFormatter(console_format) # Only message is shown in console

        file_handler = logging.FileHandler('./mummy.log')
        file_handler.setLevel(logging.DEBUG) # All is logged to file
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
        file_handler.setFormatter(file_format)
        
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
    def log(self, message):
        self.logger.info(message)

logger = Logger()
logger.log('message')