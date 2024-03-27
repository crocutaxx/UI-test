import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Connect to meeting Functionality")
class TestConnectingUsersToMeeting(BaseTest):

    # Данный тест выполняется с ошибкой для примера, т.к. в нем используются невалидные данные
    @pytest.mark.smoke
    @allure.title("Connecting to the meeting as an unauthorized user")
    @allure.severity("Critical")
    def test_connecting_to_meeting_wtih_id_unauth_user(self):

        self.login_page.open()
        self.login_page.click_enter_meet_button()
        self.connect_to_meeting_page.is_opened()
        self.connect_to_meeting_page.enter_meet_identifier("123456789")
        self.connect_to_meeting_page.enter_user_name("Cat")
        self.connect_to_meeting_page.click_enter_button()
        self.meet_page.click_on_enter_without_checking_button()
        self.meet_page.click_on_enter_without_checking_button()
        self.meet_page.check_enter_meet_push()
        self.meet_page.make_screenshot("Connect to the meet")
