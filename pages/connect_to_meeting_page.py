import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class ConnectToMeetingPage(BasePage):

    PAGE_URL = Links.CONNECT_TO_MEETING_PAGE

    IDENTIFIER_FIELD = ("xpath", "(//input[@id='standard-error-helper-text'])[1]")
    USER_NAME_FIELD = ("xpath", "(//input[@id='standard-error-helper-text'])[2]")
    ENTER_BUTTON = ("xpath", "//button[contains(@class, 'MuiButton-containedPrimary')]")


    @allure.step("Enter meet identifier")
    def enter_meet_identifier(self, room_id):
        identifier_field = self.wait.until(EC.element_to_be_clickable(self.IDENTIFIER_FIELD))
        identifier_field.send_keys(room_id)

    @allure.step("Enter user name")
    def enter_user_name(self, user_name):
        name_field = self.wait.until(EC.element_to_be_clickable(self.USER_NAME_FIELD))
        name_field.send_keys(user_name)

    @allure.step("Click enter button")
    def click_enter_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_BUTTON)).click()
