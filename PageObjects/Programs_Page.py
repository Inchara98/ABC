class Program_Objects:
    # List of Selenium attributes of Program Screen
    dashboard = "menu-item-0"
    nishtha = "menu-item-1"
    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"

    # Vanity cards
    total_state = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    total_enrollment = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    total_completion = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[1]"
    total_certification = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[1]"
    total_medium = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[1]"
    total_state_Tittle = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"
    total_enrollment_Tittle = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"
    total_completion_Tittle = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[2]"
    total_certification_Tittle = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[2]"
    total_medium_Tittle = "/html/body/app-root/app-layout/div/div[2]/div/app-nishtha/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[2]"

    Clear_Button = "//*[@id='filter-Program']/div/span[1]"
    program_logfile = "../../../Logs/Program.log"
    Program_dropdown = "ng-option-label ng-star-inserted"

    # Implementation Status
    Implementation_Status = "mat-tab-label-2-0"
    FullScreen = "//button/i"
    Zoomin = ""
    Zoomout = ""

    # Courses and Medium status
    state_colmn = "//*[@role='row']/td[1]"
    course_launch = "//*[@role='row']/td[2]"
    Medium = "//*[@role='row']/td[3]"
    CM_status = "mat-tab-label-0-1"
    Nishtha_1 = "ab8b77bb534f-0"
    Nishtha_2 = "ab8b77bb534f-1"
    Nishtha_3 = "ab8b77bb534f-2"

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
