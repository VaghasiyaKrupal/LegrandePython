import time
from Locators.DispenserLocators import DispenserLocators
from Locators.MasterLocators import MasterLocators
from Locators.PracticeLocators import PracticeLocators


class TestStandardPharma:
    def test_ForgotPassword(self, setup, RXPharmaForgotPassword):
        self.driver = setup
        self.driver.close()

    def test_CreatePatient(self, setup, RXPharmaLogin, CreatePatient):
        self.driver = setup

    def test_CreateUser(self, setup, RXPharmaLogin, CreateUser):
        self.driver = setup

    def test_PatientMainSearch(self, setup, RXPharmaLogin, PatientMainSearch):
        self.driver = setup

    def test_ChangeProductPrice(self, setup, RXPharmaLogin, ChangeProductPrice):
        self.driver = setup

    def test_OnetimeRXSkipPayment(self, setup, RXPharmaLogin, OnetimeRXSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_ApproveOnetimeFromPracticeAccount(self, setup, PracticeLogin, ApproveOrderFromPractice):
        self.driver = setup

    def test_EditPatientDetails(self, setup, HubLogin, EditPatientDetails):
        self.driver = setup

    def test_PatientApprovalAndTransferOrderForOneSkip(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup

    def test_ProcessPaymentForOnetimeAndCreateLabel(self, setup, RXPharmaLogin, ProcessPayment):
        self.driver = setup
        self.driver.find_element_by_xpath(DispenserLocators.createPostageLabelButton).click()
        self.driver.implicitly_wait(10)
        assert "(Payment processed once label is created)"
        self.driver.find_element_by_xpath(DispenserLocators.createLabelButton).click()
        time.sleep(3)
        assert "Congratulations, you have successfully created a postage label."
        self.driver.find_element_by_xpath(DispenserLocators.printLabelButton).click()
        time.sleep(1)
        self.driver.quit()

    def test_OnetimeOTCSkipPayment(self, setup, RXPharmaLogin, OnetimeOTCSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_OnetimeCompoundSkipPayment(self, setup, RXPharmaLogin, OnetimeCompoundSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_SubscriptionRXSkipPayment(self, setup, RXPharmaLogin, SubscriptionRXSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_ApproveSubscriptionFromPracticeAccount(self, setup, PracticeLogin, ApproveOrderFromPractice):
        self.driver = setup

    def test_PatientApprovalAndTransferOrderForSubSkip(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup

    def test_ProcessPaymentAndConfirmPickUpPerson(self, setup, RXPharmaLogin, ProcessPayment):
        self.driver = setup
        self.driver.find_element_by_class_name(MasterLocators.closeButton).click()
        self.driver.find_element_by_xpath(DispenserLocators.confirmPickUpButton).click()
        time.sleep(2)
        assert "You have successfully completed this order"
        dissmissButton = self.driver.find_element_by_xpath(PracticeLocators.dismissButton)
        self.driver.execute_script("arguments[0].click()", dissmissButton)
        self.driver.quit()

    def test_SubscriptionOTCSkipPayment(self, setup, RXPharmaLogin, SubscriptionOTCSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_SubscriptionCompoundSkipPayment(self, setup, RXPharmaLogin, SubscriptionCompoundSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_OnetimeRXProvidePayment(self, setup, RXPharmaLogin, OnetimeRXProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_ApprovePaymentOptionOnetimeOrderFromPracticeAccount(self, setup, PracticeLogin, ApproveOrderFromPractice):
        self.driver = setup

    def test_PatientApprovalAndTransferOrderForOnePro(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup

    def test_ProcessPaymentAndConfirmCourierPickUp(self, setup, RXPharmaLogin, ProcessPayment):
        self.driver = setup
        self.driver.find_element_by_class_name(MasterLocators.closeButton).click()
        self.driver.find_element_by_xpath(DispenserLocators.confirmCourierPickUp).click()
        time.sleep(1)
        assert "Order successfully updated."
        dissmissButton = self.driver.find_element_by_xpath(PracticeLocators.dismissButton)
        self.driver.execute_script("arguments[0].click()", dissmissButton)
        self.driver.find_element_by_xpath(DispenserLocators.completeButton).click()
        time.sleep(1)
        assert "You have successfully completed this order"
        btn = self.driver.find_element_by_xpath(PracticeLocators.dismissButton)
        self.driver.execute_script("arguments[0].click()", btn)
        self.driver.quit()

    def test_OnetimeOTCProvidePayment(self, setup, RXPharmaLogin, OnetimeOTCProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_OnetimeCompoundProvidePayment(self, setup, RXPharmaLogin, OnetimeCompoundProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_SubscriptionRXProvidePayment(self, setup, RXPharmaLogin, SubscriptionRXProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_ApprovePaymentOptionSubscriptionOrderFromPracticeAccount(self, setup, PracticeLogin, ApproveOrderFromPractice):
        self.driver = setup

    def test_PatientApprovalAndTransferOrderForSubsPro(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup

    def test_ProcessPaymentForPaymentOptionOrderSubscriptionAndCreateLabel(self, setup, RXPharmaLogin, ProcessPayment):
        self.driver = setup
        self.driver.find_element_by_xpath(DispenserLocators.createPostageLabelButton).click()
        self.driver.implicitly_wait(10)
        assert "(Payment processed once label is created)"
        self.driver.find_element_by_xpath(DispenserLocators.createLabelButton).click()
        time.sleep(3)
        assert "Congratulations, you have successfully created a postage label."
        self.driver.find_element_by_xpath(DispenserLocators.printLabelButton).click()
        time.sleep(1)
        self.driver.quit()

    def test_SubscriptionOTCProvidePayment(self, setup, RXPharmaLogin, SubscriptionOTCProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_SubscriptionCompoundProvidePayment(self, setup, RXPharmaLogin, SubscriptionCompoundProvidePayment):
        self.driver = setup
        self.driver.close()
