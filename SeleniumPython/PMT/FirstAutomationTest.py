import time

from selenium import webdriver
# from selenium.webdriver.edge.options import Options

option = webdriver.EdgeOptions()
edge_driver = webdriver.Edge(options= option)

edge_driver.maximize_window()
edge_driver.get("https://pmttest.scibd.info/")
edge_driver.implicitly_wait(time_to_wait= 2)

print(edge_driver.title)
time.sleep(3)
edge_driver.close()