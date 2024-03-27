import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class MeetPage(BasePage):

    PAGE_URL = Links.MEET_PAGE

    ENTER_WITHOUT_CHECKING = ("xpath", "//button[@data-name='entry-without-check']")
    PUSH_ENTER_MEET = ("xpath", "//div[@class='notification info Appear-appear-done Appear-enter-done']")
    COUNT_PARTICIPANTS_ON_MEET = ("xpath", "//p[@class='title']")
    PARTICIPANTS_BUTTON = ("xpath", "//div[@data-name='room-members']")


    @allure.step("Enter without cheking")
    def click_on_enter_without_checking_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_WITHOUT_CHECKING)).click()

    @allure.step("Check push enter meet")
    def check_enter_meet_push(self):
        self.wait.until(EC.visibility_of_element_located(self.PUSH_ENTER_MEET))

    @allure.step("Check count of participants")
    def check_count_of_participants(self):
        self.wait.until(EC.visibility_of_element_located(self.COUNT_PARTICIPANTS_ON_MEET))
        self.wait.until(EC.text_to_be_present_in_element(self.COUNT_PARTICIPANTS_ON_MEET, "Участники (1)"))