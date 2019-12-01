# Python Test

To check that your knowledge/research ability to use the Django framework meets what's required of a python role with WebIT.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install required python dependencies:

```
pip install -r requirements.txt
```
## Running the server
```
python manage.py migrate
python manage.py runserver
```

## Running the tests
```
python manage.py test
```

### Check coverage

```
coverage run manage.py test
coverage report
```

## Built With

* Python 3.7.5
* [Django](https://www.djangoproject.com/) - The web framework used

## Thoughts

* [django-filter](https://django-filter.readthedocs.io/en/master/) - 
This django plugin could have been used for creating a sophisticated search logic. 
Currently I just devised a simple searching logic that fits the requirement.

## Version Control

I used **Git** for local version control.