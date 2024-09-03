from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

chrome_driver.maximize_window()
chrome_driver.get("https://testpmt.azurewebsites.net/")
chrome_driver.implicitly_wait(time_to_wait= 2)

print(chrome_driver.title)
chrome_driver.close()
chrome_driver.quit()