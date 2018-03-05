#
# -*- coding: utf-8 -*-
#
# by ghostlo 
#
# 运用selenium方法模拟浏览器

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# help you choose seats
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

# get the segment in the url
def segment(url):
	i=1
	while i<11:
		try:
			req = requests.get(url)
			req1=req.json()
			req2=req1.get("data").get('list')
			return req2[0].get('bookTimeId')
		except ValueError:
			print "I can't find segment "+str(i)
			time.sleep(0.5)
			i=i+1

# chromedriver 
driver = webdriver.Chrome('/your webdriver path') 

# register
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

# the time
while True:
	now=int(time.strftime('%S',time.localtime(time.time())))
	if now==58 or now==59:
		break
	else:
		time.sleep(1)
		continue

while True:
	now=int(time.strftime('%H',time.localtime(time.time())))
	if now==6:
		break
	else:
		continue

# get the date of next day
i=1
a=False
while i<11:
	try:
		req = requests.get('http://seat.lib.bit.edu.cn/api.php/space_days/17')
		req1=req.json()
		req2=req1.get("data").get("list")
		last = str(req2[1].get('day'))
		a=True
		break
	except Exception:
		print "I can't find day "+ str(i)
		time.sleep(0.5)
		i=i+1


if a==False:
	print 'your network is broken'
	exit()

segment1=str(segment('http://seat.lib.bit.edu.cn/api.php/space_time_buckets?day='+last+'&area=17'))
segment2=str(segment('http://seat.lib.bit.edu.cn/api.php/space_time_buckets?day='+last+'&area=16'))

# page
time.sleep(0.1)
driver.get('http://seat.lib.bit.edu.cn/Home/Web/area?area=17&segment='+segment1+'&day='+last+'&startTime=08:00&endTime=22:40')
time.sleep(0.05)
choose()
driver.get('http://seat.lib.bit.edu.cn/Home/Web/area?area=16&segment='+segment2+'&day='+last+'&startTime=08:00&endTime=22:40')
time.sleep(0.05)
choose()
print "Seats are not available"
driver.close()
driver.quit()
