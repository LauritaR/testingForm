from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
try:
    service=Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service)

    driver.get("https://www.facebook.com/r.php?entry_point=login")
    time.sleep(2)
    click_elements = driver.find_elements(By.XPATH, '//*[@id="facebook"]/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]')
    click_elements[0].click()

    firs_tname= driver.find_elements(By.NAME, "firstname")
    firs_tname[0].send_keys("Robotas")
    last_name = driver.find_elements(By.NAME, "lastname")
    last_name[0].send_keys("Robotauskas")

    year_of_birth = driver.find_elements(By.NAME, "birthday_year")
    year_of_birth[0].send_keys("2000")
    month_of_birth = driver.find_elements(By.NAME, "birthday_month")
    month_of_birth[0].send_keys("May")
    day_of_birth = driver.find_elements(By.NAME, "birthday_day")
    day_of_birth[0].send_keys("19")

    gender = driver.find_element(By.CSS_SELECTOR, "input[name='sex'][value='-1']")
    gender.click()
    preferred_pronoun = driver.find_element(By.XPATH,'//*[@id="preferred_pronoun"]/option[4]')
    preferred_pronoun.click()

    email = driver.find_elements(By.NAME, "reg_email__")
    email[0].send_keys("robotas.robotauskas@mif.stud.vu.lt")
    password = driver.find_elements(By.NAME, "reg_passwd__")
    password[0].send_keys("AsMyliuTestavima!159")

    submit = driver.find_element(By.NAME, "websubmit")
    submit.click()
    time.sleep(10)
finally:
    driver.quit()

