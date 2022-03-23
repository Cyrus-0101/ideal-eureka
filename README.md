# Group 1 Project.

* Members:
- Maureen
- Breezy
- Cyrus

* A databse app that uses Python Django to communicate with the Database over secure transactions. We will use this app, to communicate with our frontend which is a React application. Since we will need JavaScript to make our work easier, when getting information from the Backend and Database, React is a UI library that compiles to HTML, CSS and JS when run.

* The reason our group decided to follow th

* [React](https://reactjs.org), is a User Interface JavaScript Library.

* [Docker](https://www.docker.com/), is a Platform as a Service products that use OS-level virtualization to deliver software in packages called containers. [Docker](https://www.docker.com/), needs to be installed in your machine before proceeding. We will use Docker to containerize our PostgreSQL and can be replicated over servers on the internet. After cloning the repo from GitHub you will see a docker-compose.yml file which contains configurations to run our Database and Database Manager, pgAdmin4. 

## Getting Started - (Windows)


```sh

# Clone Repo to machine
git clone 

# Navigate to project
cd group1

# Ensure virtualenv is installed globally
pip install virtualenv

# Create your virtual environment (Linux).
virtualenv my_env

# Activate your virtual environment.
my_env/bin/activate

# Deactivate virtual environment
deactivate

# Install requirements in the requirements.txt file.
pip install -r requirements.txt

# If you make changes and add dependencies to the app freeze requirements
pip freeze > requirements.txt

# Bring up the database
docker-compose up

# After starting the Database and Manager, with confirmation from the logs we should be
# able to open our database and create our needed tables before migrating the created models,
# to the database.
# Open localhost:5050 and enter the credentials provided in the docker-compose pgadmin4 environment
# configs. This will log you in to the admin and then will need you to enter the IP  

# Create a superuser
python3 manage.py createsuperuser

# Makemigrations tells the database our models have changed.
python3 manage.py makemigrations

# Migrate implements the changes to the DB.
python3 manage.py migrate

# Run the server.
python3 manage.py runserver

# Optional testing scripts.
coverage run --omit='*/my_env/*' manage.py test

# Generate a test code coverage report in html.
coverage html

```

## Getting Started - (Linux)

```sh

# Set up your virtual environment.
python3 -m venv my_env

# Activate your virtual environment.
source my_env/bin/activate

# Install requirements in the requirements.txt file.
pip install -r requirements.txt

# Create a superuser
python3 manage.py createsuperuser

# Run the server.
python3 manage.py runserver

# Optional testing scripts.
coverage run --omit='*/my_env/*' manage.py test

# Generate a test code coverage report in html.
coverage html

```