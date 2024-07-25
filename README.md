Getting Started with Django API
This project serves as the backend for a React frontend, providing RESTful API services. It is hosted on PythonAnywhere.

Available Commands
In the project directory, you can run:

python manage.py runserver
Runs the Django development server.
Open http://localhost:8000 to view it in your browser.

The server will automatically reload when you make changes to the code.
You may also see any errors in the terminal.

python manage.py migrate
Applies database migrations.
Use this command to update your database schema whenever your models change.

python manage.py createsuperuser
Creates a new superuser account for accessing the Django admin interface.
Follow the prompts to set up the superuser credentials.

python manage.py collectstatic
Collects static files into the directory specified by STATIC_ROOT.
This is useful for deploying the application in production.

Note: Ensure DEBUG is set to False in production and that STATIC_ROOT is correctly configured in settings.py.

Deployment
The API is hosted on PythonAnywhere. To update the deployment:

Open a Bash console on PythonAnywhere.
Navigate to your project directory:
bash
Copy code
cd /home/your_username/your_project_directory
Pull the latest changes from the GitHub repository:
bash
Copy code
git pull origin main
Apply migrations:
bash
Copy code
python manage.py migrate
Reload the web app via the PythonAnywhere dashboard or using the command line.
For more detailed information on deployment, see the Django deployment checklist.

Learn More
You can learn more about Django and its features in the Django documentation.

To learn about the frontend framework, visit the React documentation.

REST API Design
This section has moved here: https://restfulapi.net/

Best Practices for Django Development
This section has moved here: https://docs.djangoproject.com/en/stable/misc/design-philosophies/

Handling Django Models and Databases
This section has moved here: https://docs.djangoproject.com/en/stable/topics/db/

Django Security Best Practices
This section has moved here: https://docs.djangoproject.com/en/stable/topics/security/

Troubleshooting
This section has moved here: https://docs.djangoproject.com/en/stable/faq/

