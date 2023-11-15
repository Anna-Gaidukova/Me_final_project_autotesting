from ..pages import base_page, locators
from ..settings import settings_for_project
import inspect


class OrderPage(base_page.BasePage):

    def order_test(self):
        assert self.click_element(*locators.OrderPageLocators.ORDER_CHOICE1), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.OrderPageLocators.ORDER_NEXT), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.OrderPageLocators.ORDER2_PAGE), \
            "The element is not inserted"
        assert self.clear_field(*locators.OrderPageLocators.ORDER2_PLUS), \
            "The element is not inserted"
        plus = "2"
        assert self.input_data(*locators.OrderPageLocators.ORDER2_PLUS, plus), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.OrderPageLocators.ORDER_CHOICE2), \
            "The element is not inserted"
        assert self.click_element(*locators.OrderPageLocators.ORDER_ACTION), \
            "The element is not inserted"
        assert self.click_element(*locators.OrderPageLocators.ORDER_AUTH), \
            "The element is not inserted"
        emaillogin = settings_for_project.TEST_EMAIL
        assert self.input_data(*locators.OrderPageLocators.AUTH_EMAIL, emaillogin), \
            "The element is not inserted"
        passlogin = settings_for_project.PASS_LOGIN
        assert self.input_data(*locators.OrderPageLocators.AUTH_PASSWORD, passlogin), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.OrderPageLocators.AUTH_ACTION), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.OrderPageLocators.ORDER_FINAL), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

