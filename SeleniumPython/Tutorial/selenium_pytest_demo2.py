import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

@pytest.fixture()
def edge_driver_handicap2():
    edge_driver_handicap2 = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    edge_driver_handicap2.maximize_window()
    edge_driver_handicap2.implicitly_wait(10)

    yield edge_driver_handicap2

    edge_driver_handicap2.close()
    edge_driver_handicap2.quit()

@pytest.mark.parametrize('username, password', [
    ('safayatarefin@gmail.com', '12345'),
    ('mahbub.stc0510@gmail.com', 'Mahbub@0510')
])
def test_handicap_login(edge_driver_handicap2, username, password):
    edge_driver_handicap2.get("https://jobs.hi-bd.org/")

    time.sleep(5)

    login_button = edge_driver_handicap2.find_element(By.XPATH, '//*[@id="mobile-nav-menu"]/ul/li[2]/a')
    login_button.click()

    time.sleep(5)

    your_email_handicap = edge_driver_handicap2.find_element(By.XPATH, '//*[@id="form2Example11"]')
    your_email_handicap.send_keys(username)
    password_handicap = edge_driver_handicap2.find_element(By.XPATH, '//*[@id="form2Example22"]')
    password_handicap.send_keys(password)
    log_in = edge_driver_handicap2.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/section/div/div/div/div/div[2]/div/div/div/form/div[3]/button')
    time.sleep(5)
    log_in.click()

    time.sleep(5)