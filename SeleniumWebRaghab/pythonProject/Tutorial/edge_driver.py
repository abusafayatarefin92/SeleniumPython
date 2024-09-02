from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
import time

edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

edge_driver.maximize_window()
edge_driver.get("https://testpmt.azurewebsites.net/")
edge_driver.implicitly_wait(time_to_wait= 2)

edge_driver.find_element(By.XPATH, '//*[@id="LoginDiv"]/div/div/a').click()
time.sleep(3)
edge_driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys('centeruser@gmail.com')
time.sleep(1)
edge_driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys('12345')
time.sleep(1)
edge_driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[3]/button').click()
time.sleep(3)
# region = edge_driver.find_element(By.XPATH, '//*[@id="kt_body"]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/span/span[1]')
# region_select = Select(region)
# region_select.select_by_visible_text('Asia')
# time.sleep(3)
edge_driver.find_element(By.XPATH, '//*[@id="kt_body"]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/span/span[1]').click()
time.sleep(3)
# edge_driver.find_element(By.XPATH, '//*[@id="select2-RegionIdsyphkf1r9kfvzsai161yr-result-u8gj-1"]').click()
edge_driver.find_element(By.ID, 'select2-RegionIdsyphkf1r9kfvzsai161yr-result-u8gj-1').click()
time.sleep(3)

# project_or_department = driver.find_element(By.XPATH, '//*[@id="department"]')
# project_or_department_select = Select(project_or_department)
# project_or_department_select.select_by_visible_text('Finance')


print(edge_driver.title)
edge_driver.close()
edge_driver.quit()