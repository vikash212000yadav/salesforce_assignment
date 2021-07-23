# SALESFORCE LOGIN API
In this assignment, I've have to implement salesforce integration. Which include
fetching user token from salesforce using OAuth2. Once you have the token You need to
fetch the list of Users, Accounts, and Contacts from salesforce and store it in the
database.


## Steps to install and run in local system:-
* Create a virtual environment ```$python3 -m venv <env_name>```
* Activate virtual environment ```$source <env_name>/bin/activate```
* Install requirements in venv ```$pip install -r requirements.txt```
* Make migrations ```$python manage.py makemigrations```
* Apply migrations ```$python manage.py migrate```
* Create a superuser ```$python manage.py createsuperuser```
* Run the server ```$python manage.py runserver```
