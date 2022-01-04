import time
from Locators.Locators import Locators


class LoginScreen:
    def __init__(self, driver):
        self.driver = driver

    def SetUsername(self, username):
        self.driver.find_element_by_name(Locators.Email).clear()
        self.driver.find_element_by_name(Locators.Email).send_keys(username)

    def SetPassword(self, password):
        self.driver.find_element_by_name(Locators.Password).clear()
        self.driver.find_element_by_name(Locators.Password).send_keys(password)

    def SignIn(self):
        self.driver.find_element_by_css_selector(Locators.button_SignIn).click()

    def ForgotPassword(self, userEmail):
        self.driver.find_element_by_link_text(Locators.forgotPasswordLink).click()
        self.driver.find_element_by_xpath(Locators.forgotPasswordTextbox).clear()
        self.driver.find_element_by_xpath(Locators.forgotPasswordTextbox).send_keys(userEmail)

    def PatientForgotPassword(self, PatientEmail):
        self.driver.find_element_by_xpath(Locators.PatientForgotPasswordLink).click()
        time.sleep(2)
        email = self.driver.find_element_by_name(Locators.Email)
        email.clear()
        email.send_keys(PatientEmail)

    def SendResetEmail(self):
        self.driver.find_element_by_xpath(Locators.PatientForgotPasswordButton).click()

    def SubmitButton(self):
        self.driver.find_element_by_xpath(Locators.submitButton).click()

    def ClearAndEnterText(self):
        self.driver.find_element_by_xpath()