class TestStandardPharma:
    def test_ForgotPassword(self, setup, RXPharmaForgotPassword):
        self.driver = setup
        self.driver.quit()

    def test_CreatePatient(self, setup, RXPharmaLogin, CreatePatient):
        self.driver = setup
        self.driver.quit()

    def test_CreateUser(self, setup, RXPharmaLogin, CreateUser):
        self.driver = setup
        self.driver.quit()

    def test_PatientMainSearch(self, setup, RXPharmaLogin, PatientMainSearch):
        self.driver = setup
        self.driver.quit()

    def test_ChangeProductPrice(self, setup, RXPharmaLogin, ChangeProductPrice):
        self.driver = setup
        self.driver.quit()

    def test_OnetimeRXSkipPayment(self, setup, RXPharmaLogin, OnetimeRXSkipPayment):
        self.driver = setup
        self.driver.quit()

    def test_ApproveOnetimeFromPracticeAccount(self, setup, PracticeLogin, ApproveOrderFromPractice):
        self.driver = setup
        self.driver.quit()

    def test_EditPatientDetails(self, setup, HubLogin, EditPatientDetails):
        self.driver = setup
        self.driver.quit()

    def test_PatientApprovalAndTransferOrderForOneSkip(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup
        self.driver.quit()

    def test_ProcessPaymentForOnetimeAndCreateLabel(self, setup, RXPharmaLogin, ProcessPaymentAndCreateLabel):
        self.driver = setup
        self.driver.quit()

    def test_OnetimeOTCSkipPayment(self, setup, RXPharmaLogin, OnetimeOTCSkipPayment):
        self.driver = setup
        self.driver.quit()

    def test_OnetimeCompoundSkipPayment(self, setup, RXPharmaLogin, OnetimeCompoundSkipPayment):
        self.driver = setup
        self.driver.quit()

    def test_SubscriptionRXSkipPayment(self, setup, RXPharmaLogin, SubscriptionRXSkipPayment):
        self.driver = setup
        self.driver.quit()

    def test_ApproveSubscriptionFromPracticeAccount(self, setup, PracticeLogin, ApproveOrderFromPractice):
        self.driver = setup
        self.driver.quit()

    def test_PatientApprovalAndTransferOrderForSubSkip(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup
        self.driver.quit()

    def test_ProcessPaymentAndConfirmPickUpPerson(self, setup, RXPharmaLogin, ProcessPaymentAndConfirmPickUpPerson):
        self.driver = setup
        self.driver.quit()

    def test_SubscriptionOTCSkipPayment(self, setup, RXPharmaLogin, SubscriptionOTCSkipPayment):
        self.driver = setup
        self.driver.quit()

    def test_SubscriptionCompoundSkipPayment(self, setup, RXPharmaLogin, SubscriptionCompoundSkipPayment):
        self.driver = setup
        self.driver.quit()

    def test_OnetimeRXProvidePayment(self, setup, RXPharmaLogin, OnetimeRXProvidePayment):
        self.driver = setup
        self.driver.quit()

    def test_ApprovePaymentOptionOnetimeOrderFromPracticeAccount(self, setup, PracticeLogin, ApproveOrderFromPractice):
        self.driver = setup
        self.driver.quit()

    def test_PatientApprovalAndTransferOrderForOnePro(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup
        self.driver.quit()

    def test_ProcessPaymentAndConfirmCourierPickUp(self, setup, RXPharmaLogin, ProcessPaymentAndCourierPickUp):
        self.driver = setup
        self.driver.quit()

    def test_OnetimeOTCProvidePayment(self, setup, RXPharmaLogin, OnetimeOTCProvidePayment):
        self.driver = setup
        self.driver.quit()

    def test_OnetimeCompoundProvidePayment(self, setup, RXPharmaLogin, OnetimeCompoundProvidePayment):
        self.driver = setup
        self.driver.quit()

    def test_SubscriptionRXProvidePayment(self, setup, RXPharmaLogin, SubscriptionRXProvidePayment):
        self.driver = setup
        self.driver.quit()

    def test_ApprovePaymentOptionSubscriptionOrderFromPracticeAccount(self, setup, PracticeLogin,
                                                                      ApproveOrderFromPractice):
        self.driver = setup
        self.driver.quit()

    def test_PatientApprovalAndTransferOrderForSubsPro(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup
        self.driver.quit()

    def test_ProcessPaymentForPaymentOptionOrderSubscriptionAndCreateLabel(self, setup, RXPharmaLogin,
                                                                           ProcessPaymentAndCreateLabel):
        self.driver = setup
        self.driver.quit()

    def test_SubscriptionOTCProvidePayment(self, setup, RXPharmaLogin, SubscriptionOTCProvidePayment):
        self.driver = setup
        self.driver.quit()

    def test_SubscriptionCompoundProvidePayment(self, setup, RXPharmaLogin, SubscriptionCompoundProvidePayment):
        self.driver = setup
        self.driver.quit()
