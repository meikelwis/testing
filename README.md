# Project Title

Testing Project

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

These projet run on Ubuntu 16.04 and 18.04. What things you need to install the software and how to install them

1. Virtualenv using python3 using command sudo apt install virtualenv
2. Pip using command sudo apt install python3-pip

### Installing

A step by step series of examples that tell you how to get a development env running

```
1. Initialize using command virtualenv -p python3 env
2. Activate virtualenv using source env/bin/activate
3. Make sure pip version is pip >=18 by running pip --version. If it's not, run pip install --upgrade pip
4. Change directory to project folder and run pip install -r requirements.txt
5. Change .env file and adjust it with local configuration
6. Run python manage.py migrate to finish the migration
6. Run python manage.py runserver

```

## Running the tests

```
1. API can be access through the POSTMEAN or INSOMNIA.
2. To insert the data into database can be process the localhost/getdownloaddata
3. If the configuration right it will be process to database.
4. The list url can be seen through urls.py

```

### Break down into end to end tests

```
Now i am still not developing the unit testing because i am not expert at that things. For prouduction i am using fabric as the deployment to make more easy.
But since that the fabric file is private files and have different configuration depends on the project i am not going to put it at here.
```

## Built With

* [Dropwizard](https://docs.djangoproject.com/en/2.1/) - The web framework used
* [Pip](https://pypi.org/project/Django/) - Dependency Management
