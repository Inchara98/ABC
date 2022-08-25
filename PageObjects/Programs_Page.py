class Program_Objects:
    # List of Selenium attributes of Program Screen
    dashboard = "menu-item-0"
    nishtha = "menu-item-1"
    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"
    total_state = "//app-nishtha/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    total_enrollment = "//app-nishtha/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    total_completion = "//app-nishtha/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[1]"
    total_certification = "//app-nishtha/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[1]"
    total_medium = "//app-nishtha/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[1]"
    total_state_Tittle = "//app-nishtha/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"
    total_enrollment_Tittle = "//app-nishtha/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"
    total_completion_Tittle = "//app-nishtha/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[2]"
    total_certification_Tittle = "//app-nishtha/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[2]"
    total_medium_Tittle = "//app-nishtha/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[2]"
    Select_Program_Dropdown = ""
    Clear_Button = "//*[@id='filter-Program']/div/span[1]"
    program_logfile = "../../../Logs/Program.log"
    Program_dropdown = "ng-option-label ng-star-inserted"

    # Implementation Status
    Implementation_Status = "mat-tab-label-1-0"
    FullScreen = ""
    Zoomin = ""
    Zoomout = ""

    # Courses and Medium status
    state_colmn = "//*[@role='row']/td[1]"
    course_launch = "//*[@role='row']/td[2]"
    Medium = "//*[@role='row']/td[3]"
    CM_status = "mat-tab-label-0-1"
    dropdown_options = "//div[@role='option']/span"
    Choose_Program = "//div[@role='combobox']/input"
    Nishtha_1 = "//div[@role='option']/span[contains(text(),'NISHTHA 1.0')]"
    Nishtha_2 = "//div[@role='option']/span[contains(text(),'NISHTHA 2.0')]"
    Nishtha_3 = "//div[@role='option']/span[contains(text(),'NISHTHA 3.0')]"

    state_header = "//div[contains(text(),'State/UT Name')]"
    course_header = "//div[contains(text(),'Total Courses Launched')]"
    medium_header = "//div[contains(text(),'Total Mediums')]"

    state_sort = "//th[@role='columnheader'][1]"
    course_sort = "//th[@role='columnheader'][2]"
    medium_sort = "//th[@role='columnheader'][3]"

    state_values = "//td[1]"
    course_values = "//td[2]"
    medium_values = "//td[3]"

    # % against potential base
    PAP_Base = "mat-tab-label-2-3"
