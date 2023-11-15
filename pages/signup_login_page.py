from ..pages import base_page, locators
from ..settings import settings_for_project
import inspect
import random


class LoginSignup(base_page.BasePage):

    def user_email_action(self):
        hash_email = "%032x" % random.getrandbits(128)
        self.email_for_register = f"{hash_email}@mail.com"
        assert self.input_data(*locators.SignupLoginPageLocators.EMAIL_INPUT, self.email_for_register), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def userpass_action(self):
        password = settings_for_project.PASSWORD
        assert self.input_data(*locators.SignupLoginPageLocators.PASSWORD_INPUT, password), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def userpass2_action(self):
        password2 = settings_for_project.PASSWORD
        assert self.input_data(*locators.SignupLoginPageLocators.PASSWORD2_INPUT, password2), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def firstname_action(self):
        firstname = settings_for_project.FIRSTNAME
        assert self.input_data(*locators.SignupLoginPageLocators.FIRSTNAME_INPUT, firstname), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def lastname_action(self):
        lastname = settings_for_project.LASTNAME
        assert self.input_data(*locators.SignupLoginPageLocators.LASTNAME_INPUT, lastname), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def phone_action(self):
        phone = settings_for_project.PHONE
        assert self.input_data_phone(*locators.SignupLoginPageLocators.PHONE_INPUT, phone), \
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

    def city_action(self):
        city = settings_for_project.CITY
        assert self.input_data(*locators.SignupLoginPageLocators.CITY_INPUT, city), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def region_action(self):
        assert self.click_element(*locators.SignupLoginPageLocators.REGION_CLICK), \
            "The element is not inserted"
        assert self.click_element(*locators.SignupLoginPageLocators.REGION_CHOICE), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def postcode_action(self):
        postcode = settings_for_project.POSTCODE
        assert self.input_data(*locators.SignupLoginPageLocators.POSTCODE_INPUT, postcode), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def address_action(self):
        address = settings_for_project.ADDRESS
        assert self.input_data(*locators.SignupLoginPageLocators.ADDRESS_INPUT, address), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def subscribe_choice_action(self):
        assert self.click_element(*locators.SignupLoginPageLocators.SUBSCRIBE_CHOICE), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def submit_action(self):
        assert self.click_element(*locators.SignupLoginPageLocators.REGISTER_ACTION), \
            "The element is not inserted"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_register_passed(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.REGISTER_PASSED), \
            "The element register passed is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def logout_action(self):
        assert self.click_element(*locators.SignupLoginPageLocators.LOGOUT_URL), \
            "The element is not inserted"
        assert self.is_element_present(*locators.SignupLoginPageLocators.EXIT_PASSED), \
            "The element exit passed is not present"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def login_test(self):
        assert self.click_element(*locators.SignupLoginPageLocators.LOGIN_URL), \
            "The element is not inserted"
        emaillogin = settings_for_project.TEST_EMAIL
        assert self.input_data(*locators.SignupLoginPageLocators.LOGIN_INPUT_EMAIL, emaillogin), \
            "The element is not inserted"
        passlogin = settings_for_project.PASS_LOGIN
        assert self.input_data(*locators.SignupLoginPageLocators.LOGIN_INPUT_PASSWORD, passlogin), \
            "The element is not inserted"
        assert self.click_element(*locators.SignupLoginPageLocators.LOGIN_ACTION), \
            "The element is not inserted"
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN_PASSED), \
            "The element exit passed is not present"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")