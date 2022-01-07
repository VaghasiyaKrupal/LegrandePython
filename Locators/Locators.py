from datetime import date
from openpyxl import load_workbook

FilePath = "C:/Users/Administrator/PycharmProject/LegrandePython/TestData/Data.xlsx"
datafile = load_workbook(FilePath)
testData = datafile['Test Data']

today = date.today()
currentDate = today.strftime("%m/%d/%Y")

class Locators:
    # Login Locators
    Email = "email"
    Password = "password"
    button_SignIn = "[type='submit']"
    forgotPasswordLink = 'Forgot Your Password?'
    forgotPasswordTextbox = '//div[@role="dialog"]//*[@name="email"]'
    PatientForgotPasswordLink = '//*[text()="Forgot your password?"]'
    PatientForgotPasswordButton = '//*[text()="Send Reset Email"]'

    # Hub Portal Locator
    productList = "Product List"
    updateButton = '//*[text()="Update"]'
    changePriceButton = '//*[text()="Change Item Price"]'
    confirmApprovalButton = '//*[text()="Confirm Approval"]'
    transferOrderButton = '//*[text()="Transfer Order"]'
    yesButton = '//*[text()="Yes"]'
    editButton = '(//*[text()="Edit"])[4]'
    patientSearch = '[placeholder="Search by Order Number, Patient Name, or DOB (mm/dd/yyyy)"]'
    firstOrder = '[data-expanded="false"]'
    addNoteButton = '//*[text()="Add Note"]'
    completeValue = '//*[@aria-label="Complete"]'
    sendOutOfNetwork = '//*[@aria-label="Send out of Network"]'
    cancelValue = '//*[@aria-label="Cancel"]'
    selectActionDropdown = '//div[@class="sc-eTpRJs ihfShO"]//*[@class="Select-arrow"]'

    # STD Pharma Locators
    approveButton = '//*[text()="Approve"]'
    verifyOrderDate = "(//tr[@class='table-row'])[1]//td[2][text()='" + currentDate + "']"
    verifyPatientName = "(//tr[@class='table-row'])[1]//td[3][text()='" + testData.cell(2, 1).value + "']"
    processPaymentButton = '//button[text()="Process Payment"]'
    createPostageLabelButton = '//div[@class="modal-footer"]//button[text()="Create Postage Label"]'
    createLabelButton = '//div[@class="modal-footer"]//button[text()="Create Label"]'
    printLabelButton = '//div[@class="modal-footer"]//a[text()="Print Postage Label"]'


    # Mailinator Locator
    malinatorLink = 'https://www.mailinator.com/'
    goButtonLink = '//*[text()="GO"]'
    searchBoxID = 'search'
    emailInbox = '//td[contains(text(),"Welcome to Legrande Health!")]'
    emailIframe = '//iframe[@id="html_msg_body"]'
    completeAccount = '//a[@class="complete-link"]'
