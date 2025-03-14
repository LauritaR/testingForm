from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver.get("https://www.facebook.com/r.php?entry_point=login")

input_elements = driver.find_elements(By.NAME, "firstname")
input_elements[0].send_keys("Jonas")


time.sleep(50)

