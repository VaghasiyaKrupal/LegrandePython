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

    def test_CreatingRXOnetimeSkipPayment(self, setup, RXPharmaLogin, OnetimeRXSkipPayment):
        self.driver = setup

    def test_CreatingOTCOnetimeSkipPayment(self, setup, RXPharmaLogin, OnetimeOTCSkipPayment):
        self.driver = setup

    def test_CreatingCompoundOnetimeSkipPayment(self, setup, RXPharmaLogin, OnetimeCompoundSkipPayment):
        self.driver = setup

    def test_CreatingRXSubscriptionSkipPayment(self, setup, RXPharmaLogin, SubscriptionRXSkipPayment):
        self.driver = setup

    def test_CreatingOTCSubscriptionSkipPayment(self, setup, RXPharmaLogin, SubscriptionOTCSkipPayment):
        self.driver = setup

    def test_CreatingCompoundSubscriptionSkipPayment(self, setup, RXPharmaLogin, SubscriptionCompoundSkipPayment):
        self.driver = setup

    def test_EditOrder(self, setup, PracticeLogin, EditOrder):
        self.driver = setup

    def test_RXOnetimeProvidePayment(self, setup, RXPharmaLogin, OnetimeRXProvidePayment):
        self.driver = setup

    def test_OTCOnetimeProvidePayment(self, setup, RXPharmaLogin, OnetimeOTCProvidePayment):
        self.driver = setup

    def test_CompoundOnetimeProvidePayment(self, setup, RXPharmaLogin, OnetimeCompoundProvidePayment):
        self.driver = setup

    def test_RXSubscriptionProvidePayment(self, setup, RXPharmaLogin, SubscriptionRXProvidePayment):
        self.driver = setup

    def test_OTCSubscriptionProvidePayment(self, setup, RXPharmaLogin, SubscriptionOTCProvidePayment):
        self.driver = setup

    def test_CompoundSubscriptionProvidePayment(self, setup, RXPharmaLogin, SubscriptionCompoundProvidePayment):
        self.driver = setup

    def test_EditOrder(self, setup, RXPharmaLogin, EditOrder):
        self.driver = setup
