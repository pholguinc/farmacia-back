# Farmacia Backend

This project is a simple backend to optimize the sales process in a pharmacy, drugstore, etc. in the health sector. The project structure is made so that it can be scalable, therefore it is based on the hexagonal architecture.

## Requeriments
Use the package manager [pip](https://pip.pypa.io/en/stable/) to make use of packages in Django.

## Virtual Environment

We need to create and activate our virtual environment to make use of the Python environment. 
To do this, we do the following:

#### En Linux/macOS

```bash
venv\Scripts\activate
```
### En Windows

```bash
venv\Scripts\activate
```

## Installation

To install the necessary packages of the project we need to install the packages that are already defined in the requirements.txt file

And to install it we execute the following command

```bash
pip install -r requirements.txt
```

## Database

For the database, postgreSQL is being used with docker, which is already defined in the docker-compose.yaml file, and we execute the following command

```bash
docker-compose up
```

## Run Migrations

To run the migrations that will allow us to create the database tables, we execute the following

First we check the available migrations with the command:

```bash
python manage.py makemigrations 
```
And then we run the migrations to generate our database tables


```bash
python manage.py migrate
```

## Run API

To finally run our Django API server run the following command:

```bash
python manage.py runserver
```
