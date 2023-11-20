from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_top_banner_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.TOP_BANNER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_payment_delivery_btn_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.PAYMENT_DELIVERY_BTN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_goods_compare_btn_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.GOODS_COMPARE_BTN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_bookmarks_btn_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.BOOKMARKS_BTN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_private_account_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.PRIVATE_ACCOUNT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_link_seen(self):
        assert self.click_element(*locators.BasePageLocators.PRIVATE_ACCOUNT), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_LINK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_signup_link_seen(self):
        assert self.click_element(*locators.BasePageLocators.PRIVATE_ACCOUNT), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.SIGNUP_LINK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_logo_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_phone_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_cart_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_search_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_btn_where_search_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.WHERE_SEARCH), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_sub_choice_everywhere_search_seen(self):
        assert self.click_element(*locators.BasePageLocators.WHERE_SEARCH), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.SUB_CHOICE_EVERYWHERE_SEARCH), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_about_us_tab_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.ABOUT_US_BTN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_bonus_program_tag_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.BONUS_PROGRAM), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_specials_tab_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.SPECIALS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_payment_delivery_tab_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.PAYMENT_DELIVERY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_warranty_tab_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_blog_tag_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.BLOG), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

#Main_body
    def is_main_slider_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_SLIDER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_category_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.CATEGORY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_sub_cat_children_books_seen(self):
        assert self.hover_action(*locators.MainPageLocators.CATEGORY_CHILDREN_BOOKS), \
            "The element is not present"
        assert self.click_element(*locators.MainPageLocators.CATEGORY), \
            "The element is not present"
        self.explicit_wait(2)
        assert self.hover_action(*locators.MainPageLocators.CATEGORY_CHILDREN_BOOKS), \
            "The element is not present"
        self.explicit_wait(5)
        assert self.is_element_present(*locators.MainPageLocators.SUB_CAT_CHILDREN_BOOKS), \
            "The element is not present"
        self.click_element(*locators.MainPageLocators.CATEGORY)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_recommended_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_RECOMMENDED), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_new_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_NEW), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_reduced_price_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_REDUCED_PRICE), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_hits_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_reviews_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_REVIEWS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_block_children_books_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.BLOCK_CHILDREN_BOOKS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_block_educational_lit_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.BLOCK_EDUCATIONAL_LIT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_block_fiction_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.BLOCK_FICTION), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_block_religious_lit_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.BLOCK_RELIGIOUS_LIT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_producers_block_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.PRODUCERS_BLOCK), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_sub_block_prod1_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.SUB_BlOCK_PROD1), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_sub_block_prod7_seen(self):
        assert self.is_element_present(*locators.MainPageLocators.SUB_BlOCK_PROD7), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

#Footer
    def is_subscribe_text_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE_TEXT), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def subscribe_action(self, email):
        assert self.input_data(*locators.BasePageLocators.NEWSLETTER_INPUT, email), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBE_BTN), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_alert_success_after_sbscr(self):
        assert self.is_element_appeared_after_while(*locators.BasePageLocators.ERROR_MSG, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def information_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.INFORMATION), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def support_service_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.SUPPORT_SERVICE), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def additional_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.ADDITIONAL), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_private_acc_footer_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.PRIVATE_ACCOUNT_FOOTER), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_contacts_seen(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")








