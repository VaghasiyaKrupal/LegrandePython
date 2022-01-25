class Locators:
    # Login Locators
    Email = "email"
    Password = "password"
    button_SignIn = "[type='submit']"
    forgotPasswordLink = 'Forgot Your Password?'
    forgotPasswordTextbox = '//div[@role="dialog"]//*[@name="email"]'
    PatientForgotPasswordLink = '//*[text()="Forgot your password?"]'
    PatientForgotPasswordButton = '//*[text()="Send Reset Email"]'
    termsCheckbox = '//div[@class="modal-dialog"]//*[@class="checkbox checkbox-success"]'

    # Mailinator Locator
    malinatorLink = 'https://www.mailinator.com/'
    goButtonLink = '//*[text()="GO"]'
    searchBoxID = 'search'
    emailInbox = '//td[contains(text(),"Welcome to Legrande Health!")]'
    emailIframe = '//iframe[@id="html_msg_body"]'
    completeAccount = '//a[@class="complete-link"]'
