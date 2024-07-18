import pytest

from HANDICAP.Config.Config import TestData
from HANDICAP.Pages.Application_Pages.Application_Login_Page import LoginPage
from HANDICAP.Tests.Base_Test import BaseTest


class TestApplicantLoginPage(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.ApplicantLoginPage_Title)
        assert title == TestData.ApplicantLoginPage_Title

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.User_Name, TestData.Password)
