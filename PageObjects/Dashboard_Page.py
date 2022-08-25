class Dashboard_Objects:
    # Login Screen locators
    username = "username1"
    password = "password1"
    login_btn = "login"

    # List of selenium locator of dashboard screen
    user_name_field = ""
    password_filed = ""
    login_button = ""
    login_logfile = "../../../Logs/Login.log"
    dashboard_logfile = "../../../Logs/Dashboard.log"

    # Nishtha Card
    nishtha_info = "//sb-cqube-program-card[1]/div/img"
    total_teachers = "//sb-cqube-program-card[1]/div/div[2]/div[1]/span[1]"
    total_course = "//sb-cqube-program-card[1]/div/div[2]/div[1]/span[2]"
    teacher_text = "//sb-cqube-program-card[1]/div/div[2]/div[2]/span[1]"
    course_text = "//sb-cqube-program-card[1]/div/div[2]/div[2]/span[2]"
    Nisha_dashboard = "//sb-cqube-program-card[1]/div/button"

    # Diksha ETB abd e-Content
    diksha_info = "//sb-cqube-program-card[2]/div/img"
    total_content = "//sb-cqube-program-card[2]/div/div[2]/div[1]/span[1]"
    total_etbs = "//sb-cqube-program-card[2]/div/div[2]/div[1]/span[2]"
    content_text = "//sb-cqube-program-card[2]/div/div[2]/div[2]/span[1]"
    etb_text = "//sb-cqube-program-card[2]/div/div[2]/div[1]/span[2]"
    Diksha_dashboard = "//sb-cqube-program-card[2]/div/button"

    # Micro-Improvements
    micro_info = "//sb-cqube-program-card[3]/div/img"
    total_states = "//sb-cqube-program-card[3]/div/div[2]/div[1]/span[1]"
    total_micro = "//sb-cqube-program-card[3]/div/div[2]/div[2]/span[1]"
    micro_text = "//sb-cqube-program-card[3]/div/div[2]/div[2]/span[2]"
    states_text = "//sb-cqube-program-card[3]/div/div[2]/div[2]/span[1]"
    Micro_Dashboard = "//sb-cqube-program-card[3]/div/button"

    # PM POSHAN
    pm_info = "//sb-cqube-program-card[4]/div/img"
    total_schools = "//sb-cqube-program-card[4]/div/div[2]/div[1]/span[1]"
    total_state = "//sb-cqube-program-card[4]/div/div[2]/div[1]/span[2]"
    schools_text = "//sb-cqube-program-card[4]/div/div[2]/div[1]/span[2]"
    pmstate_text = "//sb-cqube-program-card[4]/div/div[2]/div[2]/span[2]"
    PM_dashboard = "//sb-cqube-program-card[4]/div/button"

    # NAS
    nas_info = "//sb-cqube-program-card[5]/div/img"
    total_std_surveyed = "//sb-cqube-program-card[5]/div/div[2]/div[1]/span[1]"
    total_scs_surveyed = "//sb-cqube-program-card[5]/div/div[2]/div[2]/span[1]"
    school_survey_text = "//sb-cqube-program-card[5]/div/div[2]/div[1]/span[2]"
    student_survey_text = "//sb-cqube-program-card[5]/div/div[2]/div[2]/span[2]"
    NAS_dashboard = "//sb-cqube-program-card[5]/div/button"

    # UDISE
    udise_info = "//sb-cqube-program-card[6]/div/img"
    ts_surveyed = "//sb-cqube-program-card[6]/div/div[2]/div[1]/span[1]"
    total_teacher = "//sb-cqube-program-card[6]/div/div[2]/div[2]/span[1]"
    ts_text = "//sb-cqube-program-card[6]/div/div[2]/div[1]/span[2]"
    teachers_text = "//sb-cqube-program-card[6]/div/div[2]/div[2]/span[2]"
    UDISE_dashbord = "//sb-cqube-program-card[6]/div/button"

    #   Performance Grade Index (PGI)
    pgi_info = "//sb-cqube-program-card[7]/div/img"
    pg_states = "//sb-cqube-program-card[7]/div/div[2]/div[1]/span[1]"
    pg_parameters = "//sb-cqube-program-card[7]/div/div[2]/div[2]/span[1]"
    pg_state_text = "//sb-cqube-program-card[7]/div/div[2]/div[1]/span[2]"
    pg_parameters_text = "//sb-cqube-program-card[7]/div/div[2]/div[2]/span[2]"
    PGI_dashboard = "//sb-cqube-program-card[7]/div/button"

    #   NIPUN Bharath
    nipun_info = "//sb-cqube-program-card[8]/div/img"
    total_learnings = "//sb-cqube-program-card[8]/div/div[2]/div[1]/span[1]"
    total_contents = "//sb-cqube-program-card[8]/div/div[2]/div[2]/span[1]"
    learning_text = "//sb-cqube-program-card[8]/div/div[2]/div[1]/span[2]"
    contents_text = "//sb-cqube-program-card[8]/div/div[2]/div[2]/span[2]"
    NIPUN_dashboard = "//sb-cqube-program-card[8]/div/button"

    # NCERT Quiz
    ncert_info = "//sb-cqube-program-card[9]/div/img"
    total_enrolment = "//sb-cqube-program-card[9]/div/div[2]/div[1]/span[1]"
    total_certification = "//sb-cqube-program-card[9]/div/div[2]/div[1]/span[2]"
    enrolment_text = "//sb-cqube-program-card[9]/div/div[2]/div[2]/span[1]"
    certification_text = "//sb-cqube-program-card[9]/div/div[2]/div[2]/span[2]"
    NCERT_dashboard = "//sb-cqube-program-card[9]/div/button"

    # NCF
    ncf_info = "//sb-cqube-program-card[10]/div/img"
    total_participating = "//sb-cqube-program-card[10]/div/div[2]/div[1]/span[1]"
    total_paper = "//sb-cqube-program-card[10]/div/div[2]/div[1]/span[2]"
    participating_text = "//sb-cqube-program-card[10]/div/div[2]/div[2]/span[1]"
    paper_text = "//sb-cqube-program-card[10]/div/div[2]/div[2]/span[2]"
    NCF_dashboard = "//sb-cqube-program-card[10]/div/button"
