from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

edge_driver.maximize_window()
edge_driver.get("https://jobs.hi-bd.org/")

time.sleep(5)

print(edge_driver.title)

login_button = edge_driver.find_element(By.XPATH,
                                        '//*[@id="mobile-nav-menu"]/ul/li[2]/a')
login_button.click()

time.sleep(5)

print(edge_driver.title)

your_email = edge_driver.find_element(By.XPATH,
                                      '//*[@id="form2Example11"]')
your_email.send_keys('safayatarefin@gmail.com')
password = edge_driver.find_element(By.XPATH,
                                    '//*[@id="form2Example22"]')
password.send_keys('123456')
log_in = edge_driver.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div/div/section/div/div/div/div/div[2]/div/div/div/form/div[3]/button')
log_in.click()

print(edge_driver.title)

time.sleep(5)
edge_driver.close()
edge_driver.quit()