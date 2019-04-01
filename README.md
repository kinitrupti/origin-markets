# Origin Markets with Django #

I have used a form of authentication, so that each user will only see their own data with DRF Auth.
The GLEIF API finds the corresponding Legal Name of the entity which issued the bond.


# How to use

Postman add on extension for chrome if very useful and handy to test the api. I recommend using it.

We will follow these steps:

    * Installing Django
    * Making the Django Project
    * Installing Django Rest Framework
    * Setup the Login Function and api route
    * Testing the Login api route
    * Using the Token to access authenticated Api
    * GLEIF API to fetch the data

Atatched screenshots for reference.

I have not used models for the queries. It can be made to use models and django-filter.

# Installation

pip3 install -r requirements.txt

$ git clone https://github.com/kinitrupti/origin-markets.git
$ cd origin-markets/
$ virtualenv --python=`which python3` venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cd myproject
$ python manage.py migrate
$ python manage.py runserver
