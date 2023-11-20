from ..pages import base_page, locators
from ..settings import settings_for_project
import inspect


class OrderPage(base_page.BasePage):

    def order_choice1(self):
        assert self.hover_action(*locators.OrderPageLocators.ORDER_CHOICE1), \
            "The element is not present"
        assert self.click_element(*locators.OrderPageLocators.ORDER_CHOICE1), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_next(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER_NEXT), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_choice2_page(self):
        assert self.click_element(*locators.OrderPageLocators.ORDER_PAGE2), \
            "The element is not inserted"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_choice2_plus(self):
        assert self.clear_field(*locators.Order2PageLocators.ORDER2_PLUS), \
            "The element is not inserted"
        plus = "2"
        assert self.input_data(*locators.Order2PageLocators.ORDER2_PLUS, plus), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_choice2_to_cart(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER_CHOICE2), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_action(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER_ACTION), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def firstname_action(self):
        firstname = settings_for_project.FIRSTNAME
        assert self.input_data(*locators.OrderPageLocators.FIRSTNAME_INPUT, firstname), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def lastname_action(self):
        lastname = settings_for_project.LASTNAME
        assert self.input_data(*locators.OrderPageLocators.LASTNAME_INPUT, lastname), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def phone_action(self):
        phone = settings_for_project.PHONE
        assert self.input_data_phone(*locators.OrderPageLocators.PHONE_INPUT, phone), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def input_data_phone(self, how, what, data):
        try:
            element = self.browser.find_element(how, what)
            self.browser.execute_script("arguments[0].value = arguments[1]", element, data)
        except Exception as e:
            print(f"An exception occurred: {e}")
            return False
        return True

    def region_action(self):
        assert self.click_element(*locators.OrderPageLocators.REGION_CLICK), \
            "The element is not inserted"
        assert self.click_element(*locators.SignupLoginPageLocators.REGION_CHOICE), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def city_action(self):
        city = settings_for_project.CITY
        assert self.input_data(*locators.OrderPageLocators.CITY_INPUT, city), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")


    def address_action(self):
        address = settings_for_project.ADDRESS
        assert self.input_data(*locators.OrderPageLocators.ADDRESS_INPUT, address), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_final_action(self):
        assert self.click_element(*locators.Order2PageLocators.ORDER_FINAL), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")


