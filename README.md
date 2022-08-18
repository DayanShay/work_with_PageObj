# work_with_class
Sela Project Pytest playwright with class

Before Runing - tests on this Branch - Must do - 
```commandline
pip install -r .\playwright_project_with_class\requirements.txt 
```
Configuration file:
If you want to Change Defualt settings 

file data_file_for_tests.json

```json
{
  "email": "Your Email", <- insert here your Email that you have signup with
  "password": "Your Password", <- insert here your Password that you have signup with
  "browser": "WebDriver"  <- insert here witch brwoser you want to use for the tests - "Chrome" OR "Firefox" ONLY ! 
  "url": "http://automationpractice.com/index.php" <- If You Have your Local Server - you can change the url here.
}
```
![image](https://user-images.githubusercontent.com/108628136/185473394-a5f5283d-fbaf-47e9-8093-19629a4538f7.png)


Running allure report 
```commandline
pytest --alluredir=playwrightReports\ .\playwright\test_playwright.py 
```
```commandline
allure serve .\playwrightReports\
```
![image](https://user-images.githubusercontent.com/108628136/185263434-42746437-4e70-475f-8576-bf8d78c2c4fc.png)
