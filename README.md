## Instawork Assignment

## Requirements :
**Python 3.7,**
**Mysql,**
**pipenv or pip**


## Installation :
**Create local .env file and update this file with content of env.example available in project directory**<br />
**Create Database using command: CREATE DATABASE instawork_db CHARACTER SET UTF8;**<br />
**Create User using command: CREATE USER instawork;**<br />
**Grant permission using command: GRANT ALL ON instawork_db.\* to 'instawork'@'localhost' identified by 'instawork1!';**<br />
**Clone the Project and change directory to Project root: cd instawork_assignment**<br />
**Init Virtual env using: pipenv shell or virtualenv <env_name>**<br />
**Install requirements using : pipenv install or pip install -r requirements.txt**<br />
**Run migrations using(makemigrations command not required) : python manage.py migrate**<br />
**Run server using python manage.py runserver 0.0.0.0:8000**<br />
**base_url:localhost, port:8000**<br />


## Project Description

CRUD APIs for Members Model

#### Endpoints :
base_url : \<host>:\<port>

#### 1) List the members: 
 **EndPoint** : <base_url>/members/<br />
 **Method** : GET<br />
 **Response Code** : 200<br />
 **Sample Response** : [
    {
        "id": "fe877267-688e-4b55-b4b9-509174e99017",
        "first_name": "Vidyasagar",
        "last_name": "Goutam",
        "email": "vidyasagargtm@gmail.com",
        "phone": "9643807502",
        "role": "admin"
    }
]

#### 2) Create a member:
 **EndPoint** : \<base_url>/members/<br />
 **Method** : POST<br />
 **Data** : {
        "first_name": "Vidyasagar",
        "last_name": "Goutam",
        "email": "vidyasagargtm@gmail.com",
        "phone": "9643807502",
        "role": "admin"
    }<br />
 **Role Choices** : admin, regular<br />
 **Response Code** : 201<br />
 **Sample Response** :   
   {
        "id": "fe877267-688e-4b55-b4b9-509174e99017",
        "first_name": "Vidyasagar",
        "last_name": "Goutam",
        "email": "vidyasagargtm@gmail.com",
        "phone": "9643807502",
        "role": "admin"
    }
 
 #### 3) Update a member : 
 **EndPoint** : <base_url>/members/\<pk><br />
 **Method** : PUT<br />
 **Data** :    {
        "first_name": "Vidyasagar",
        "last_name": "Goutam",
        "email": "vidyasagargtm@gmail.com",
        "phone": "9643807502",
        "role": "admin"
    }<br />
 **Role Choices** : admin, regular<br />
 **Response Code** : 200<br />
 **Sample Response** :   
   {
        "id": "fe877267-688e-4b55-b4b9-509174e99017",
        "first_name": "Vidyasagar",
        "last_name": "Goutam",
        "email": "vidyasagargtm@gmail.com",
        "phone": "9643807502",
        "role": "admin"
   }
  
 #### 4) Update a member : Requires updated parameters only
 **EndPoint** : <base_url>/members/\<pk><br />
 **Method** : PATCH<br />
 **Data** : {
        "first_name": "Naveen",
        "last_name": "Kumar",
        "role": "regular"
    }<br />
 **Role Choices** : admin, regular<br />
 **Response Code** : 200<br />
 **Sample Response** :   
  {
       "id": "fe877267-688e-4b55-b4b9-509174e99017",
       "first_name": "Naveen",
       "last_name": "Kumar",
       "email": "vidyasagargtm@gmail.com",
       "phone": "9643807502",
       "role": "regular"
  }
 
 #### 5) Delete a member : 
 **EndPoint** : <base_url>/members/\<pk><br />
 **Method** : DELETE<br />
 **Response Code** : 204   