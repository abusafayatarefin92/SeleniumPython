import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

@pytest.fixture()
def edge_driver_handicap():
    edge_driver_handicap = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    edge_driver_handicap.maximize_window()
    edge_driver_handicap.implicitly_wait(10)

    yield edge_driver_handicap

    edge_driver_handicap.close()
    edge_driver_handicap.quit()

def test_handicap_login(edge_driver_handicap):
    edge_driver_handicap.get("https://test.jobs.hi-bd.org/login")


    time.sleep(5)

    your_email = edge_driver_handicap.find_element(By.XPATH,
                                                   '//*[@id="form2Example11"]')
    your_email.send_keys('safayatarefin@gmail.com')
    password = edge_driver_handicap.find_element(By.XPATH,
                                                 '//*[@id="form2Example22"]')
    password.send_keys('123456')
    log_in = edge_driver_handicap.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div/div/div/section/div/div/div/div/div[2]/div/div/div/form/div[3]/button')
    log_in.click()

    time.sleep(5)
    print('Test Completed')