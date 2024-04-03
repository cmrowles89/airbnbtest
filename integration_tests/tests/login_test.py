import pytest

from integration_tests.pages.login_page import LoginPage


class TestLogin():

    @pytest.fixture
    def login(self, driver):
        return LoginPage(driver)

    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert(login.success_message_present())

    def test_invalid_credentials(self, login):
        login.with_("tomsmith", "bad password")
        assert(login.failure_message_present())        