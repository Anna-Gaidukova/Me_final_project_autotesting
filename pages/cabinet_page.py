from ..pages import base_page, locators
from ..settings import settings_for_project
import inspect


class Cabinet(base_page.BasePage):

    def login_cabinet_test(self):
        assert self.click_element(*locators.BasePageLocators.PRIVATE_ACCOUNT), \
            "The element is not inserted"
        assert self.click_element(*locators.BasePageLocators.LOGIN_LINK), \
            "The element is not inserted"
        emaillogin = settings_for_project.TEST_EMAIL
        assert self.input_data(*locators.CabinetPageLocators.EMAIL_POPUP, emaillogin), \
            "The element is not inserted"
        passlogin = settings_for_project.PASS_LOGIN
        assert self.input_data(*locators.CabinetPageLocators.PASSWORD_POPUP, passlogin), \
            "The element is not inserted"
        assert self.click_element(*locators.CabinetPageLocators.LOGIN_POPUP), \
            "The element is not inserted"
        assert self.is_element_present(*locators.CabinetPageLocators.CABLOGIN_TEXT), \
            "The element exit passed is not present"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def open_menu_cabinet_test(self):
        assert self.click_element(*locators.CabinetPageLocators.CABLOGIN_TEXT), \
            "The element is not inserted"
        assert self.click_element(*locators.CabinetPageLocators.CABLOGIN_ENTER), \
            "The element is not inserted"
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN_PASSED), \
            "The element exit passed is not present"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - OK")


