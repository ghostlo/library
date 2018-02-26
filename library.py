#
# -*- coding: utf-8 -*-
#
# help doc http://docs.seleniumhq.org/docs/#
# 运用selenium方法模拟浏览器

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gii(argv):
	arg=str(argv)
	WebDriverWait(driver, 1, poll_frequency=0.01).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/ul/li['+arg+']')))
	time.sleep(0.03)
	driver.find_element_by_xpath('/html/body/div/ul/li['+arg+']').click()
	if EC.text_to_be_present_in_element((By.XPATH,'//*[@id="title:book-tip-info"]'),u'预约确认')==True:
		driver.find_element_by_xpath('/html/body/div[3]/div/table/tbody/tr[3]/td/div[2]/button[2]').click()
		driver.close()
		driver.quit()
	else:
		time.sleep(0.1)
		driver.find_element_by_class_name('ui-popup').click()
		a1=driver.find_element_by_class_name('ui-popup')
		a1.find_element_by_css_selector('.ui-dialog-close').click()

def choose():
	for i in range(1,18):
		gii(i)
		
# 系统时间
orgintime = time.strftime('%d',time.localtime(time.time()))
orgintime1 = int(orgintime)
done = str(orgintime1+1)
tm=time.strftime('%Y-%m-',time.localtime(time.time()))
last = tm+done
# 年+月+日

# 使用chromedriver 初始位置在downloads里
driver = webdriver.Chrome('/Users/longxiansheng/Downloads/chromedriver')  # Optional argument, if not specified will search path.

# 登录
driver.get('http://seat.lib.bit.edu.cn/Home/web/index/area/1')
WebDriverWait(driver, 1, poll_frequency=0.01).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/span[4]/a')))
time.sleep(0.01)
driver.find_element_by_xpath("/html/body/div[1]/span[4]/a").click()

username=raw_input("你的用户名:")
password=raw_input("你的密码:")

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)

driver.find_element_by_xpath('//*[@id="casLoginForm"]/ul/li[4]/input').click()

# 页面
driver.get('http://seat.lib.bit.edu.cn/Home/Web/area?area=17&segment=95601&day='+last+'&startTime=08:00&endTime=22:40')
time.sleep(0.05)
choose()
driver.get('http://seat.lib.bit.edu.cn/Home/Web/area?area=16&segment=94870&day='+last+'&startTime=08:00&endTime=22:40')
time.sleep(0.05)
choose()
print "I can't help you"
driver.close()
driver.quit()