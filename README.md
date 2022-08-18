# work_with_class
Sela Project Pytest playwright with PageObj

Before Runing - tests on this Branch - Must do -

1) Download project Dictionary


Download - > https://github.com/DayanShay/work_with_class/tree/playwright/playwright_project_with_class

2) Install requirements

"FullPath" < - insert full path to requirements.txt file.

```commandline
pip install -r .\playwright_project_with_class\requirements.txt 
```

3) Configuration settings 

If you want to Change Defualt settings 

file data_file_for_tests.json < - inside the directory

```json
{
  "email": "Your Email", <- insert here your Email that you have signup with
  "password": "Your Password", <- insert here your Password that you have signup with
  "browser": "WebDriver"  <- insert here witch brwoser you want to use for the tests - "Chrome" OR "Firefox" ONLY ! 
  "url": "http://automationpractice.com/index.php" <- If You Have your Local Server - you can change the url here.
}
```
![image](https://user-images.githubusercontent.com/108628136/185473394-a5f5283d-fbaf-47e9-8093-19629a4538f7.png)

Run regularly with Python - pytest

"FullPath" < - insert full path to tests file.

```commandline
pytest "FullPath"\playwright_project_with_class\tests_playwright_with_class.py
```


Running allure report

"FullPath" < - insert full path to tests file.

```commandline
pytest --alluredir=playwrightReports\ "FullPath"\playwright_project_with_class\tests_playwright_with_class.py
```
"FullPath" < - insert full path to Reports directory.

```commandline
allure serve "FullPath"\playwrightReports\
```
![image](https://user-images.githubusercontent.com/108628136/185263434-42746437-4e70-475f-8576-bf8d78c2c4fc.png)
