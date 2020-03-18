from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time


class Fuction:

    def __init__(self,driver:webdriver.Firefox,timeout,poll):
        self.driver = driver
        self.timeout = timeout
        self.poll = poll

    def findelement(self, loc):
        if not isinstance(loc, tuple):
            print("传的数据类型错误：如：loc=('id','value')")
        else:
            print("正在定位元素：定位元素方式>>>%s,value值>>>%s" % (loc[0], loc[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*loc))
            return ele

    def sendKeys(self,loc,text):
        ele=self.findelement(loc)
        ele.send_keys(text)

    def click(self,loc):
        ele = self.findelement(loc)
        ele.click()

    def is_alert(self,username):
        try:
            a = self.driver.switch_to.alert
            a.text
            time.sleep(1)
            a.accept()
            self.screenshot_full("login_%s" % username)
        except:
            return ''


    def screenshot_element(self,picturePath,loc):
        #新建一个图片保存地址及图片名
        self.driver.save_screenshot(picturePath)
        #获取要截图的元素
        ele = self.findelement(loc)
        #获取元素的坐标
        left = ele.location['x']
        top = ele.location['y']
        #获取图片大小
        width = left + ele.size['width']
        height = top + ele.size['height']
        #打开图片
        im = Image.open(picturePath)
        #将获取的图片复制指定的文件里
        picture =im.crop((left,top,width,height))
        #保存复制的图片
        picture.save(picturePath)

    def screenshot_full(self,fileName):
        self.driver.get_screenshot_as_file(r"F:\pycharm 2019\项目列表\复习\picture\\"+fileName+'.png')

    def read_picture(self,username):
        with open(r'F:\pycharm 2019\项目列表\复习\picture\login_%s.png' % username, 'rb') as f:
            return f.read()




