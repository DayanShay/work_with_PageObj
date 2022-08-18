# work_with_class
Sela Project Pytest selenium


Before Runing - tests on this Branch - Must do - 
```commandline
pip install -r .\selenuim_project_with_class\requirements.txt 
```

Configuration  :
If you want to Change Defualt settings 

file data_file_for_tests.json

```json
{
  "email": "Your Email", <- insert here your Email that you have signup with
  "password": "Your Password", <- insert here your Password that you have signup with
  "browser": "WebDriver"  <- insert here witch brwoser you want to use for the tests - "Chrome" OR "Firefox" ONLY ! 
  "url": "http://automationpractice.com/index.php" <- If You Have your Local Server - you can change the url here.
  "path_driver" : "Full_Path_to_Driver" <- Suppurt Only Chrome or Firefox !
  "search_word" : "summer" <- Do not Change The Search Word ! 

}
```
![image](https://user-images.githubusercontent.com/108628136/185474790-98e2aea6-388b-4dff-bea9-4fe38d964951.png)

Running allure report :
```commandline
pytest --alluredir=selenuimReports\ .\playwright\test_playwright.py 
```
```commandline
allure serve .\selenuimReports\
```

![image](https://user-images.githubusercontent.com/108628136/185255957-3097897d-4d4f-4d00-bc77-79acd17b93bc.png)
