import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿


class VerificationCode:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"g:/chromedriver.exe")
        self.find_element = self.driver.find_element_by_css_selector

driver = webdriver.Chrome(executable_path=r"g:/chromedriver.exe")


# driver.get('https://www.baidu.com')
#
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# driver.quit()



driver.get('https://www.baidu.com/')
