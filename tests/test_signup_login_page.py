import pytest
from ..pages.signup_login_page import LoginSignup
from ..settings import settings_for_project


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup_page
class TestSignupPage:

    def test_get_reg_page(self, browser):
        page = LoginSignup(browser, settings_for_project.REG_URL)
        page.open()

    def test_register(self, browser):
        self.link_to_cabinet = browser.current_url
        page = LoginSignup(browser, self.link_to_cabinet)
        page.user_email_action()
        page.userpass_action()
        page.userpass2_action()
        page.firstname_action()
        page.lastname_action()
        page.phone_action()
        page.region_action()
        page.city_action()
        page.postcode_action()
        page.address_action()
        page.subscribe_choice_action()
        page.submit_action()
        page.is_elem_register_passed()
        page.logout_action()


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login_page
class TestLoginPage:

    def test_get_reg_page(self, browser):
        page = LoginSignup(browser, settings_for_project.REG_URL)
        page.open()

    def test_login(self, browser):
        self.link_to_cabinet = browser.current_url
        page = LoginSignup(browser, self.link_to_cabinet)
        page.login_test()
        page.logout_action()

