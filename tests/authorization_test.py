import allure
from base.base_test import BaseTest

@allure.feature("Authorization functionality")
class TestAuthorization(BaseTest):

    @allure.title("Invalid authorization")
    @allure.severity("Normal")
    def test_invalid_authorization(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.check_push_incorrect_data()
        self.login_page.is_opened()
        self.login_page.make_screenshot("The user is not logged in")


