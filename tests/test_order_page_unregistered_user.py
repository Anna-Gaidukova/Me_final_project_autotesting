import pytest
from ..pages.base_page import BasePage
from ..pages.order_page_unregistered_user import OrderPage
from ..pages.cabinet_page import Cabinet
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
        page.order_choice1()
        page.order_next()
        page.order_choice2_page()
        page.order_choice2_plus()
        page.order_choice2_to_cart()
        page.order_action()
        page.firstname_action()
        page.lastname_action()
        page.phone_action()
        page.region_action()
        page.city_action()
        page.address_action()
        page.order_final_action()


