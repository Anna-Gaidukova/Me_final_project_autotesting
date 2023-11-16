import pytest
from ..pages.base_page import BasePage
from ..pages.order2_page import Order2Page
from ..settings import settings_for_project

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order2_page
class TestOrder2Page:

    def test_get_order_page(self, browser):
        page = BasePage(browser, settings_for_project.PROD_SERVER)
        page.open()

    def test_order(self, browser):
        self.link_to_cabinet = browser.current_url
        page = Order2Page(browser, self.link_to_cabinet)
        page.is_sub_cat_children_books_seen()
        #page.add_to_cart_first_product()
        global price_1_product
        price_1_product = page.add_to_cart_first_product()
        page.press_btn_continue_shop_popup()
        #page.add_to_cart_second_product()
        global price_2_product
        price_2_product = page.add_to_cart_second_product()
        page.press_btn_checkout_shop_popup()
        page.check_total_price_qty(price_1_product, price_2_product)
        page.auth_action_test()
        page.final_action_test()
        #page.order_test()






