from selenium import webdriver
from base.common_functions import Fuction


class TestScreenShot:

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
        self.picture = Fuction(self.driver,10,1)

    def test_scteenshot(self):
        self.picture.screenshot_full('baidu')

