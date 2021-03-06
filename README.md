#University of Pittsburgh Activity Finder

Setup of Django environment
1. Install Python3
2. Install virtualenv\
	$pip3 install virtualenv
3. Create virtualenv for the project\
	$virtualenv -p python3 myvenv
4. Activate virtualenv for the project\
	$source myvenv/bin/activate\
	Deactivate: $deactivate
5. Install Django\
    $pip3 install django
6. Create the project\
	$django-admin startproject UPitt_activity_finder
7. Install mysqlclient (library for connecting to MySQL)\
	$pip3 install mysqlclient
8. Create a database schema
	- schema name: UPitt_activity_finder_db
	- $python manage.py makemigrations
	- $python manage.py migrate
9. Check if server runs\
   	$python manage.py runserver 127.0.0.1:8000 (on local machine)\
	$python manage.py runserver 0.0.0.1:8000 (on server)
10. Create super user for administration login\
	$python manage.py createsuperuser
11. Install django-geoposition
    $pip install django-geoposition
