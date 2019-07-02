from unittest import main, TestCase
from unittest.mock import patch
from importlib import reload
import log
def info():
    info.triggered_info = True
class MockLogger():
    def setLevel(self, level):
        pass
    def info(self, message):
        info()
    def addHandler(self, handler):
        pass
class MockHandler():
    def setLevel(self, level):
        pass
    def setFormatter(self, formater):
        pass
class MockFormatter():
    pass
class TestLogger(TestCase):
    @patch('logging.FileHandler')
    @patch('logging.Formatter')
    @patch('logging.StreamHandler')
    @patch('logging.getLogger')
    def setUp(self, getLogger, StreamHandler, Formatter, FileHandler):
        getLogger.return_value = MockLogger()
        StreamHandler.return_value = MockHandler()
        Formatter.return_value = MockFormatter()
        FileHandler.return_value = MockHandler()
        info.triggered_info = False
        reload(log)
        self.logger = log.Logger()
    def test_log(self):
        self.logger.log('message')
        self.assertTrue(info.triggered_info)

if __name__ == '__main__':
    main()