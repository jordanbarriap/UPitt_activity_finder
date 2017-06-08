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
    $pip install django
6. Create the project\
	$django-admin startproject UPitt_activity_finder
7. Install mysqlclient (library for connecting to MySQL)\
	$pip install mysqlclient
8. Check if server runs\
    $python manage.py runserver 127.0.0.1:8000
