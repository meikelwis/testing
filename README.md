# Project Title

Testing Project

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

These project run on Ubuntu 16.04 and 18.04. Things you need to install and how to install them

1. Virtualenv using python3 using command sudo apt install virtualenv
2. Pip using command sudo apt install python3-pip
3. Installing docker https://docs.docker.com/compose/install/#install-compose 

### Installing

A step by step series of examples that tell you how to get a development env running

```
1. Initialize using command virtualenv -p python3 env
2. Activate virtualenv using source env/bin/activate
3. Make sure pip version is pip >=18 by running pip --version. If it's not, run pip install --upgrade pip. Make sure that you aleady install docker-compose so that the web service can be run
4. Change directory to project folder and run pip install -r requirements.txt
5. Change .env file and adjust it with local configuration
6. Run docker-compose up

```

## Running the tests

```
1. API can be access through the POSTMEAN or INSOMNIA.
2. If the configuration right it will be process to database.
3. The list url can be seen through urls.py

```

### Break down into end to end tests

```
-
```

## Built With

* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used
* [Pip](https://pypi.org/project/Django/) - Dependency Management
