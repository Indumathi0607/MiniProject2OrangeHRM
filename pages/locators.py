from selenium.webdriver.common.by import By


class Locators:
    # locators in Login page
    company_branding_image = (By.XPATH, ("//img[@alt = 'company-branding']"))  # XPATH
    login_title = (By.XPATH, "//h5[@class = 'oxd-text oxd-text--h5 orangehrm-login-title']")  # XPATH
    username_title = (By.XPATH, "//label[@class = 'oxd-label' and text() = 'Username']")  # XPATH
    username_input = (By.XPATH, "//input[@name= 'username']")  # XPATH
    password_title = (By.XPATH, "//label[@class = 'oxd-label' and text() = 'Password']")  # XPATH
    password_input = (By.XPATH, "//input[@name= 'password']")  # XPATH
    login_button = (By.XPATH, "//button[@type= 'submit']")  # XPATH
    forgot_password_link = (By.XPATH, "//p[text() = 'Forgot your password? ']")  # XPATH
    invalid_credentials_message = (By.XPATH, "//p[@class ='oxd-text oxd-text--p oxd-alert-content-text']")  # XPATH
    required_error_message = (By.XPATH, "//span[text() = 'Required']") #XPATH

    #locators in Dashboard page
    dashboard_title = (By.XPATH, ("//h6[text() = 'Dashboard']")) #XPATH
    user_dropdown = (By.XPATH, "//p[@class = 'oxd-userdropdown-name']") #XPATH
    logout_option = (By.XPATH, "//ul[@class = 'oxd-dropdown-menu']//a[text() = 'Logout']") #XPATH
    admin_menu_option = (By.XPATH, "//span[@class = 'oxd-text oxd-text--span oxd-main-menu-item--name' and text() = 'Admin']") #XPATH
    my_info_menu_option = (By.XPATH, "//span[@class = 'oxd-text oxd-text--span oxd-main-menu-item--name' and text() = 'My Info']")  # XPATH
    leave_menu_option = (By.XPATH, "//span[@class = 'oxd-text oxd-text--span oxd-main-menu-item--name' and text() = 'Leave']")  #XPATH
    claim_menu_option = (By.XPATH, "//span[@class = 'oxd-text oxd-text--span oxd-main-menu-item--name' and text() = 'Claim']") #XPATH
    add_user_button = (By.XPATH, "//button[@class= 'oxd-button oxd-button--medium oxd-button--secondary']") #XPATH
    my_info_submenu_title = (By.XPATH, "(//h6[@class = 'oxd-text oxd-text--h6 orangehrm-main-title'])[1]") #XPATH

    #Locators in Admin menu
    user_role_dropdown = (By.XPATH, "(//div[@class = 'oxd-select-text-input'])[1]") #XPATH
    ess_user_role = (By.XPATH, "//div[@role='listbox']//span[text()='ESS']") #XPATH
    status_dropdown = (By.XPATH, "(//div[@class = 'oxd-select-text-input'])[2]") #XPATH
    status_enabled = (By.XPATH, "//div[@role='listbox']//span[text()='Enabled']")  # XPATH
    employee_name_input = (By.XPATH, '//input[@placeholder = "Type for hints..."]') #XPATH
    employee_name_suggestion_list = (By.XPATH, "(//div[@role='listbox']//span)[1]") #XPATH
    new_username_input = (By.XPATH, "//label[text() ='Username']//parent::div//following-sibling::div/input") #XPATH
    new_password_input = (By.XPATH, "//label[text() = 'Password']//parent::div//following-sibling::div/input[@type= 'password']") #XPATH
    confirm_password_input = (By.XPATH, "//label[text() = 'Confirm Password']//parent::div//following-sibling::div/input[@type= 'password']") #XPATH
    save_button = (By.XPATH, "//button[@type = 'submit']") #XPATH
    user_management_tab = (By.XPATH, "//span[text() = 'User Management ']") #XPATH

    #Dashboard - Leave locators
    assign_leave_tab = (By.XPATH, "//a[text() = 'Assign Leave']")
    leave_type_dropdown = (By.XPATH, "(//div[@class = 'oxd-select-text-input'])")  # XPATH
    leave_option = (By.XPATH, "//div[@role='listbox']//span[text()='CAN - Matternity']")  # XPATH

    #Dashboard - Claims locators
    submit_claim_tab = (By.XPATH, "//a[text() = 'Submit Claim']") #XPATH
    event_drop_down = (By.XPATH, "(//div[@class = 'oxd-select-wrapper']//div[text() = '-- Select --'])[1]") #XPATH
    event_option = (By.XPATH, "(//div[@role='listbox']//span)[2]")
    currency_drop_down = (By.XPATH, "(//div[@class = 'oxd-select-wrapper']//div[text() = '-- Select --'])[2]")  # XPATH
    currency_option = (By.XPATH, "//div[@role='listbox']//span[text()='Indian Rupee']") #XPATH
    remarks_input = (By.XPATH, "oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical") #XPATH
    create_button = (By.XPATH, "//button[@type= 'submit']") #XPATH
    submit_claim_confirmation = (By.XPATH, "//h6[text() = 'Submit Claim']") #XPATH

    #Locators of Forgot password popup
    fp_title_text = (By.XPATH, "//p[@class = 'oxd-text oxd-text--p orangehrm-card-note orangehrm-forgot-password-card-note']/p") #XPATH
    fp_username_input = (By.XPATH, "//input[@name = 'username']") #XPATH
    fp_reset_password_button = (By.XPATH, "//button[@type = 'submit']") #XPATH
    fp_reset_link_sent_message = (By.XPATH, "//h6[@class ='oxd-text oxd-text--h6 orangehrm-forgot-password-title']") #XPATH


