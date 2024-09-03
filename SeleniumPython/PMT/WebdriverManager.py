from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

edge_driver.maximize_window()
edge_driver.get("https://testpmt.azurewebsites.net/")
edge_driver.implicitly_wait(time_to_wait= 2)

print(edge_driver.title)
edge_driver.close()