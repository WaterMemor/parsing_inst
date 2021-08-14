import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup
import locale
import shutil
import time
import os.path

driver = webdriver.Firefox(executable_path=r'C:\\Program Files\\geckodriver.exe')
driver.get('https://www.instagram.com/accounts/login/')

#регестрация
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
"input[name='username']"))).send_keys("your username")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
"input[name='password']"))).send_keys("your password")
link = driver.find_element(By.CSS_SELECTOR, "button[class='sqdOP  L3NKy   y3zKF     ']")
link.click()
time.sleep(10)
#два оповещения
link2 = driver.find_element(By.CSS_SELECTOR, "button[class='sqdOP yWX7d    y3zKF     ']")
if(link2):
    link2.click()
time.sleep(5)
link6 = driver.find_element(By.CSS_SELECTOR, "button[class='aOOlW   HoLwm ']")
if(link6):
    link6.click()
time.sleep(5)
#войти в профиль
# link4 = driver.find_element(By.CSS_SELECTOR, "span[class='_2dbep qNELH']")
# link4.click()
# time.sleep(10)
# link3 = driver.find_element(By.CSS_SELECTOR, "div[class='                     Igw0E     IwRSH        YBx95       _4EzTm                                                                                                              ']")
# link3.click()
# time.sleep(10)

#найти по хештегу
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
"input[placeholder='Поиск']"))).send_keys("#zharkovadesign\n")
time.sleep(5)
link3 = driver.find_element_by_class_name('yCE8d  ')
if(link3):
    link3.click()
time.sleep(5)

#зайти в пост
link7 = driver.find_elements_by_class_name('v1Nh3 ')
a = 0
times = 3
for i in link7:
    if a < times:
            i.click()
            time.sleep(10)
            #нажать лайк
            link8 = driver.find_element_by_class_name('fr66n')
            link8.click()
            #выйти
            link10 = driver.find_element(By.CSS_SELECTOR, "div[class='                     Igw0E     IwRSH      eGOV_         _4EzTm                                                                                  BI4qX            qJPeX            fm1AK   TxciK yiMZG']") 
            link10.click()
            a = a+1
time.sleep(10)
# driver.execute_script("window.open('https://www.instagram.com/explore/tags/zharkovadesign/', 'new_window')")
# time.sleep(10)



print('STOP')
