from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.CLASS_NAME, "email")
    PASS_INPUT = (By.CLASS_NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    ERROR_MESSAGE_MAIN = (By.CSS_SELECTOR, "div.message-error")
    ERROR_MESSAGE_EMAIL = (By.ID, "Email-error")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Forgot password?']")

    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL) # suntem pe Login Page

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    # va seta o adresa de email neinregistrata folosind metoda set_email() de mai sus
    # se foloseste pentru pasul BDD fara parametri
    def set_unregistered_email(self):
        self.set_email("wrong_email@host.com")

    def set_password(self, password):
        self.type(self.PASS_INPUT, password)

    # va seta o parola folosind functia set_password() de mai sus
    # se foloseste pentru pasul BDD fara parametri
    def set_wrong_password(self):
        self.set_password("parolaoarecare")

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON) # click pe butonul de logare

    def click_forgot_password_link(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    def is_main_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE_MAIN)

    def get_main_error_message_text(self):
        return self.get_element_text(self.ERROR_MESSAGE_MAIN)

    def is_email_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE_EMAIL)

    def get_email_error_message_text(self):
        return self.get_element_text(self.ERROR_MESSAGE_EMAIL)

    # se foloseste pentru pasul BDD fara parametri
    def is_no_customer_account_found_message_displayed(self):
        return "No customer account found" in self.get_main_error_message_text()






