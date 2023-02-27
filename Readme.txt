README File for Contact Us Project
This project allows users to contact you through a web form, with the messages submitted being stored in a MySQL database.

Technologies Used
The following technologies have been used in this project:

HTML
CSS
JavaScript
Bootstrap
Python
Django
MySQL
Requirements
Before running this project, you will need to have the following installed on your machine:

Python
Django
MySQL
Installation
Clone the repository to your local machine using the command:

git clone https://github.com/your-username/contact-us.git

Create a virtual environment in the project directory using the command:

python -m venv env

Activate the virtual environment using the command:

source env/bin/activate

Install the required packages using the command:

pip install -r requirements.txt

Create a MySQL database and configure the database settings in the settings.py file.

Run the following commands to create the database tables and start the Django development server:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Usage
To use the Contact Us form, go to the URL of your Django development server (e.g. http://localhost:8000/contact-us/).

Fill in the form fields and click on the "Submit" button. The message will be stored in the MySQL database and an email notification will be sent to the specified email address.

Credits
This project was created by Gokul.C.
