# SchoolManagement
School Management Backend code using DRF


You can run the project by :
1. Using the virtual environment through the command **source /home/button_chicken/Desktop/SchoolManagement/env/bin/activate** (you can change the path accordingly)
OR
2. Installing the dependencies using **pip3 install -r requirements.txt**

Basic Commands:
1. To create a superuser - **python3 manage.py createsuperuser**
2. To run the project - **python3 manage.py runserver**
3. To make the migrations - **python3 manage.py makemigrations** followed by **python3 manage.py migrate**

Note- The postman collection has been included in the repo, you need to pass the JWT token with every request(except for login and register) in order to validate the user.
