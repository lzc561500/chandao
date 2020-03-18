from base.common_functions import Fuction
import time

class Login(Fuction):
    loc_username = ("css selector","#account")
    loc_password = ("name","password")
    loc_login = ("css selector","#submit")

    def login(self,username,password):
        self.sendKeys(self.loc_username,username)
        time.sleep(1)
        self.sendKeys(self.loc_password,password)
        time.sleep(2)
        self.click(self.loc_login)






