from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class RegisterPage(BasePage):
    # form elements

    MALE_RADIO_BUTTON = (By.ID, "gender-male")
    FEMALE_RADIO_BUTTON = (By.ID, "gender-female")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    DAY_DROPDOWAN = (By.NAME, "DateOfBirthDay")
    MONTH_DROPDOWN = (By.NAME, "DateOfBirthMonth")
    YEAR_DROPDOWN = (By.NAME, "DateOfBirthYear")
    EMAIL = (By.ID, "Email")
    COMPANY = (By.ID, "Company")
    NEWSLETTER_CHECKBOX = (By.ID, "Newsletter")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")

    # form error elements

    FIRST_NAME_ERROR = (By.ID, "FirstName-error")
    LAST_NAME_ERROR = (By.ID, "LastName-error")
    EMAIL_ERROR = (By.ID, "Email-error")
    PASSWORD_ERROR = (By.ID, "Password-error")
    CONFORM_PASSWORD_ERROR = (By.ID, "ConfirmPassword-error")

    REGISTER_BUTTON = (By.ID, "register-button")
    REGISTER_MESSAGE = (By.CLASS_NAME, "master-wrapper-page")
    CONTINUE_BUTTON = (By.CLASS_NAME, "buttons")

    REGISTER_PAGE_URL = "https://demo.nopcommerce.com/register"

    def navigate_to_register_page(self):
        self.driver.get(self.REGISTER_PAGE_URL)

    def select_male_radio_button(self):
        self.click(self.MALE_RADIO_BUTTON)

    def select_female_radio_button(self):
        self.click(self.FEMALE_RADIO_BUTTON)

    def set_first_name(self, first_name):
        self.type(self.FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        self.type(self.LAST_NAME, last_name)

    def select_day_of_birth(self, day):
        self.select_dropdown_option_by_text(self.DAY_DROPDOWAN, day)

    def select_month_of_birth(self, month):
        self.select_dropdown_option_by_text(self.MONTH_DROPDOWN, month)

    def select_year_of_birth(self, year):
        self.select_dropdown_option_by_text(self.YEAR_DROPDOWN, year)

    def set_email(self, email):
        self.type(self.EMAIL, email)

    def set_company(self, name):
        self.type(self.COMPANY, name)

    def check_newsletter_checkbox(self):
        self.check_checkbox(self.NEWSLETTER_CHECKBOX)

    def uncheck_newsletter_checkbox(self):
        self.uncheck_checkbox(self.NEWSLETTER_CHECKBOX)

    def set_password(self, password):
        self.type(self.PASSWORD, password)

    def set_confirm_password(self, confirm_password):
        self.type(self.CONFIRM_PASSWORD, confirm_password)

    def click_on_register_button(self):
        self.click(self.REGISTER_BUTTON)

    def is_first_name_error_displayed(self):
        assert self.is_element_displayed(self.FIRST_NAME_ERROR)
        return self.is_element_displayed(self.FIRST_NAME_ERROR)

    def is_last_name_error_displayed(self):
        assert self.is_element_displayed(self.LAST_NAME_ERROR)
        return self.is_element_displayed(self.LAST_NAME_ERROR)

    def is_email_error_displayed(self):
        assert self.is_element_displayed(self.EMAIL_ERROR)
        return self.is_element_displayed(self.EMAIL_ERROR)

    def is_password_error_displayed(self):
        assert self.is_element_displayed(self.PASSWORD_ERROR)
        return self.is_element_displayed(self.PASSWORD_ERROR)

    def is_password_confirm_error_displayed(self):
        assert self.is_element_displayed(self.CONFORM_PASSWORD_ERROR)
        return self.is_element_displayed(self.CONFORM_PASSWORD_ERROR)

    def is_register_success_message_displayed(self):
        assert self.is_element_displayed(self.REGISTER_MESSAGE)
        return self.is_element_displayed(self.REGISTER_MESSAGE)

    def is_continue_button_displayed(self):
        assert self.is_element_displayed(self.CONTINUE_BUTTON)
        return self.is_element_displayed(self.CONTINUE_BUTTON)

    def get_register_success_message_text(self):
        self.wait_for_element_to_be_present(self.REGISTER_MESSAGE, 3)
        return self.get_element_text(self.REGISTER_MESSAGE)

    def get_email_error_text(self):
        return self.get_element_text(self.EMAIL_ERROR)

