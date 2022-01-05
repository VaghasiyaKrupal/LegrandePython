import time
from openpyxl import load_workbook
from Locators.Locators import Locators

FilePath = "C:/Users/Administrator/PycharmProject/LegrandePython/TestData/Data.xlsx"
datafile = load_workbook(FilePath)
datasheet = datafile.get_sheet_by_name('Test Data')


class TestPractice:
    def test_ForgotPassword(self, setup, PracticeForgotPassword):
        self.driver = setup
        self.driver.close()

    def test_CreatePatient(self, setup, PracticeLogin, CreatePatient):
        self.driver = setup

    def test_onetimeTemplate(self, setup, PracticeLogin):
        self.driver = setup
        self.driver.find_element_by_link_text(Locators.orderTemplateScreen).click()
        self.driver.find_element_by_link_text(Locators.createTemplateButton).click()
        self.driver.find_element_by_xpath(Locators.selectOnetimeTemplate).click()
        self.driver.find_element_by_xpath(Locators.templateTitle).send_keys(datasheet.cell(2, 12).value)
        self.driver.find_element_by_xpath(Locators.continueButton).click()
        self.driver.find_element_by_xpath(Locators.templateProductSearch).click()
        self.driver.find_element_by_xpath("//*[text()='" + datasheet.cell(2, 6).value + "']").click()
        self.driver.find_element_by_xpath(Locators.AddButton).click()
        self.driver.find_element_by_xpath(Locators.ProductQuantity).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(Locators.Quantity).click()
        self.driver.find_element_by_xpath(Locators.ProductRefilles).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(Locators.Quantity).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.DAWCheckbox).click()
        time.sleep(2)
        instruction = self.driver.find_element_by_xpath(Locators.productInstruction)
        instruction.click()
        instruction.send_keys(datasheet.cell(2, 9).value)
        self.driver.find_element_by_xpath(Locators.templateNotes).send_keys(datasheet.cell(2, 11).value)
        self.driver.find_element_by_xpath(Locators.saveTemplateButton).click()
        self.driver.close()

    def test_subscriptionTemplate(self, setup, PracticeLogin):
        self.driver = setup
        self.driver.find_element_by_link_text(Locators.orderTemplateScreen).click()
        self.driver.find_element_by_link_text(Locators.createTemplateButton).click()
        self.driver.find_element_by_xpath(Locators.selectSubscriptionTemplate).click()
        self.driver.find_element_by_xpath(Locators.templateTitle).send_keys(datasheet.cell(2, 12).value)
        self.driver.find_element_by_xpath(Locators.continueButton).click()
        self.driver.find_element_by_xpath(Locators.templateProductSearch).click()
        self.driver.find_element_by_xpath("//*[text()='" + datasheet.cell(2, 6).value + "']").click()
        self.driver.find_element_by_xpath(Locators.addProductButton).click()
        self.driver.find_element_by_xpath(Locators.ProductQuantity).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(Locators.Quantity).click()
        self.driver.find_element_by_xpath(Locators.ProductRefilles).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(Locators.Quantity).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.DAWCheckbox).click()
        time.sleep(2)
        instruction = self.driver.find_element_by_xpath(Locators.productInstruction)
        instruction.click()
        instruction.send_keys(datasheet.cell(2, 9).value)
        self.driver.find_element_by_xpath(Locators.templateNotes).send_keys(datasheet.cell(2, 11).value)
        self.driver.find_element_by_xpath(Locators.saveTemplateButton).click()
        self.driver.close()

    def test_DropChart(self, setup, PracticeLogin):
        self.driver = setup
        self.driver.find_element_by_partial_link_text(Locators.documentsScreen).click()
        self.driver.find_element_by_xpath(Locators.newDocuments).click()
        self.driver.find_element_by_xpath(Locators.documentsDoctorSearchbox).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Locators.selectDoctor).click()
        self.driver.find_element_by_xpath(Locators.selectDocumentsSearchbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(Locators.documentsType).click()
        self.driver.find_element_by_xpath(Locators.documentTitle).send_keys('WL')
        self.driver.find_element_by_xpath(Locators.continueButton).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(Locators.uploadFile).send_keys(
            "C:/Users/Administrator/Downloads/Test Files/Welcome Letter.pdf")
        time.sleep(5)
        SubmitButton = self.driver.find_element_by_xpath(Locators.submitButton)
        if SubmitButton.is_enabled():
            SubmitButton.click()
        else:
            print("\n File not uploaded")
        self.driver.close()

    def test_createUser(self, setup, PracticeLogin, CreateUser):
        self.driver = setup

    def test_PatientMainSearch(self, setup, PracticeLogin, PatientMainSearch):
        self.driver = setup

    def test_CreatingRXOnetimeSkipPayment(self, setup, PracticeLogin, OnetimeRXSkipPayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Onetime RX with skip payment, created successfully')
        else:
            print("\nOrder: Onetime RX with skip payment, is not created")
        self.driver.close()

    def test_VerifyOrderDetailsScreen(self, setup,PracticeLogin):
        self.driver = setup
        self.driver.find_element_by_link_text('Orders').click()
        self.driver.find_element_by_xpath('//table/tbody/tr[1]/td[2]/a').click()
        assert 'Prescription & Order Details'

    def test_CreatingOTCOnetimeSkipPayment(self, setup, PracticeLogin, OnetimeOTCSkipPayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Onetime OTC with skip payment, created successfully')
        else:
            print("\nOrder: Onetime OTC with skip payment, is not created")
        self.driver.close()

    def test_CreatingCompoundOnetimeSkipPayment(self, setup, PracticeLogin, OnetimeCompoundSkipPayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Onetime Compound with skip payment, created successfully')
        else:
            print("\nOrder: Onetime Compound with skip payment, is not created")
        self.driver.close()

    def test_CreatingRXSubscriptionSkipPayment(self, setup, PracticeLogin, SubscriptionRXSkipPayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Subscription RX with Skip payment, created successfully')
        else:
            print("\nOrder: Subscription RX with Skip payment, is not created")
        self.driver.close()

    def test_CreatingOTCSubscriptionSkipPayment(self, setup, PracticeLogin, SubscriptionOTCSkipPayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Subscription OTC with Skip payment, created successfully')
        else:
            print("\nOrder: Subscription OTC with Skip payment, is not created")
        self.driver.close()

    def test_CreatingCompoundSubscriptionSkipPayment(self, setup, PracticeLogin, SubscriptionCompoundSkipPayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Subscription Compound with Skip payment, created successfully')
        else:
            print("\nOrder: Subscription Compound with Skip payment, is not created")
        self.driver.close()

    def test_EditOrder(self, setup, PracticeLogin, EditOrder):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nYour order is successfully updated')
        else:
            print("\nYour order is not update")
        self.driver.close()

    def test_RXOnetimeProvidePayment(self, setup, PracticeLogin, OnetimeRXProvidePayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Onetime RX with provide payment, created successfully')
        else:
            print("\nOrder: Onetime RX with provide payment, is not created")
        self.driver.close()

    def test_OTCOnetimeProvidePayment(self, setup, PracticeLogin, OnetimeOTCProvidePayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Onetime OTC with provide payment, created successfully')
        else:
            print("\nOrder: Onetime OTC with provide payment, is not created")
        self.driver.close()

    def test_CompoundOnetimeProvidePayment(self, setup, PracticeLogin, OnetimeCompoundProvidePayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Onetime Compound with provide payment, created successfully')
        else:
            print("\nOrder: Onetime Compound with provide payment, is not created")
        self.driver.close()

    def test_RXSubscriptionProvidePayment(self, setup, PracticeLogin, SubscriptionRXProvidePayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Subscription RX with provide payment, created successfully')
        else:
            print("\nOrder: Subscription RX with provide payment, is not created")
        self.driver.close()

    def test_OTCSubscriptionProvidePayment(self, setup, PracticeLogin, SubscriptionOTCProvidePayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Subscription OTC with provide payment, created successfully')
        else:
            print("\nOrder: Subscription OTC with provide payment, is not created")
        self.driver.close()

    def test_CompoundSubscriptionProvidePayment(self, setup, PracticeLogin, SubscriptionCompoundProvidePayment):
        self.driver = setup
        if "You're all set!" in self.driver.page_source:
            self.driver.find_element_by_partial_link_text("Return to Dashboard").click()
            print('\nOrder: Subscription Compound with provide payment, created successfully')
        else:
            print("\nOrder: Subscription Compound with provide payment, is not created")
        self.driver.close()

    def test_CreateOrderFromUserAccount(self, setup, UserLogin, OnetimeRXSkipPayment):
        self.driver = setup

    def test_CheckUserOrder(self, setup, PracticeLogin):
        self.driver = setup
        time.sleep(3)
        assert self.driver.find_element_by_xpath(Locators.myQueueOrderDate) in self.driver.page_source
        assert self.driver.find_element_by_xpath(Locators.myQueuePatientName) in self.driver.page_source
        # Pending bacause select indian timezone at the time of account creation and append created user name for Created By column