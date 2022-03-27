# Gallery

## Author
### [Tracy Wangari]
## Description
Gallery is a picture gallery made with a Django application that allows user to display own photos for others to view.



## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running

   ```bash
   git clone https://github.com/Thuotracy/gallery-app.git
   ```
 or download a zip file of the project from github


Navigate to the project directory
```bash
cd gallery
```

##### 2. Create a virtual environment
 Install `Virtualenv`

   ```prettier
   python3 -m venv venv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   python3 -m venv Virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```
##### 3. Create a django and create django projects
 Install django
 ```bash
 pip install django
  ```
  Create django project
  ```bash
  django-admin startproject gallery.
```
create a tracy app
 ```bash
 django-admin startapp news
 ```



##### 5. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```picha```
   ```
   # create database picha
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python manage.py makemigrations gallery
```


then run the command below;

 ```bash
 python manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine,

    python3 manage.py runserver

## Technologies Used
* Django
* Python
* Html
* Css
* Bootstrap3
* Django-Admin

## Bugs
There are no known bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2022 Tracy

# Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

# Contacts
tracyjacobs775@gmail.com