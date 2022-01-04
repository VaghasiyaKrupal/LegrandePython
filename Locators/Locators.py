from openpyxl import load_workbook

FilePath = "C:/Users/Administrator/PycharmProject/LegrandPython/TestData/Data.xlsx"
datafile = load_workbook(FilePath)
datasheet = datafile.get_sheet_by_name('Test Data')


class Locators:
    # Login Locators
    Email = "email"
    Password = "password"
    button_SignIn = "[type='submit']"
    forgotPasswordLink = 'Forgot Your Password?'
    forgotPasswordTextbox = '//div[@role="dialog"]//*[@name="email"]'
    PatientForgotPasswordLink = '//*[text()="Forgot your password?"]'
    PatientForgotPasswordButton = '//*[text()="Send Reset Email"]'

    # Practice portal locators
    addPersonButton = "person_add"
    firstName = "first_name"
    lastName = "last_name"
    birthDate = "date_of_birth"
    phoneNumber = "phone"
    closeButton = "//button[@type='button' and text()='Close']"
    Add_RX = "add_rx"
    orderTemplateScreen = 'Order Templates'
    createTemplateButton = 'New Plan Template'
    documentsScreen = 'Documents'
    newDocuments = '//*[text()="Upload New Document"]'
    documentsDoctorSearchbox = '//*[@placeholder="Search by first or last name"]'
    selectDoctor = "//div[@data-test='_HINTS_HINT']//*[text()='" + datasheet.cell(2, 4).value + " " + "Practice']"
    selectDocumentsSearchbox = '//*[text()="Select a document type"]'
    documentsType = '//*[@class="Select-menu-outer"]//*[text()="Welcome Letter"]'
    documentTitle = '//*[@placeholder="Enter a title"]'
    uploadFile = '[type="file"]'
    viewDetails = "View Details"
    createAccountButton = "//button[@type='submit' and text()='Create Account']"
    Patient_search_textbox = '//*[@placeholder="Search by Name, Phone, or DOB (mm/dd/yyyy)"]'
    tableRow = '//tbody/tr'
    doctor_search_textbox = '//*[@placeholder="Search by Name"]'
    NextButton = '//button[@type="button" and text()="Next"]'
    CreateOnetimeRXButton = "//*[text()='Create New Rx']"
    createSubscriptionRxButton = "//*[text()='Create Custom Plan']"
    OnetimeSearchMedicine = "New One-time Rx"
    searchForMedication = '//*[@placeholder="Search for a Medication"]'
    AddButton = "//*[@class='is-flex row']//*[text()='Add']"
    addProductButton = "//*[text()='Add']"
    ProductQuantity = "//*[@data-test='amount']//*[@class='Select-arrow']"
    Quantity = '//*[@class="Select-menu-outer"]//*[text()="2"]'
    ProductRefilles = '//*[@data-test="refills"]//*[@class="Select-arrow"]'
    DAWCheckbox = '//*[@class="sc-eMigcr cVTyKh"]'
    productInstruction = '//*[@placeholder="Enter Rx Instructions"]'
    allergiesButton = '(//*[text()="Edit"])[3]'
    allergiesTextbox = '//*[@class="modal-dialog"]//input[@class="sc-kLIISr eXqdIs"]'
    doneButton = "//*[text()='Done']"
    addDropchartButton = "//*[@data-test='edit-document']"
    selectDocuments = '(//*[@class="modal-dialog"]//*[@type="checkbox"])[1]'
    selectButton = '//*[@class="modal-dialog"]//*[text()="Select"]'
    skipPayment = '//*[text()="Skip Payment"]'
    providePayment = '//*[text()="Provide Payment"]'
    surgeryDate = '//*[@placeholder="MM/DD/YYYY"]'
    pharmacyNotes = '//*[@placeholder="Enter notes for the pharmacist. (optional) "]'
    submitButton = '//*[text()="Submit"]'
    selectOnetimeTemplate = "(//*[@type='button' and text()='Select'])[1]"
    selectSubscriptionTemplate = "(//*[@type='button' and text()='Select'])[2]"
    templateTitle = '//*[@placeholder="Template Title"]'
    continueButton = "//*[text()='Continue']"
    templateProductSearch = '//*[@placeholder="Search for a Product"]'
    subscriptionProductSearch = '//*[@placeholder="Search for a product"]'
    templateNotes = '//*[@placeholder="Enter notes for the pharmacist"]'
    saveTemplateButton = '//*[text()="Save Template"]'
    accountLinkLabel = 'account-link-label'
    manageUser = 'Manage Users'
    addUserButton = '//*[text()="Add New User"]'
    selectAccountType = 'Select-arrow'
    clerkOption = '//*[@class="Select-menu-outer"]//*[text()="Clerk"]'
    dismissButton = '//*[@type="button" and text()="Dismiss"]'
    mainPatientSearch = 'search'
    mainSearchTextbox = '//*[@placeholder="Search for a Patient by Name or DOB"]'
    mainSearchButton = 'Search-btn'
    cardName = 'name'
    cardNumber = 'number'
    cardCVV = 'cvv'
    cardMonthDropdown = '(//*[@id="card"]//*[@class="Select-arrow"])[2]'
    cardYearDropdown = '(//*[@id="card"]//*[@class="Select-arrow"])[3]'
    cardMonth = "//*[@class='Select-menu-outer']//*[text()='" + datasheet.cell(2, 16).value + "']"
    cardYear = "//*[@class='Select-menu-outer']//*[text()='" + str(datasheet.cell(2, 17).value) + "']"
    addressLine1 = 'street_1'
    addressLine2 = 'street_2'
    addressCity = 'city'
    addressState = '//*[@id="shipping_address"]//*[@class="Select-arrow"]'
    addressZipCode = 'zip'
    state = "//div[@class='Select-menu-outer']//div[@role='option' and text()='" + datasheet.cell(2, 21).value + "']"
    updateOrderButton = '//*[text()="Update Order"]'

    # Hub Portal Locator
    productList = "Product List"
    updateButton = '//*[text()="Update"]'
    changePriceButton = '//*[text()="Change Item Price"]'

    # Patient Portal Locators
    allergies = 'allergies.0'
    payorAccountNumber = 'account_number'
    payorGroupNumber = 'group_number'
    payorRxBinNumber = 'rx_bin'
    payorPCnNumber = 'pc_number'
    payorPhoneNumber = 'insurer_phone'
    completePayment = '(//*[text()="Complete Payment"])[1]'
    patientAccountLink = '(//*[@fill="currentColor"])[2]'
    patientSettings = '//*[text()="Settings"]'
    patientAccount = "//*[text()='Account']"
    patientPassword = '//*[text()="Password"]'
    patientHealthInsurance = '//*[text()="Health Insurance"]'
    patientAllergies = '//*[text()="Allergies"]'
    patientPreference = '//*[text()="Preferences"]'
    orderScreen = 'orders'
    firstOrder = 'css-5sgxtb'
    saveUpdateButton = "//*[text()='Save Updates']"
    newDate = '(//*[text()="1"])[2]'
    updatePaymentButton = '(//*[text()="Update"])[2]'
    updateShippingButton = '(//*[text()="Update"])[3]'
    CardNumber = 'CardNumber'
    ExperientionDate = 'ExpirationDate'
    cvvCode = "SecurityCode"
    PostalCode = "PostalCode"
    cardDetails = '5555 5537 5304 8194'
    cardExpiryDate = '12/25'
    cardCvvCode = '354'
    cardPostalCode = '584697'
    iframeSaveButton = '//*[text()="Save"]'
    shippingState = '//input[@id="state"]'
    stateValue = "//*[text()='"+datasheet.cell(2, 26).value+"']"
    currentPasswordID = 'old_password'
    newPasswordID = 'new_password'
    confirmPasswordID = 'confirm_password'
    addNewInsurance = '//*[text()="Add New Insurance"]'
    payorID = 'payor_id'
    firstPayor = '//form[1]/div[1]/div[1]/div[1]/div[2]/div[1]'
    editPayorName = '//form[1]/div[1]/div[1]/div[1]/div[2]/div[2]'
    addInsuranceButton = '//*[@type="submit" and text()="Add Insurance"]'
    allergiesID = 'allergy'
    addAllergyButton = '//*[text()="Add Allergy"]'
    removeAllergyButton = '//*[@aria-label="remove-allergy"]'
    confirmButton = '//*[text()="Confirm"]'
    messageCheckbox = '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div[2]/label/span'
    additionalCheckbox = '//*[@id="__next"]/div/div[2]/div[1]/div[3]/div[2]/label/span/span'
    cancelPlanCheckbox = '//*[text()="Permanently cancel my plan."]'
    reasoneDropdownID = 'selected_remarks'
    selectOtherReason = '//*[text()="Other"]'
    userReasonID = 'user_remarks'

