# pip install selenium

from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"g:/chromedriver.exe")


# driver.get('https://www.baidu.com')
#
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# driver.quit()



driver.get('http://122.152.233.159/ifadmin/admin/admincp.php')
driver.find_element_by_name("user").send_keys("mumu_wangjiachen")
driver.find_element_by_name("password").send_keys("mI07*HBxhU")
driver.find_element_by_class_name("btn").click()
time.sleep(3)
driver.find_element_by_link_text("数据库").click()
driver.find_element_by_link_text("SQL查询").click()
driver.find_element_by_name("sql").send_keys("select * from KrakenEvent limit 1")
driver.find_element_by_id("selectServer").clear()
driver.find_element_by_id("selectServer").send_keys("2")
driver.find_element_by_name("export").click()
time.sleep(10)
driver.quit()