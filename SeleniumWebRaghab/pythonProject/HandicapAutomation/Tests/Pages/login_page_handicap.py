from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, edge_driver_handicap):
        self.edge_driver_handicap = edge_driver_handicap
        self.username_textbox = (By.XPATH, '//*[@id="username"]')
        self.password_textbox = (By.XPATH, '//*[@id="password"]')
        self.login_button = (By.XPATH,'//*[@id="signup"]/form/div[3]/button')

    def open_page(self, url_handicap):
        self.edge_driver_handicap.get(url_handicap)

    def enter_username(self, username_handicap):
        self.edge_driver_handicap.find_element(*self.username_textbox).send_keys(username_handicap)

    def enter_password(self, password_handicap):
        self.edge_driver_handicap.find_element(*self.password_textbox).send_keys(password_handicap)

    def click_login_button(self):
        self.edge_driver_handicap.find_element(*self.login_button).click()