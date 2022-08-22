
# NVSK_QA

###  Prerequisites:
 - Open the Terminal
 - Google Chrome need to be installed in the server.
   - Steps to install the Google Chrome
      ```
     wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
     sudo apt install ./google-chrome-stable_current_amd64.deb
     Check chrome brower version using command -> google-chrome -version
      ```
   - Navigate to the directory where NVSK_QA has been downloaded or cloned 
      ```
      cd NVSK_QA/
      git checkout NVSK_QA
      git pull
      ```
 - Chrome driver need to be downloaded and placed in the NVSK_QA/Driver/ folder.
 - Steps to Download the chrome driver 

 	Note: Based on the Chrome browser version need to download chrome driver ```https://sites.google.com/chromium.org/driver/```
   

 
- ### Steps to execute the test script
    ```
     cd NVSK_QA/
     sudo apt update
     sudo apt install python3-pip
    ```
 - Execute the Requirement.txt in the terminal (Requirement.txt file is present in the NVSK_QA Folder) [mandatory]
    ```
        sudo pip3 install -r Requirement.txt
    ```
 - Fill the config.ini file (config.ini file present in the NVSK_QA/Configuration/ Folder)
     ```		
    [config]
    baseURL=   #Fill the domain name provided in the config.yml file ex: https://domain_name
    username=  #Fill the username for NVSK login
    password=  #Fill the password for NVSK login
    ```  
## Navigate to NVSK_QA Directory in the terminal **(i.e cd /home/ubuntu/NVSK_QA/)**

- For Functional:
  ```
  pytest -v -s --capture=tee-sys Testsuite/functional_testsuite.py --html=Reports/Functional_Report.html
  ```

- For Regression:
  ```
  pytest -v -s --capture=tee-sys Testsuite/regression_testsuite.py --html=Reports/Regression_Report.html
  ```
            
- For System Testing:
  ```
  pytest -v -s --capture=tee-sys Testsuite/system_testsuite.py --html=Reports/System_Report.html
  ```           
- For Smoke Testing:
  ```
  pytest -v -s --capture=tee-sys Testsuite/smoke_testsuite.py --html=Reports/Smoke_Report.html 
  ```

##### Note : After execution of scripts,the report will be generated and saved in the Reports folder
