from openpyxl import load_workbook

FilePath = "C:/Users/Administrator/PycharmProject/LegrandPython/TestData/Data.xlsx"
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

    def test_CreatingRXOnetimeSkipPayment(self, setup, PracticeLogin, OnetimeRXSkipPayment):
        self.driver = setup

    def test_CreatingOTCOnetimeSkipPayment(self, setup, PracticeLogin, OnetimeOTCSkipPayment):
        self.driver = setup

    def test_CreatingCompoundOnetimeSkipPayment(self, setup, PracticeLogin, OnetimeCompoundSkipPayment):
        self.driver = setup

    def test_CreatingRXSubscriptionSkipPayment(self, setup, PracticeLogin, SubscriptionRXSkipPayment):
        self.driver = setup

    def test_CreatingOTCSubscriptionSkipPayment(self, setup, PracticeLogin, SubscriptionOTCSkipPayment):
        self.driver = setup

    def test_CreatingCompoundSubscriptionSkipPayment(self, setup, PracticeLogin, SubscriptionCompoundSkipPayment):
        self.driver = setup

    def test_EditOrder(self, setup, PracticeLogin, EditOrder):
        self.driver = setup

    def test_RXOnetimeProvidePayment(self, setup, PracticeLogin, OnetimeRXProvidePayment):
        self.driver = setup

    def test_OTCOnetimeProvidePayment(self, setup, PracticeLogin, OnetimeOTCProvidePayment):
        self.driver = setup

    def test_CompoundOnetimeProvidePayment(self, setup, PracticeLogin, OnetimeCompoundProvidePayment):
        self.driver = setup

    def test_RXSubscriptionProvidePayment(self, setup, PracticeLogin, SubscriptionRXProvidePayment):
        self.driver = setup

    def test_OTCSubscriptionProvidePayment(self, setup, PracticeLogin, SubscriptionOTCProvidePayment):
        self.driver = setup

    def test_CompoundSubscriptionProvidePayment(self, setup, PracticeLogin, SubscriptionCompoundProvidePayment):
        self.driver = setup

    def test_EditOrder(self, setup, PracticeLogin, EditOrder):
        self.driver = setup
