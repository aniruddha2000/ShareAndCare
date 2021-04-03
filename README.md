**Share And Care - A Food Management Web Application** 

Theme: Food management 

Food wastage is a real concern at places where a lot of ready-to-eat food is produced. Create a web/mobile platform to put up leftover food for the nearby locals.

Share-and-Care is a web app designed to handle such scenarios. People can log in to the Share-and-Care website, create an account, upload details about leftover food by creating a food post, see and filter global food posts. 

**Developer Guide:**

In order to run the web app in the zip file follow these steps:
Prerequisites of the web app are python(>3.6), django, django-countries, django-phone-field and django-filter so they must be installed before.
Open a terminal in the directory and type:
     python3 manage.py makemigrations
     Python3 manage.py migrate
     python3 manage.py runserver
This will start a localhost server for Share-and-Care
If you are getting any errors like python3 not found then replace python3 with python in the above command.
Alternatively, if you have python 3.6 already then you can follow the pipenv creation stated as follows :
Create a new virtual environment and install the necessary packages -
$ pipenv install
Start the virtual environment.
$ pipenv shell
Start the development server.
$ pipenv run server


**“How To Use“ Guide:**

Sign in to create an account.
After signing in you’ll be automatically redirected to your profile homepage                                              
Click on “New post” to create a new post

After a new post has been created you can view it in my posts, whereas other users will be able to view it under the home section. The posts can be filtered using country and city filters and can be searched using global search options. The user can also modify or delete any posts under my post section.


And lastly, the user can edit their profile details under the “more” section


And that’s it.
