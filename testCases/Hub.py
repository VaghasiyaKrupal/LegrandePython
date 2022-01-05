from openpyxl import load_workbook

FilePath = "C:/Users/Administrator/PycharmProject/LegrandePython/TestData/Data.xlsx"
datafile = load_workbook(FilePath)
loginSheet = datafile.get_sheet_by_name("Login Credentials")


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

    def test_CreatingRXOnetimeSkipPayment(self, setup, HubLogin, OnetimeRXSkipPayment):
        self.driver = setup

    def test_CreatingOTCOnetimeSkipPayment(self, setup, HubLogin, OnetimeOTCSkipPayment):
        self.driver = setup

    def test_CreatingCompoundOnetimeSkipPayment(self, setup, HubLogin, OnetimeCompoundSkipPayment):
        self.driver = setup

    def test_CreatingRXSubscriptionSkipPayment(self, setup, HubLogin, SubscriptionRXSkipPayment):
        self.driver = setup

    def test_CreatingOTCSubscriptionSkipPayment(self, setup, HubLogin, SubscriptionOTCSkipPayment):
        self.driver = setup

    def test_CreatingCompoundSubscriptionSkipPayment(self, setup, HubLogin, SubscriptionCompoundSkipPayment):
        self.driver = setup

    def test_EditOrder(self, setup, HubLogin, EditOrder):
        self.driver = setup

    def test_RXOnetimeProvidePayment(self, setup, HubLogin, OnetimeRXProvidePayment):
        self.driver = setup

    def test_OTCOnetimeProvidePayment(self, setup, HubLogin, OnetimeOTCProvidePayment):
        self.driver = setup

    def test_CompoundOnetimeProvidePayment(self, setup, HubLogin, OnetimeCompoundProvidePayment):
        self.driver = setup

    def test_RXSubscriptionProvidePayment(self, setup, HubLogin, SubscriptionRXProvidePayment):
        self.driver = setup

    def test_OTCSubscriptionProvidePayment(self, setup, HubLogin, SubscriptionOTCProvidePayment):
        self.driver = setup

    def test_CompoundSubscriptionProvidePayment(self, setup, HubLogin, SubscriptionCompoundProvidePayment):
        self.driver = setup

    def test_EditOrder(self, setup, HubLogin, EditOrder):
        self.driver = setup
