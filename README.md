# Teacher Management

This project is for teacher management. Have a directory of teachers and their details, its displayed in the web format.
can create an entry for teacher with unique mobile and email id, a teacher can teach maximum of 5 subject.

### Setup the project

clone the repository 

```
https://github.com/girishvas/teachers.git
```
move to the project folder 
```
cd teachers
```

there are two methods to setup the project.

#### 1. Docker

then run the docker compose command to run the project. Docker will configure the project, installl all the dependencies and
run the project. Make sure that the directory contains the `Dockerfile` and `docker-compose.yml` files.

```
docker-compose build
docker-compose up
```
project will available in the below link
```
http://127.0.0.1:8000/
```

#### 2. Virtual environment 

--> Create a Python Virtualenv and activate it
```
virtualenv env --python python3.6
source .env/bin/activate
```
--> Install project requirements
```
pip install -r requirement.txt
```

--> Run Database migration
```
./manage.py migrate 
```
--> Create a Superuser to manage the system

```
./manage.py createsuperuser
```

 Run the Project
```
./manage.py runserver
```
The application will be available in below link
```
http://127.0.0.1:8000/
```
