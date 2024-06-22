# Setting Up My Django Project

How to set up a Django project

## Usage

Instructions on how to use:

#### Create a virtual environment

In your terminal, run:

1.          python3 -m venv .venv

#### Activate the virtual environment

For Unix/macOS:

2.          . .venv/bin/activate


For Windows:

3.          .\.venv\Scripts\Activate

#### Install Django

4.          pip install django

#### Verify Django installation

5.          django-admin

You should see a list of available subcommands:

6.            Type 'django-admin help <subcommand>' for help on a specific subcommand.

              Available subcommands:

              [django]
              check
              compilemessages
              createcachetable
              dbshell
              diffsettings
              dumpdata
              flush
              inspectdb
              loaddata
              makemessages
              makemigrations
              migrate
              optimizemigration
              runserver
              sendtestemail
              shell
              showmigrations
              sqlflush
              sqlmigrate
              sqlsequencereset
              squashmigrations
              startapp
              startproject
              test
              testserver

#### Start a new Django project

In your terminal, run:

7.         django-admin startproject <name of file> .

- This command creates a new Django project named my_first_project.
- You will get a manage.py file and a directory named my_first_project with various configuration files.

#### Run the development server

In your terminal, run:

8.          python manage.py runserver

- This command starts the Django development server.
- You might see unapplied migration warnings; you can ignore them for now.

#### Open the server in your browser

Visit:

9.          https://127.0.0.1:8000/

- This URL points to the localhost, running on your local computer.
- If everything is set up correctly, you will see the Django welcome page indicating a successful installation.

#### Open another terminal to issue commands

- While the server is running, open another terminal to install packages or perform other tasks.
- Ensure you activate the virtual environment in the new terminal:

For Unix/macOS:

10.         . .venv/bin/activate

For Windows:

11.         .\.venv\Scripts\Activate
