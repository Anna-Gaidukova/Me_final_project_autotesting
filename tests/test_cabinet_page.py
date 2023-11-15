import pytest
from ..pages.base_page import BasePage
from ..pages.cabinet_page import Cabinet
from ..pages.signup_login_page import LoginSignup
from ..settings import settings_for_project

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cabinet_page
class TestCabinetPage:

    def test_get_cabinet_page(self, browser):
        page = BasePage(browser, settings_for_project.PROD_SERVER)
        page.open()

    def test_register(self, browser):
        self.link_to_cabinet = browser.current_url
        page = Cabinet(browser, self.link_to_cabinet)
        page.login_cabinet_test()
        page.open_menu_cabinet_test()

