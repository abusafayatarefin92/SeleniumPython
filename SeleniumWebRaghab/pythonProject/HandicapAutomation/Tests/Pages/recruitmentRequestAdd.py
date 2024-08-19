from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RecruitmentRequestAdd:
    def __init__(self, edge_driver_handicap):
        self.edge_driver_handicap = edge_driver_handicap
        self.recruitment_request_add_button = (By.XPATH, '//*[@id="right-panel"]/div[1]/div/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/a')
        self.project_or_department_select = (By.XPATH, '//*[@id="department"]')
        self.hiring_manager_text = (By.XPATH, '//*[@id="name_of_department"]')
        self.vacant_position_title_text = (By.XPATH, '//*[@id="position_title"]')
        self.job_description_select = (By.XPATH, '//*[@id="job_description"]')
        self.number_of_position_text = (By.XPATH, '//*[@id="number_of_position"]')
        self.employee_at_present_select = (By.XPATH, '//*[@id="employee_at_present"]')
        self.location_text = (By.XPATH, '//*[@id="location"]')
        self.type_of_appointment_select = (By.XPATH, '//*[@id="appointment_type"]')
        self.range_of_slary_from_text = (By.XPATH, '//*[@id="salary_range_from"]')

    def recruitment_request_add(self):
        self.edge_driver_handicap.find_element(*self.recruitment_request_add_button).click()

    def select_project_or_department(self, name):
        value = self.edge_driver_handicap.find_element(*self.project_or_department_select)
        project_or_department_name = Select(value)
        project_or_department_name.select_by_visible_text(name)

    def insert_hiring_manager(self, text):
        self.edge_driver_handicap.find_element(*self.hiring_manager_text).send_keys(text)

    def insert_vacant_position_title(self, text):
        self.edge_driver_handicap.find_element(*self.vacant_position_title_text).send_keys(text)

    def select_job_description(self, name):
        value = self.edge_driver_handicap.find_element(*self.job_description_select)
        job_description_name = Select(value)
        job_description_name.select_by_visible_text(name)

    def insert_number_of_position(self, text):
        self.edge_driver_handicap.find_element(*self.number_of_position_text).send_keys(text)

    def select_employee_at_present(self, name):
        value = self.edge_driver_handicap.find_element(*self.employee_at_present_select)
        employee_at_present = Select(value)
        employee_at_present.select_by_visible_text(name)

    def insert_location(self, text):
        self.edge_driver_handicap.find_element(*self.location_text).send_keys(text)

    def select_type_of_appointment(self, name):
        value = self.edge_driver_handicap.find_element(*self.type_of_appointment_select)
        type_of_appointment = Select(value)
        type_of_appointment.select_by_visible_text(name)

    def insert_range_of_slary_from(self, text):
        self.edge_driver_handicap.find_element(*self.range_of_slary_from_text).send_keys(text)