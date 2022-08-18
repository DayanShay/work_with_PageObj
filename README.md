# work_with_PageObj
Sela Project Pytest selenium with PageObj



Before Running - tests on this Branch - Must do - 

1) Download project Dictionary

Download - > https://github.com/DayanShay/work_with_PageObj/tree/selenium/selenuim_project_with_PageObj

2) Install requirements

"FullPath" < - insert full path to requirements.txt file.

```commandline
pip install -r "FullPath"\selenuim_project_with_PageObj\requirements.txt 
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
  "path_driver" : "Full_Path_to_Driver" <- Suppurt Only Chrome or Firefox !
  "search_word" : "summer" <- Try Change The Search Word ! 

}
```
![image](https://user-images.githubusercontent.com/108628136/185474790-98e2aea6-388b-4dff-bea9-4fe38d964951.png)

Run regularly with Python - pytest

"FullPath" < - insert full path to tests file.

```commandline
pytest "FullPath"\selenium_project_with_PageObj\tests_selenium_with_PageObj.py
```

Running allure report :

"FullPath" < - insert full path to tests file.

```commandline
pytest --alluredir=selenuimReports\ "FullPath"\selenium_project_with_PageObj\tests_selenium_with_PageObj.py
```
"FullPath" < - insert full path to Reports directory.

```commandline
allure serve .\selenuimReports\
```

![image](https://user-images.githubusercontent.com/108628136/185255957-3097897d-4d4f-4d00-bc77-79acd17b93bc.png)
