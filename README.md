OrangeHRM WebApplication Automation Framework
----
-------------------------
Introduction:
---
This web automation framework involves

- ✅ Built using Selenium WebDriver + Pytest +Data driven using csv + PytestHTML + Allure Reporting
- ✅ Page Object Model (POM) design
- ✅ Cross-browser support (Chrome, Firefox, Edge)
- ✅ Automatic screenshots on failure
- ✅ Data driven approach is done to read the test data from CSV and update the test result to the same
- ✅ Reporting done using:
  -     Allure reporting with title, step info and screenshots
  -     Also Pytest HTML reporting is done

Usage of this framework:
---------
To execute the automation testcases of web application and prepare proper test reports with test title, step info and screenshots.

Project Structure:
-----------------
------------------------------
Project2HRWebApp/data:
----
-  test_data.csv file contains different login credentials which will be read by framework during execution
        and then update the test result, execution date, tester name, etc. to the same sheet after execution

Project2HRWebApp/pages:
-----

- basepage.py: Common browser actions (click, type, waits)
- locators.py: All the element locators in one place
- loginpage.py: Login page related actions
- dashboardpage.py: Actions done in dashboard page that is shown after successful login

Project2HRWebApp/reports:
-------------
- allure-reports: will contain the allure report results
- html: will contain the pytest html report

Project2HRWebApp/tests:
-------
Classified the testcases based on their feature/functionality.
- test_dashboard.py
- test_leave_assignment.py
- test_login.py
- test_my_info.py
- test_new_user.py


Project2HRWebApp/utilities:
---------------
- capture_screenshot.py: Takes screenshots including the test failures
- constants.py: Stores values like URLs, credentials, etc.
- random_user_generator.py: helps to generate random username during run time to create new user testcase
- read_testdata_file.py: Helps to read the test_data.csv
- write_testdata_file.py: Helps to update the csv file with test results


Project2HRWebApp/conftest.py: Browser setup (Chrome, Firefox, Edge, etc.)
Project2HRWebApp/pytest.ini: Define markers to execute selected testcases. The markers are used in .feature file
Project2HRWebApp/requirements.txt: List of required Python libraries
Project2HRWebApp/README.md: You’re reading this file 😊

---------------------------------

Installed Plugins:
----------------
pytest
selenium
pytest-selenium
webdriver-manager
pytest html reporting: pytest-html
allure reporting: allure-python-commons, allure-pytest
csv handling: openpy, openpyxl





By using this project, you’ll understand:
----

- How to run web automation tests in Python
- How to read and write data using csv file
- How to use Page Object Model (POM) for clean code
- How to generate Allure Reports with screenshots
- How to generate pytest HTML reports

Pre-requisites:
----

- Python 3.8 or higher
- Google Chrome (or Firefox / Edge)
- Internet connection (for driver downloads)

Download the Plugins
-----
Run 'pip install -r requirements.txt' in project terminal

Reporting
----------

- To view the Allure test report run: allure serve reports
- This will open a detailed dashboard in your browser,
- Shows test results, logs and screenshots.
- To view the html report, directly open the .html file from reports/html/index.html

Commands to remember:
-------

1. To run all test files
   pytest   
2. To run selected test file
   pytest tests/test_login.py
3. To run test by marker for example 'smoke' defined in .ini file,and @smoke in.feature file
   pytest -m smoke
4. Run with Allure reporting: To run tests and generate report
   pytest --alluredir=reports/allure-results
   To view the report
   allure serve reports/allure-results
   This will automatically build and open the report in browser
   To save HTML report inside the reports folder.
   allure generate reports/allure-results -o reports/allure-reports --clean
5. To run with specific browser
   pytest --browser=firefox 
6. To run in verbose mode for debugging
   pytest -v  
7. To stop at first failure, this is useful for debugging one case at a time.
   pytest -x
8. To interrupt the execution: Ctrl+C

command to run testcases and generate both html and allure reports:
        pytest --browser=chrome --html=reports/html/report.html --self-contained-html --alluredir=reports/allure-results


To open the Allure report copied to different location/Google drive:
--------------
1. Open the command prompt in the folder where allure-results is copied
2. Run command: python -m http.server 8000
3. Then open the following link in the browser: http://localhost:8000/allure-report

Author
-------
Indumathi





