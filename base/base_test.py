import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.meet_page import MeetPage
from pages.connect_to_meeting_page import ConnectToMeetingPage


class BaseTest:

    # Аннотация типов
    data: Data
    login_page: LoginPage
    meet_page: MeetPage
    connect_to_meeting_page: ConnectToMeetingPage

    @pytest.fixture(autouse=True)
    def user(self, request, driver_1):

        request.cls.driver = driver_1
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver_1)
        request.cls.meet_page = MeetPage(driver_1)
        request.cls.connect_to_meeting_page = ConnectToMeetingPage(driver_1)