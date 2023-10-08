# Personal Financial Monitor
The Restful-API for planning and monitoring personal financial. This project is designed for working with mobile application. 


# Setup Project
- ## Setup Virtual Environment
    #### 1. initiate virtual environment with command
    ```
    $ mkdir personalFinanceMonitor
    $ cd personalFinanceMonitor
    $ python -m venv env
    ```
    #### 2. run this command for activate virtual environment
    ```
    $ env\Scripts\activate
    ```
    when activate we will see
    ```
    (env) $ D:\personalFinanceMonitor>
    ```
    if you want to deactivate
    ```
    $ deactivate
    ```
- ## Install Modules and Dependency
    #### 1. run this command while you is in virtual environment
    ```
    $ pip install -r "requirements.txt"
    ```
- ## Setup Database for Development
    #### 1. Pull image MySQL and Phpmyadmin
    ```
    $ docker pull mysql
    $ docker pull phpmyadmin/phpmyadmin
    ```
    #### 2. Setup MySQL server instance
    ```
    $ docker run --name=keeplearning -e MYSQL_ROOT_PASSWORD=keep1234 -e MYSQL_DATABASE=keeplearning -p 3306:3306 -d mysql
    ```
    #### 3. Shell to MySQL Container
    ```
    $ docker exec -it keeplearning bash
    root@keeplearning:/# mysql -u root -p
    ```
    #### 4. Bind user connection
    ```
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'youpassword';
    ```
    #### 5. Show All Database name
    ```
    mysql> show databases;
    ```
    if you want to quit from shell database
    ```
    mysql> quit;
    ```
    #### 7. Setup Phpmyadmin 
    ```
    $ docker run --name myadmin -d --link keeplearning:db -p 8081:80 phpmyadmin/phpmyadmin
    ```
    you can access Web GUI Phpmyadmin through http://localhost:8081
- ## Testing Project
    #### 1. Run All TestCase
    ```
    $ pytest tests/
    ```
    #### 2. Run pytest with coverage
    ```
    $ coverage run -m pytest
    ```
    #### 3. View Coverage Report
    ```
    $ coverage report
    ```
    #### 4. Generate HTML Coverage Report
    ```
    $ coverage html
    ```
    An HTML report in the htmlcov/ directory and you can see on browser by open index.html