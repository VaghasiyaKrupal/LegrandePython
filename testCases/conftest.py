import time
from datetime import date
from faker import Faker
from openpyxl import load_workbook
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginScreen
from pageObjects.BaseFile import CommanFlow
from webdriver_manager.chrome import ChromeDriverManager
from Locators.Locators import Locators
from Locators.PracticeLocators import PracticeLocators


faker = Faker()
today = date.today()
currentDate = today.strftime("%m/%d/%Y")
FirstName = faker.first_name()
LastName = faker.last_name()
PhoneNumber = faker.phone_number()
EmailAddress = FirstName + "." + LastName + "@mailinator.com"

FilePath = "C:/Users/Administrator/PycharmProject/LegrandePython/TestData/Data.xlsx"
datafile = load_workbook(FilePath)
testData = datafile['Test Data']
loginData = datafile["Login Credentials"]
scriptData = datafile['Script Data']


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    return driver


@pytest.fixture()
def MasterLogin(setup):
    driver = setup
    driver.get(loginData.cell(2, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.SetUsername(loginData.cell(2, 3).value)
    login.SetPassword(loginData.cell(2, 4).value)
    login.SignIn()
    driver.implicitly_wait(10)


@pytest.fixture()
def MasterForgotPassword(setup):
    driver = setup
    driver.get(loginData.cell(2, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.ForgotPassword(loginData.cell(2, 3).value)
    time.sleep(1)
    login.SubmitButton()


@pytest.fixture()
def PracticeLogin(setup):
    driver = setup
    driver.get(loginData.cell(3, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.SetUsername(loginData.cell(3, 3).value)
    login.SetPassword(loginData.cell(3, 4).value)
    login.SignIn()
    checkboxes = driver.find_elements(By.XPATH, '//div[@class="modal-dialog"]//*[@class="checkbox checkbox-success"]')
    if checkboxes:
        checkboxes[0].click()
        driver.find_element(By.XPATH, PracticeLocators.continueButton).click()


@pytest.fixture()
def PracticeForgotPassword(setup):
    driver = setup
    driver.get(loginData.cell(3, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.ForgotPassword(loginData.cell(3, 3).value)
    time.sleep(1)
    login.SubmitButton()


@pytest.fixture()
def HubLogin(setup):
    driver = setup
    driver.get(loginData.cell(4, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.SetUsername(loginData.cell(4, 3).value)
    login.SetPassword(loginData.cell(4, 4).value)
    login.SignIn()
    checkboxes = driver.find_elements(By.XPATH, '//div[@class="modal-dialog"]//*[@class="checkbox checkbox-success"]')
    if checkboxes:
        checkboxes[0].click()
        driver.find_element(By.XPATH, PracticeLocators.continueButton).click()


@pytest.fixture()
def HubForgotPassword(setup):
    driver = setup
    driver.get(loginData.cell(4, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.ForgotPassword(loginData.cell(4, 3).value)
    time.sleep(1)
    login.SubmitButton()


@pytest.fixture()
def RXPharmaLogin(setup):
    driver = setup
    driver.get(loginData.cell(5, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.SetUsername(loginData.cell(5, 3).value)
    login.SetPassword(loginData.cell(5, 4).value)
    login.SignIn()
    checkboxes = driver.find_elements(By.XPATH, '//div[@class="modal-dialog"]//*[@class="checkbox checkbox-success"]')
    if checkboxes:
        checkboxes[0].click()
        driver.find_element(By.XPATH, PracticeLocators.continueButton).click()


@pytest.fixture()
def RXPharmaForgotPassword(setup):
    driver = setup
    driver.get(loginData.cell(5, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.ForgotPassword(loginData.cell(5, 3).value)
    time.sleep(1)
    login.SubmitButton()


@pytest.fixture()
def OTCPharmaLogin(setup):
    driver = setup
    driver.get(loginData.cell(6, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.SetUsername(loginData.cell(6, 3).value)
    login.SetPassword(loginData.cell(6, 4).value)
    login.SignIn()
    checkboxes = driver.find_elements(By.XPATH, '//div[@class="modal-dialog"]//*[@class="checkbox checkbox-success"]')
    if checkboxes:
        checkboxes[0].click()
        driver.find_element(By.XPATH, PracticeLocators.continueButton).click()


@pytest.fixture()
def OTCPharmaForgotPassword(setup):
    driver = setup
    driver.get(loginData.cell(6, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.ForgotPassword(loginData.cell(6, 3).value)
    time.sleep(1)
    login.SubmitButton()


@pytest.fixture()
def CompoundPharmaLogin(setup):
    driver = setup
    driver.get(loginData.cell(7, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.SetUsername(loginData.cell(7, 3).value)
    login.SetPassword(loginData.cell(7, 4).value)
    login.SignIn()
    checkboxes = driver.find_elements(By.XPATH, '//div[@class="modal-dialog"]//*[@class="checkbox checkbox-success"]')
    if checkboxes:
        checkboxes[0].click()
        driver.find_element(By.XPATH, PracticeLocators.continueButton).click()


@pytest.fixture()
def CompoundPharmaForgotPassword(setup):
    driver = setup
    driver.get(loginData.cell(7, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.ForgotPassword(loginData.cell(7, 3).value)
    time.sleep(1)
    login.SubmitButton()


@pytest.fixture()
def PatientLogin(setup):
    driver = setup
    driver.get(loginData.cell(8, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.SetUsername(loginData.cell(8, 3).value)
    login.SetPassword(loginData.cell(8, 4).value)
    login.SignIn()
    time.sleep(3)


@pytest.fixture()
def PatientForgotPassword(setup):
    driver = setup
    driver.get(loginData.cell(8, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.PatientForgotPassword(loginData.cell(3, 3).value)
    time.sleep(1)
    login.SendResetEmail()


@pytest.fixture()
def UserLogin(setup):
    driver = setup
    driver.get(loginData.cell(9, 2).value)
    driver.implicitly_wait(5)
    login = LoginScreen(driver)
    login.SetUsername(loginData.cell(9, 3).value)
    login.SetPassword(loginData.cell(9, 4).value)
    login.SignIn()
    checkboxes = driver.find_elements(By.XPATH, '//div[@class="modal-dialog"]//*[@class="checkbox checkbox-success"]')
    if checkboxes:
        checkboxes[0].click()
        driver.find_element(By.XPATH, PracticeLocators.continueButton).click()


@pytest.fixture()
def CreatePatient(setup):
    driver = setup
    patient = CommanFlow(driver)
    patient.CreatePatient()


@pytest.fixture()
def CreateUser(setup):
    driver = setup
    user = CommanFlow(driver)
    user.CreateUser()


@pytest.fixture()
def PatientMainSearch(setup):
    driver = setup
    mainSearch = CommanFlow(driver)
    mainSearch.PatientMainSearch()


@pytest.fixture()
def ChangeProductPrice(setup):
    driver = setup
    product = CommanFlow(driver)
    product.ChangeProductPrice()


@pytest.fixture()
def OnetimeRXSkipPayment(setup):
    driver = setup
    onetimeRxSkipPayment = CommanFlow(driver)
    onetimeRxSkipPayment.OnetimeRXSkipPayment()


@pytest.fixture()
def OnetimeOTCSkipPayment(setup):
    driver = setup
    onetimeOTCSkipPayment = CommanFlow(driver)
    onetimeOTCSkipPayment.OnetimeOTCSkipPayment()


@pytest.fixture()
def OnetimeCompoundSkipPayment(setup):
    driver = setup
    onetimeCompoundSkipPayment = CommanFlow(driver)
    onetimeCompoundSkipPayment.OnetimeCompoundSkipPayment()


@pytest.fixture()
def SubscriptionRXSkipPayment(setup):
    driver = setup
    SubscriptionRXSkipPayment = CommanFlow(driver)
    SubscriptionRXSkipPayment.SubscriptionRXSkipPayment()


@pytest.fixture()
def SubscriptionOTCSkipPayment(setup):
    driver = setup
    SubscriptionOTCSkipPayment = CommanFlow(driver)
    SubscriptionOTCSkipPayment.SubscriptionOTCSkipPayment()


@pytest.fixture()
def SubscriptionCompoundSkipPayment(setup):
    driver = setup
    SubscriptionCompoundSkipPayment = CommanFlow(driver)
    SubscriptionCompoundSkipPayment.SubscriptionCompoundSkipPayment()


@pytest.fixture()
def OnetimeRXProvidePayment(setup):
    driver = setup
    OnetimeRXProvidePayment = CommanFlow(driver)
    OnetimeRXProvidePayment.OnetimeRXProvidePayment()


@pytest.fixture()
def OnetimeOTCProvidePayment(setup):
    driver = setup
    OnetimeOTCProvidePayment = CommanFlow(driver)
    OnetimeOTCProvidePayment.OnetimeOTCProvidePayment()


@pytest.fixture()
def OnetimeCompoundProvidePayment(setup):
    driver = setup
    OnetimeCompoundProvidePayment = CommanFlow(driver)
    OnetimeCompoundProvidePayment.OnetimeCompoundProvidePayment()


@pytest.fixture()
def SubscriptionRXProvidePayment(setup):
    driver = setup
    SubscriptionRXProvidePayment = CommanFlow(driver)
    SubscriptionRXProvidePayment.SubscriptionRXProvidePayment()


@pytest.fixture()
def SubscriptionOTCProvidePayment(setup):
    driver = setup
    SubscriptionOTCProvidePayment = CommanFlow(driver)
    SubscriptionOTCProvidePayment.SubscriptionOTCProvidePayment()


@pytest.fixture()
def SubscriptionCompoundProvidePayment(setup):
    driver = setup
    SubscriptionCompoundProvidePayment = CommanFlow(driver)
    SubscriptionCompoundProvidePayment.SubscriptionCompoundProvidePayment()


@pytest.fixture()
def EditOrder(setup):
    driver = setup
    editOrder = CommanFlow(driver)
    editOrder.EditOrder()
