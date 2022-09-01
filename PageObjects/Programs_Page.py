class Program_Objects:
    # List of Selenium attributes of Program Screen
    L = r'L\.|[^\d.]'
    dashboard = "menu-item-0"
    nishtha = "menu-item-1"
    Diksha = "menu-item-2"
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
    Potential_Base = "mat-tab-label-2-3"

    # District Wise Status
    District_Status = "mat-tab-label-2-3"
    click_district_program = "//ng-select[@id='filter-Program']/div/div/div[3]/input"
    click_state_options = "//ng-select[@id='filter-State/UT']/div/div/div[3]/input"
    state_names_id = "aff430dd515c-"

    # Course wise Tab
    Course_Status = "mat-tab-label-0-4"


    # Micro_improvements program
    dashboard = "menu-item-0"
    Micro_improvements = "menu-item-3"
    a_plus = "font-size-increase"
    a_minus = "font-size-decrease"
    a_default = "font-size-reset"
    total_Micro_improvements_ongoing_value = "//app-improvement-program/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    total_Micro_improvements_ongoing_text = "//app-improvement-program/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"
    total_Micro_improvements_ongoing_info = "//app-improvement-program/div[1]/div/div[1]/sb-cqube-info-card/div/img"
    total_micro_improvements_started_info = "//app-improvement-program/div[1]/div/div[2]/sb-cqube-info-card/div/img"
    total_micro_improvements_started_number = "//app-improvement-program/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    total_micro_improvements_started_text = "//app-improvement-program/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"
    total_micro_improvements_in_progress_info = "//app-improvement-program/div[1]/div/div[3]/sb-cqube-info-card/div/img"
    total_micro_improvements_in_progress_value = "//app-improvement-program/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[1]"
    total_micro_improvements_in_progress_text = "//app-improvement-program/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[2]"
    total_micro_improvements_in_submitted_info="//app-improvement-program/div[1]/div/div[4]/sb-cqube-info-card/div/img"
    total_micro_improvements_in_submitted_value = "//app-improvement-program/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[1]"
    total_micro_improvements_in_submitted_text = "//app-improvement-program/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[2]"
    total_micro_improvements_in_submitted_with_evidence_info = "//app-improvement-program/div[1]/div/div[5]/sb-cqube-info-card/div/img"
    total_micro_improvements_in_submitted_with_evidence_value = "//app-improvement-program/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[1]"
    total_micro_improvements_in_submitted_with_evidence_text = "//app-improvement-program/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[2]"

    # Implementation Status micro-improvements
    Implementation_Status_micro_improvements = "//app-improvement-program/div[2]/mat-tab-group/mat-tab-header/div/div/div/div[1]"
    FullScreen = ""
    Zoomin = ""
    Zoomout = ""

    #improvements status micro improvements
    improvements_status_micro_improvements = '//*[text()="Improvements Status"]'
    dropdown_option = '//app-improvement-program/div[2]/mat-tab-group/div/mat-tab-body[2]/div/div/div/div/div[2]/div/div/app-level-n-metric-filter-panel/div/div/ng-select'
    Choose_metrics = '//*[@id="metricFilter-Metrics to be shown"]/div/div/div[1]'
    Total_micro_improvements = '//*[@id="af316e86d9fa-0"]/span'
    micro_improvements_started = '//*[@id="af316e86d9fa-1"]'
    micro_improvements_in_progress = '//*[@id="af316e86d9fa-2"]/span'
    micro_improvements_submitted = '//*[@id="af316e86d9fa-3"]/span'
    micro_improvements_submitted_with_evidence = '//*[@id="af316e86d9fa-4"]/span'

    # Diksha Program
    Totalstates_info = "//app-digital-learning/div[1]/div/div[1]/sb-cqube-info-card/div/img"
    Totalstates_UT = "//app-digital-learning/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[1]"
    Totalstates_text = "//app-digital-learning/div[1]/div/div[1]/sb-cqube-info-card/div/div/span[2]"
    Total_ETB_info = "//app-digital-learning/div[1]/div/div[2]/sb-cqube-info-card/div/img"
    Total_ETB = "//app-digital-learning/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[1]"
    Total_ETB_text = "//app-digital-learning/div[1]/div/div[2]/sb-cqube-info-card/div/div/span[2]"
    Total_QR_Code_info = "//app-digital-learning/div[1]/div/div[3]/sb-cqube-info-card/div/img"
    Total_QR_Code = "//app-digital-learning/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[1]"
    Total_QR_Code_text = "//app-digital-learning/div[1]/div/div[3]/sb-cqube-info-card/div/div/span[2]"
    Total_Content_info = "//app-digital-learning/div[1]/div/div[4]/sb-cqube-info-card/div/img"
    Total_Content = "//app-digital-learning/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[1]"
    Total_Content_text = "//app-digital-learning/div[1]/div/div[4]/sb-cqube-info-card/div/div/span[2]"
    Total_time_spent_info = "//app-digital-learning/div[1]/div/div[5]/sb-cqube-info-card/div/img"
    Total_time_spent = "//app-digital-learning/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[1]"
    Total_time_spent_text = "//app-digital-learning/div[1]/div/div[5]/sb-cqube-info-card/div/div/span[2]"

    Implementation_Status_tab = "//app-digital-learning/div[2]/mat-tab-group/mat-tab-header/div/div/div/div[1]"

    ETB_Coverage_Tab = "//*[contains(text(),'ETB Coverage Status')]"
    State_column = "//th[@role='columnheader'][1]"
    Curiculum_Textbook_column = "//th[@role='columnheader'][2]"
    Energised_Textbook_column = "//th[@role='columnheader'][3]"
    per_Energised_Textbook_column = "//th[@role='columnheader'][4]"
    State_header = "//div[contains(text(),'State/UT name')]"
    Curiculum_Textbook_header = "//div[contains(text(),'Total Curriculum Textbooks')]"
    Energised_Textbook_header = "//div[contains(text(),'Total Energized Textbooks')]"
    per_Energised_Textbook_header = "//div[contains(text(),'% Energized Textbooks')]"

    Content_Coverage_Tab = "//app-digital-learning/div[2]/mat-tab-group/mat-tab-header/div/div/div/div[3]"

    Learning_session_potential_tab = "//*[contains(text(),'Learning Sessions on Potential Users')]"

