import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.signup_login_page import LoginSignup
from ..settings import settings_for_project

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def test_get_order_page(self, browser):
        page = BasePage(browser, settings_for_project.PROD_SERVER)
        page.open()

    def test_order(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.order_test()


