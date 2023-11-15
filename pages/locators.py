from selenium.webdriver.common.by import By


class BasePageLocators:
    TOP_BANNER = (By.XPATH, "//div[contains(@class, 'exponea-banner')]")
    PAYMENT_DELIVERY_BTN = (By.CSS_SELECTOR, "button[onclick*='/oplata-dostavka/']")
    GOODS_COMPARE_BTN = (By.XPATH, "//span[text()='Порівняння товарів (0)']")
    BOOKMARKS_BTN = (By.XPATH, "//span[text()='Закладки (0)']")
    PRIVATE_ACCOUNT = (By.XPATH, "//span[text()='Особистий кабінет']")
    LOGIN_LINK = (By.XPATH, "//a[@id='login-popup']")
    SIGNUP_LINK = (By.XPATH, "//a[@href='https://bookks.com.ua/simpleregister/']")
    LOGO = (By.XPATH, "//div[@id='logo']")
    PHONE = (By.XPATH, "//div[@class = 'phone-box col-xs-12 col-sm-12 col-md-3  text-xs-center text-sm-center text-md-center']//div[contains(text(), '+38')]")
    CART = (By.XPATH, "//div[contains(@class, 'box-cart')]/descendant::div[@id='cart']/button")
    SEARCH = (By.XPATH, '//div[@id="searchtop"]')
    #GOODS_SEARCH_INPUT = (By.XPATH, )
    WHERE_SEARCH = (By.XPATH, "//div[@id='searchtop']//button[@id='change_category']/span[@class='category-name']")
    SUB_CHOICE_EVERYWHERE_SEARCH = (By.XPATH, "//div[@id='searchtop']//button[@id='change_category']/following-sibling::ul//a[text()='Всюди']")
    ABOUT_US_BTN = (By.XPATH, '//a[@class="no-img-parent-link" and contains(@href, "/about_us")]')
    BONUS_PROGRAM = (By.XPATH, '//a[@class="no-img-parent-link" and contains(@href, "/bonusna-programma")]')
    SPECIALS = (By.XPATH, '//a[@class="no-img-parent-link" and contains(@href, "/specials/")]')
    PAYMENT_DELIVERY = (By.XPATH, '//a[@class="no-img-parent-link" and contains(@href, "/oplata-dostavka")]')
    WARRANTY = (By.XPATH, '//a[@class="no-img-parent-link" and contains(@href, "/garantіi/")]')
    BLOG = (By.XPATH, '//a[@class="no-img-parent-link" and contains(@href, "/blogs/")]')

#Footer
    SUBSCRIBE_TEXT = (By.XPATH, '//span[text()="Підписатись на розсилку"]')
    NEWSLETTER_INPUT = (By.XPATH, '//input[@id="input-newsletter"]')
    SUBSCRIBE_BTN = (By.XPATH, '//button[@id="subcribe"]')
    ERROR_MSG = (By.XPATH, "//span[@id='error-msg']/b[@style='color:green']")

    INFORMATION = (By.XPATH, "//h3[contains(., 'Інформація')]")
    ABOUT_SHOP = (By.XPATH, '//a[@href="https://bookks.com.ua/about_us"]')
    OPLATA_DOSTAVKA = (By.XPATH, '//a[@href="https://bookks.com.ua/oplata-dostavka"]')
    PUBLIC_OFFER = (By.XPATH, '//a[@href="https://bookks.com.ua/dogovir"]')
    GOODS_RETURN = (By.XPATH, '//a[@href="https://bookks.com.ua/povernennya-tovaru"]')

    SUPPORT_SERVICE = (By.XPATH, "//h3[contains(., 'Служба підтримки')]")
    CONNTACT_US = (By.XPATH, '//a[@href="https://bookks.com.ua/contact-us/"]')
    SITEMAP = (By.XPATH, '//a[@href="https://bookks.com.ua/sitemap/"]')

    ADDITIONAL = (By.XPATH, "//h3[contains(., 'Додатково')]")
    BRANDS = (By.XPATH, '//a[@href="https://bookks.com.ua/brands/"]')
    VOUCHERS = (By.XPATH, '//a[@href="https://bookks.com.ua/vouchers/"]')
    PARTNERS = (By.XPATH, '//a[@href="https://bookks.com.ua/affiliates/"]')
    SALES_GOODS = (By.XPATH, '//a[@href="https://bookks.com.ua/specials/"]')

    PRIVATE_ACCOUNT_FOOTER = (By.XPATH, "//h3[contains(., 'Особистий кабінет')]")
    MY_ACCOUNT = (By.XPATH, '//a[@href="https://bookks.com.ua/my-account/"]')
    ORDER_HISTORY = (By.XPATH, '//a[@href="https://bookks.com.ua/order-history/"]')
    WISHLIST_FOOTER = (By.XPATH, "//a[text()='Закладки']")
    NEWSLETTER_FOOTER = (By.XPATH, '//a[@href="https://bookks.com.ua/newsletter/"]')
    SAFE_PAYMENTS = (By.XPATH, "//h3[text()='Безпечні платежі']")
    CONNTACTS = (By.XPATH, "//h3[text()='Контакти']")


class MainPageLocators:
    MAIN_SLIDER = (By.XPATH, "//div[@class='item']/a/img")
    CATEGORY = (By.XPATH, "//header[@class='pad-top']/div[@class='container'][2]//a[@href='detskie-knigi']")
    SUB_CAT_CHILDREN_BOOKS = (By.XPATH, "//header[@class='pad-top']/div[@class='container'][2]//li[@class='dropdown menu-open']//div[@class='dropdown-inner']/ul/li[7]")
    INFO_BLOCK_RECOMMENDED = (By.XPATH, "//div[@class='title-module']/span[text()='Рекомендовані']")
    INFO_BLOCK_NEW = (By.XPATH, "//div[@class='title-module']/span[text()='Новинка']")
    INFO_BLOCK_REDUCED_PRICE = (By.XPATH, "//div[@class='title-module']/span[text()='Товари зі знижкою']")
    INFO_BLOCK_HITS = (By.XPATH, "//div[@class='title-module']/span[text()='Хіти продажів']")
    INFO_BLOCK_REVIEWS = (By.XPATH, "//div[@class='title-module']/span[text()='Відгуки покупців']")

    BLOCK_CHILDREN_BOOKS = (By.XPATH, "//div[@class='display-table-cell']/a[text()='ДИТЯЧІ КНИГИ']")
    BLOCK_EDUCATIONAL_LIT = (By.XPATH, "//div[@class='display-table-cell']/a[@href='https://bookks.com.ua/uchebnaya-literatura/']")
    BLOCK_FICTION = (By.XPATH, "//div[@class='display-table-cell']/a[@href='https://bookks.com.ua/hudozhestvennaya-literatura/']")
    BLOCK_RELIGIOUS_LIT = (By.XPATH, "//div[@class='display-table-cell']/a[@href='https://bookks.com.ua/religioznaya-literatura/']")

    PRODUCERS_BLOCK = (By.XPATH, "//div[@class='title-module']/span[text()='Виробники']")
    SUB_BlOCK_PROD1 = (By.XPATH, "//div[@class='display-table']/div[@class='display-table-cell'][text()='Школа Харків']")
    SUB_BlOCK_PROD7 = (By.XPATH, "//div[@class='display-table']/div[@class='display-table-cell'][text()='А-БА-БА-ГА-ЛА-МА-ГА']")


class SignupLoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@id='register_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='register_password']")
    PASSWORD2_INPUT = (By.XPATH, "//input[@id='register_confirm_password']")
    FIRSTNAME_INPUT = (By.XPATH, "//input[@id='register_firstname']")
    LASTNAME_INPUT = (By.XPATH, "//input[@id='register_lastname']")
    PHONE_INPUT = (By.XPATH, "//input[@id='register_telephone']")
    REGION_CLICK = (By.XPATH, "//select[@id='register_zone_id']")
    REGION_CHOICE = (By.XPATH, "//option[@value='3490']")
    CITY_INPUT = (By.XPATH, "//input[@id='register_city']")
    POSTCODE_INPUT = (By.XPATH, "//input[@id='register_postcode']")
    ADDRESS_INPUT = (By.XPATH, "//input[@id='register_address_1']")
    SUBSCRIBE_CHOICE = (By.XPATH, "//label[text()='Ні']")
    REGISTER_ACTION = (By.XPATH, "//a[@id='simpleregister_button_confirm']")
    REGISTER_PASSED = (By.XPATH, "//h1[text()='Обліковий запис створений']")
    EXIT_PASSED = (By.XPATH, "//h1[text()='Вихід']")
    LOGIN_PASSED = (By.XPATH, "//h2[text()='Обліковий запис']")
    LOGOUT_URL = (By.XPATH, "//column[@id='column-right']//a[@href='https://bookks.com.ua/logout/']")

    LOGIN_URL = (By.XPATH, "//a[@href ='https://bookks.com.ua/login/']")
    LOGIN_INPUT_EMAIL = (By.XPATH, "//input[@id='input-email']")
    LOGIN_INPUT_PASSWORD = (By.XPATH, "//input[@id='input-password']")
    LOGIN_ACTION = (By.XPATH, "//input[@value='Вхід']")


class OrderPageLocators:
    ORDER_CHOICE1 = (By.XPATH, "//div[@class='cart']//button[contains(@onclick, '100 казок 1-й том Абабагаламага')]")
    ORDER_CHOICE2 = (By.XPATH, "//button[@id='button-cart']")
    ORDER2_PLUS = (By.XPATH, "//input[@id='input-quantity']")
    ORDER_NEXT = (By.XPATH, "//button[text()='Продовжити покупки']")
    ORDER2_PAGE = (By.XPATH, "//div[@class='caption']//a[@href='https://bookks.com.ua/hudozhestvennaya-literatura/brama-ievropy']")
    ORDER_ACTION = (By.XPATH, "//a[text()='Оформлення замовлення']")
    ORDER_AUTH = (By.XPATH, "//a[text()='Я зареєстрований']")
    AUTH_EMAIL = (By.XPATH, "//input[@name='email']")
    AUTH_PASSWORD = (By.XPATH, "//input[@name='password']")
    AUTH_ACTION = (By.XPATH, "//a[@id='simplecheckout_button_login']")
    ORDER_FINAL = (By.XPATH, "//div[@class='simplecheckout-button-right']//input[@id='button-confirm']")


class CabinetPageLocators:
    EMAIL_POPUP = (By.XPATH, "//input[@id='input-email-popup']")
    PASSWORD_POPUP = (By.XPATH, "//input[@id='input-password-popup']")
    LOGIN_POPUP = (By.XPATH, "//input[@value='Вхід']")
    CABLOGIN_TEXT = (By.XPATH, "//b[text()='Тест Тест']")
    CABLOGIN_ENTER = (By.XPATH, "//div[@class='btn-group box-account open']//a[@href='https://bookks.com.ua/my-account/']")


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass




