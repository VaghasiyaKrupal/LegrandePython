from openpyxl import load_workbook

FilePath = "C:/Users/Administrator/PycharmProject/LegrandePython/TestData/Data.xlsx"
datafile = load_workbook(FilePath)
loginSheet = datafile.get_sheet_by_name("Login Credentials")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = loginSheet.cell(2, 2).value
        return url

    @staticmethod
    def getUsername():
        username = loginSheet.cell(2, 3).value
        return username

    @staticmethod
    def getPassword():
        password = loginSheet.cell(2, 4).value
        return password
