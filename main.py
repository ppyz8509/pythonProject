import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('D:\\webdriver\\chromedriver.exe')


driver = webdriver.Chrome(service=s)
driver.get("https://sc.npru.ac.th")
time.sleep(5)
driver.close()