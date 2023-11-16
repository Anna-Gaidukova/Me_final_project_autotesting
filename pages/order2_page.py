from ..pages import base_page, locators
from ..settings import settings_for_project
import inspect


class Order2Page(base_page.BasePage):

    def is_sub_cat_children_books_seen(self):
        assert self.click_element(*locators.MainPageLocators.CATEGORY_CHILDREN_BOOKS), \
            "The element is not present"
        self.explicit_wait(2)
        assert self.click_element(*locators.MainPageLocators.SUB_CAT_CHILDREN_BOOKS2), \
            "The element is not present"
        self.explicit_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def add_to_cart_first_product(self):
        #assert self.hover_action(*locators.Order2PageLocators.ORDER_CHOICE1), \
            #"The element is not present"
        #self.explicit_wait(5)
        assert self.click_element(*locators.Order2PageLocators.ORDER_CHOICE1), \
            "The element is not present or intractable"
        self.explicit_wait(5)
        price = self.get_text(*locators.Order2PageLocators.PRICE_FIRST_PRODUCT)
        price = float(price.replace(' грн.', '')) # 250
        print(price)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        if price:
            return price

    def press_btn_continue_shop_popup(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER_NEXT), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_second_product(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER2_PAGE), \
            "The element currency is not present or intractable"
        self.explicit_wait(2)
        price = self.get_text(*locators.Order2PageLocators.PRICE_SECOND_PRODUCT)
        print(price)
        price = float(price.replace(' грн.', ''))*2
        print(price)
        assert self.clear_field(*locators.Order2PageLocators.ORDER2_PLUS), \
            "The element currency is not present"
        assert self.input_data(*locators.Order2PageLocators.ORDER2_PLUS, 2), \
            "The element currency is not present"
        assert self.click_element(*locators.Order2PageLocators.ORDER_CHOICE2), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        if price:
            return price

    def press_btn_checkout_shop_popup(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER_ACTION), \
            "The element currency is not present or intractable"
        self.explicit_wait(3)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def check_total_price_qty(self, price1, price2):
        total_price = self.get_text(*locators.Order2PageLocators.TOTAL_PRICE)
        self.explicit_wait(2)
        total_price = float(total_price.replace(' грн.', ''))
        print(f"total_prise int: {total_price}")
        total_actual = price1+price2
        print(f"total_actual int: {total_actual}")
        assert total_actual == total_price, \
            "Total price doesn't match to actual"
        #qty_actual = int(self.get_text(*locators.Order2PageLocators.QTY))
        #assert qty_actual == qty, \
         #   "QTY doesn't match to actual"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def auth_action_test(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER_AUTH), \
            "The element is not inserted"
        email_login = settings_for_project.TEST_EMAIL
        assert self.input_data(*locators.Order2PageLocators.AUTH_EMAIL, email_login), \
            "The element is not inserted"
        pass_login = settings_for_project.PASSWORD
        assert self.input_data(*locators.Order2PageLocators.AUTH_PASSWORD, pass_login), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.Order2PageLocators.AUTH_ACTION), \
            "The element is not inserted"
        self.explicit_wait(10)

    def final_action_test(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER_FINAL), \
            "The element is not inserted"
        self.explicit_wait(10)
        print(f"{inspect.currentframe().f_code.co_name} - OK")



