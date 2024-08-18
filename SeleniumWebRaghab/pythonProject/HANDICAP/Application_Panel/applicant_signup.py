from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.implicitly_wait(5)
driver.get("https://jobs.hi-bd.org/login")
driver.maximize_window()

driver.find_element(By.NAME, 'email').send_keys("safayatarefin@gmail.com")
driver.find_element(By.NAME, 'password').send_keys("123456")
driver.find_element(By.XPATH, '//button[contains(text(),"Log")]').click()
