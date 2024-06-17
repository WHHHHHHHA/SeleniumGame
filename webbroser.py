# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.ignore_local_proxy_environment_variables()
ser = Service()
ser.path = r'C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(options=opts,service=ser)
driver.get("https://www.baidu.com") # 打开百度浏览器

time.sleep(3) #等待3秒
driver.quit() #关闭浏览器
