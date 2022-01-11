class TestHub:
    def test_ForgotPassword(self, setup, HubForgotPassword):
        self.driver = setup
        self.driver.close()

    def test_CreatePatient(self, setup, HubLogin, CreatePatient):
        self.driver = setup

    def test_CreateUser(self, setup, HubLogin, CreateUser):
        self.driver = setup

    def test_PatientMainSearch(self, setup, HubLogin, PatientMainSearch):
        self.driver = setup

    def test_ChangeProductPrice(self, setup, HubLogin, ChangeProductPrice):
        self.driver = setup

    def test_OnetimeRXSkipPayment(self, setup, HubLogin, OnetimeRXSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_EditPatientDetails(self, setup, HubLogin, EditPatientDetails):
        self.driver = setup

    def test_PatientApprovalAndTransferOrder(self, setup, HubLogin, PatientApprovalAndTransferOrder):
        self.driver = setup

    def test_CompleteOrder(self, setup, HubLogin, CompleteOrder):
        self.driver = setup

    def test_OnetimeOTCSkipPayment(self, setup, HubLogin, OnetimeOTCSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_OrderSendOutOfNetwork(self, setup, HubLogin, SendOutOfNetwork):
        self.driver = setup

    def test_OnetimeCompoundSkipPayment(self, setup, HubLogin, OnetimeCompoundSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_CancelOrder(self, setup, HubLogin, CancelOrder):
        self.driver = setup

    def test_SubscriptionOTCSkipPayment(self, setup, HubLogin, SubscriptionOTCSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_SubscriptionCompoundSkipPayment(self, setup, HubLogin, SubscriptionCompoundSkipPayment):
        self.driver = setup
        self.driver.close()

    def test_OnetimeRXProvidePayment(self, setup, HubLogin, OnetimeRXProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_OnetimeOTCProvidePayment(self, setup, HubLogin, OnetimeOTCProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_OnetimeCompoundProvidePayment(self, setup, HubLogin, OnetimeCompoundProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_SubscriptionOTCProvidePayment(self, setup, HubLogin, SubscriptionOTCProvidePayment):
        self.driver = setup
        self.driver.close()

    def test_SubscriptionCompoundProvidePayment(self, setup, HubLogin, SubscriptionCompoundProvidePayment):
        self.driver = setup
        self.driver.close()
