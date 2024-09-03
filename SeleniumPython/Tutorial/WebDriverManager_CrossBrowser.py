from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select

# browser_name = 'edge'
#
# if  browser_name == 'chrome':
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# elif browser_name == 'firefox':
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# elif browser_name == 'edge':
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# else:
#     print('please choose browser from chrome, firefox & edge')

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://test.jobs.hi-bd.org/admin/login")

time.sleep(5)

your_email = driver.find_element(By.XPATH, '//*[@id="username"]')
your_email.send_keys('arefin_super_admin')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('123456')

time.sleep(3)

log_in = driver.find_element(By.XPATH,'//*[@id="signup"]/form/div[3]/button')
log_in.click()

time.sleep(5)

recruitment_request = driver.find_element(By.XPATH, '//*[@id="main-menu"]/ul/li[2]/a')
recruitment_request.click()
time.sleep(3)

hiring_manager = driver.find_element(By.XPATH, '//*[@id="main-menu"]/ul/li[2]/ul/li[2]/a')
hiring_manager.click()
time.sleep(3)

recruitment_request_add = driver.find_element(By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/a')
recruitment_request_add.click()
time.sleep(5)

project_or_department = driver.find_element(By.XPATH, '//*[@id="department"]')
project_or_department_select = Select(project_or_department)
project_or_department_select.select_by_visible_text('Finance')
time.sleep(3)

# job_id = driver.find_element(By.XPATH, '//*[@id="11"]/td[2]/a').text
# print(job_id)

print(driver.title)
driver.close()
driver.quit()