# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import datetime
import requests
import random

def discord_send_message(text):
    now = datetime.datetime.now()
    message = {"content": f"{str(text)}"}
    requests.post(discord_url, data=message)
    print(message)

# ChromeDriver로 접속
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
discord_url = "https://discord.com/api/webhooks/1278371220399591446/A51sccPzLIUhEE_ZTJEmeYhQbqlXegzacEQniyHMlvbHSSZnZG6hZ7ewo5Ue-EkDJVHd"
# 웹페이지 호출
driver.get("https://enterpot.co.kr/reservation.html")
time.sleep(random.uniform(2,4))
test=driver.find_element(By.XPATH, '//*[@id="datepicker"] ')
time.sleep(random.uniform(2,4))
test.clear()

while 1:
    test.clear()
    test.send_keys("2024-10-03",Keys.ENTER)
    time.sleep(random.uniform(2,4))

    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[1]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-03][12:00] 예약불가")
    else:
        discord_send_message("[2024-10-03][12:00] 예약가능")

    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[2]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-03][14:00] 예약불가")
    else:
        discord_send_message("[2024-10-03][14:00] 예약가능")

        
    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[3]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-03][16:00] 예약불가")
    else:
        discord_send_message("[2024-10-03][16:00] 예약가능")

        
    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[4]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-03][18:00] 예약불가")
    else:
        discord_send_message("[2024-10-03][18:00] 예약가능")


        
    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[5]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-03][20:00] 예약불가")
    else:
        discord_send_message("[2024-10-03][20:00] 예약가능")
        
    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[6]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-03][22:00] 예약불가")
    else:
        discord_send_message("[2024-10-03][22:00] 예약가능")
        
    test.clear()
    test.send_keys("2024-10-05",Keys.ENTER)
    time.sleep(random.uniform(2,4))

    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[1]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-04][12:00] 예약불가")
    else:
        discord_send_message("[2024-10-04][12:00] 예약가능")

    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[2]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-04][14:00] 예약불가")
    else:
        discord_send_message("[2024-10-04][14:00] 예약가능")

        
    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[3]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-04][16:00] 예약불가")
    else:
        discord_send_message("[[2024-10-04][16:00] 예약가능")

        
    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[4]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-04][18:00] 예약불가")
    else:
        discord_send_message("[2024-10-04][18:00] 예약가능")


        
    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[5]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-04][20:00] 예약불가")
    else:
        discord_send_message("[2024-10-04][20:00] 예약가능")
        
    val=driver.find_element(By.XPATH, '//*[@id="themes"]/div[2]/div/div[6]/button').text;
    if "예약불가" in val:
        pass
        #discord_send_message("[2024-10-04][22:00] 예약불가")
    else:
        discord_send_message("[2024-10-04][22:00] 예약가능")
        


driver.close()
