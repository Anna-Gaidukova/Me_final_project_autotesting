import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
import random
from ..settings import settings_for_project

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method_email(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@gmail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, settings_for_project.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_top_banner_seen()
        page.is_payment_delivery_btn_seen()
        page.is_goods_compare_btn_seen()
        page.is_bookmarks_btn_seen()
        page.is_private_account_seen()
        page.is_login_link_seen()
        page.is_signup_link_seen()
        page.is_logo_seen()
        page.is_phone_seen()
        page.is_cart_seen()
        page.is_search_seen()
        page.is_btn_where_search_seen()
        page.is_sub_choice_everywhere_search_seen()
        page.is_about_us_tab_seen()
        page.is_bonus_program_tag_seen()
        page.is_specials_tab_seen()
        page.is_payment_delivery_tab_seen()
        page.is_warranty_tab_seen()
        page.is_blog_tag_seen()

    def test_main_page_main_body(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_main_slider_seen()
        page.is_category_seen()
        page.is_sub_cat_children_books_seen()
        page.is_info_block_recommended_seen()
        page.is_info_block_new_seen()
        page.is_info_block_reduced_price_seen()
        page.is_info_block_hits_seen()
        page.is_info_block_reviews_seen()
        page.is_block_children_books_seen()
        page.is_block_educational_lit_seen()
        page.is_block_fiction_seen()
        page.is_block_religious_lit_seen()
        page.is_producers_block_seen()
        page.is_sub_block_prod1_seen()
        page.is_sub_block_prod7_seen()

    def test_main_page_subscribe_action(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_subscribe_text_seen()
        page.subscribe_action(self.email_for_subscribe)
        page.is_alert_success_after_sbscr()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.information_seen()
        page.support_service_seen()
        page.additional_seen()
        page.is_private_acc_footer_seen()
        page.is_conntacts_seen()





