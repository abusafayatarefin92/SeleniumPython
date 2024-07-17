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

login_button = edge_driver.find_element(By.XPATH, '//*[@id="mobile-nav-menu"]/ul/li[2]/a')
login_button.click()

time.sleep(5)

print(edge_driver.title)
edge_driver.close()
edge_driver.quit()