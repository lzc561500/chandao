import time
from data.read_data_excel import Data
from page.loginPage import Login
from selenium import webdriver
import pytest
import allure

class TestLogin:

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get(r"http://127.0.0.1/zentao/user-login.html")
        self.login = Login(self.driver,10,1)


    @allure.title('登录')
    @pytest.mark.parametrize('data',Data('./data/data.xls','data').readData())
    def test_login(self,data):
            allure.attach('用户名','输入用户名')
            username = data['用户名']
            allure.attach('密码','输入密码')
            password = data['密码']
            allure.attach('登录','点击登录按钮')
            self.login.login(username,password)
            allure.attach('截取图片','截取错误图片')
            self.login.is_alert(username)
            picture = self.login.read_picture(username)
            allure.attach(picture,'错误信息',attachment_type=allure.attachment_type.PNG)
            time.sleep(2)
            self.driver.delete_all_cookies()
            self.driver.refresh()






