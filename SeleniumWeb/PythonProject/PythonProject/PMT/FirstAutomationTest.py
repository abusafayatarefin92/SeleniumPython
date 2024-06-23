from selenium import webdriver
from selenium.webdriver.edge.options import Options

option = webdriver.EdgeOptions()
edge_driver = webdriver.Edge(options= option)

edge_driver.maximize_window()
edge_driver.get("https://testpmt.azurewebsites.net/")
edge_driver.implicitly_wait(time_to_wait= 2)

print(edge_driver.title)
edge_driver.close()