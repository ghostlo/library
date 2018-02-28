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
import requests

def gii(argv):
	arg=str(argv)
	WebDriverWait(driver, 1, poll_frequency=0.01).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/ul/li['+arg+']')))
	time.sleep(0.1)
	driver.find_element_by_xpath('/html/body/div/ul/li['+arg+']').click()
	if EC.text_to_be_present_in_element((By.XPATH,'//*[@id="title:book-tip-info"]'),u'预约确认')==True:
		driver.find_element_by_xpath('/html/body/div[3]/div/table/tbody/tr[3]/td/div[2]/button[2]').click()
		print 'it is done'
		print 'congratulation'
		driver.close()
		driver.quit()
	else:
		time.sleep(0.1)
		driver.find_element_by_class_name('ui-popup').click()
		a1=driver.find_element_by_class_name('ui-popup')
		a1.find_element_by_css_selector('.ui-dialog-close').click()

def choose():
	for i in range[1:18]
		gii(i)

req=requests.get('http://seat.lib.bit.edu.cn/api.php/space_days/17')

try:
	req1=req.json()
	req2=req1.get("data").get("list")
	last = str(req2[1].get('day'))
except ValueError:
	print 'oh day'
	time.sleep(1)
	req = requests.get('http://seat.lib.bit.edu.cn/api.php/space_days/17')
	try:
		req1 = req.json()
		req2 = req1.get("data").get("list")
		last = str(req2[1].get('day'))
	except ValueError:
		print 'noday'

def segment(url):
	req=requests.get(url)
	try:
		req1=req.json()
		req2=req1.get("data").get('list')
		return req2[0].get('bookTimeId')
	except ValueError:
		print 'oh segment'
		time.sleep(1)
		req = requests.get(url)
		try:
			req1 = req.json()
			req2 = req1.get("data").get('list')
			return req2[0].get('bookTimeId')
		except ValueError:
			print 'nosegment'
			driver.close()
			driver.quit()

# 使用chromedriver 初始位置在downloads里
driver = webdriver.Chrome('/your webdriver path') 

# 登录
driver.get('http://seat.lib.bit.edu.cn/Home/web/index/area/1')
time.sleep(30)

try:
	driver.find_element_by_xpath("/html/body/div[1]/span[4]/a").click()
except Exception as e:
	time.sleep(1)
	print 'oh register'
	driver.find_element_by_xpath("/html/body/div[1]/span[4]/a").click()

username=raw_input("你的用户名:")
password=raw_input("你的密码:")

driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)

driver.find_element_by_xpath('//*[@id="casLoginForm"]/ul/li[4]/input').click()

segment1=str(segment('http://seat.lib.bit.edu.cn/api.php/space_time_buckets?day='+last+'&area=17'))
segment2=str(segment('http://seat.lib.bit.edu.cn/api.php/space_time_buckets?day='+last+'&area=16'))

# 页面
while True:
	now=int(time.strftime('%H',time.localtime(time.time())))
	if now==6:
		break
	else:
		continue

# 页面
time.sleep(0.1)
driver.get('http://seat.lib.bit.edu.cn/Home/Web/area?area=17&segment='+segment1+'&day='+last+'&startTime=08:00&endTime=22:40')
time.sleep(0.05)
choose()
driver.get('http://seat.lib.bit.edu.cn/Home/Web/area?area=16&segment='+segment2+'&day='+last+'&startTime=08:00&endTime=22:40')
time.sleep(0.05)
choose()
print "I can't help you"
driver.close()
driver.quit()