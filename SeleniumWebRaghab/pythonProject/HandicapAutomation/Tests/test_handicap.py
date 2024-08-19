import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from HandicapAutomation.Tests.Pages.login_page_handicap import LoginPage
from HandicapAutomation.Tests.Pages.recruitmentRequestAdd import RecruitmentRequestAdd

@pytest.fixture()
def edge_driver_handicap():
    edge_driver_handicap = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    edge_driver_handicap.maximize_window()
    edge_driver_handicap.implicitly_wait(10)

    yield edge_driver_handicap

    edge_driver_handicap.close()
    edge_driver_handicap.quit()

def test_handicap_login(edge_driver_handicap):
    login_page = LoginPage(edge_driver_handicap)
    recruitment_request_add = RecruitmentRequestAdd(edge_driver_handicap)

    #login
    login_page.open_page('https://test.jobs.hi-bd.org/admin/login')
    time.sleep(4)
    login_page.enter_username('arefin_super_admin')
    login_page.enter_password('123456')
    time.sleep(4)
    login_page.click_login_button()
    time.sleep(4)

    #Add new recruitment Request
    recruitment_request = edge_driver_handicap.find_element(By.XPATH, '//*[@id="main-menu"]/ul/li[2]/a')
    recruitment_request.click()
    time.sleep(3)
    hiring_manager = edge_driver_handicap.find_element(By.XPATH, '//*[@id="main-menu"]/ul/li[2]/ul/li[2]/a')
    hiring_manager.click()
    time.sleep(2)
    recruitment_request_add.recruitment_request_add()
    time.sleep(1)
    recruitment_request_add.select_project_or_department('Finance')
    time.sleep(1)
    recruitment_request_add.insert_hiring_manager('Meftaul Haque')
    time.sleep(1)
    recruitment_request_add.insert_vacant_position_title('Executive')
    time.sleep(1)
    recruitment_request_add.select_job_description('Project Officer_Job Description')
    time.sleep(1)
    recruitment_request_add.insert_number_of_position('2')
    time.sleep(1)
    recruitment_request_add.select_employee_at_present('No')
    time.sleep(1)
    recruitment_request_add.insert_location('Dhaka')
    time.sleep(1)
    recruitment_request_add.select_type_of_appointment('Permanent')
    time.sleep(1)
    job_starting_date = edge_driver_handicap.find_element(By.XPATH, '//*[@id="job_starting_date"]')
    job_starting_date.click()
    time.sleep(1)
    starting_date = edge_driver_handicap.find_element(By.XPATH, '/html/body/div[2]/div[1]/table/tbody/tr[5]/td[7]')
    starting_date.click()
    time.sleep(1)
    recruitment_request_add.insert_range_of_slary_from('15000')
    time.sleep(1)