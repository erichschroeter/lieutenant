# Installation

These instructions were created on an Ubuntu system.

> These instructions were based off of [this tutorial][0].

A walkthrough video of these instructions hase been created for your
convenience located at [https://www.youtube.com/watch?v=psTw2HgnNsc][10].

[![Youtube tutorial](https://img.youtube.com/vi/psTw2HgnNsc/0.jpg)](https://www.youtube.com/watch?v=psTw2HgnNsc)

## PostgreSQL

To install PostgreSQL run this command:

    $ sudo apt-get install postgresql postgresql-contrib

Create a database user:

    $ sudo su - postgres
    postgres:~$ createuser --interactive -P
    Enter name of role to add: django_lieutenant
    Enter password for new role:
    Enter it again:
    Shall the new role be a superuser? (y/n) n
    Shall the new role be allowed to create databases? (y/n) n
    Shall the new role be allowed to create more new roles? (y/n) n
    postgres:~$

Create a new database for the app and then logout of postgres user:

    postgres:~$ createdb --owner django_lieutenant lieutenant
    postgres:~$ logout

## Application user

In order to improve security we should run the web application with limited
privileges.

Create a user for the app, named _lieutenant_ and assigned to a system group
called _webapps_.

    $ sudo groupadd --system webapps
    $ sudo useradd --system --gid webapps --shell /bin/bash --home /home/lieutenant lieutenant

## Install pip

To install [pip][3] run this command:

    $ sudo apt-get install python-pip

## Install virtualenv and virtualenvwrapper

[Virtualenv][1] is a Python tool that allows you to create isolated environments
for Python applications. This allows Python applications to have different
dependencies without conflictions. [Virtualenvwrapper][2] is a Python tool that
wraps [virtualenv][1] with some helpful commands that makes life easier.

    $ sudo pip install virtualenv virtualenvwrapper

### Create and activate an environment for our app

We are going to keep as much of our web app within its own home directory. If
you prefer a different location (e.g. `/var/www/`, `/srv/`, etc) use that
instead. Create the home directory and change the owner to our application user.

    $ sudo mkdir -p /home/lieutenant/
    $ sudo chown lieutenant /home/lieutenant/

As the application user create a virtual Python environment in the new
directory.

    $ sudo su - lieutenant
    lieutenant:~$ cd /home/lieutenant/
    lieutenant:~$ . `which virtualenvwrapper.sh`
    lieutenant:~$ mkvirtualenv lieutenant

    NOTE: Virtual environments directory /home/lieutenant/.virtualenvs does not exist. Creating...
    New python executable in lieutenant/bin/python
    Installing setuptools, pip, wheel...done.
    virtualenvwrapper.user_scripts creating /home/lieutenant/.virtualenvs/lieutenant/bin/predeactivate
    virtualenvwrapper.user_scripts creating /home/lieutenant/.virtualenvs/lieutenant/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /home/lieutenant/.virtualenvs/lieutenant/bin/preactivate
    virtualenvwrapper.user_scripts creating /home/lieutenant/.virtualenvs/lieutenant/bin/postactivate
    virtualenvwrapper.user_scripts creating /home/lieutenant/.virtualenvs/lieutenant/bin/get_env_details
    (lieutenant)lieutenant:~$

## Install special dependencies

Some dependencies installed via [pip][3] need to be compiled during installion
and this section prepares those dependencies for compilation.

    lieutenant:~$ sudo apt-get install libpq-dev python-dev

Installing the dependencies above should prevent any errors while installing
dependencies using [pip][3].

# Supervisor and nginx

In production we do not use the Django single-threaded development server, but
a dedicated application server called [gunicorn][5]. Within the repo are config
files and scripts that intended for [supervisor][6] and [nginx][7].

[Supervisor][6] is a service that manages the web application process, so if
for some reason the app process crashes it will automatically be restarted.

[Nginx][7] is the web server we will use to serve the web app. We could also
use [Apache][8], however at this moment no config is provided for it.

    $ sudo apt-get install supervisor nginx

# Clone git repository

Now that we have the fundamental dependencies installed (i.e. [pip][3],
[virtualenv][1], [virtualenvwrapper][2]) we can download the lieutenant web app
and its dependencies.

    $ cd /home/lieutenant/
    $ git clone https://github.com/erichschroeter/lieutenant.git
    $ cd lieutenant/

Activate the app environment:

    $ workon lieutenant
    (lieutenant)lieutenant:~/lieutenant$ pip install -r requirements.txt
    ...
    [ downloading and installing dependencies]
    ...
    (lieutenant)lieutenant:~/lieutenant$

Create the tables in the database:

    (lieutenant)lieutenant:~/lieutenant$ cd lieutenant/
    (lieutenant)lieutenant:~/lieutenant/lieutenant$ ./manage.py migrate

# Create symlinks and start services

Create log directory:

    $ sudo mkdir -p /var/log/lieutenant/

Create symlinks to the provided config and script files in the repo:

    $ sudo ln -s /home/lieutenant/lieutenant/bin/gunicorn_start /home/lieutenant/.virtualenvs/lieutenant/bin/
    $ sudo ln -s /home/lieutenant/lieutenant/bin/postactivate /home/lieutenant/.virtualenvs/lieutenant/bin/
    $ sudo ln -s /home/lieutenant/lieutenant/bin/predeactivate /home/lieutenant/.virtualenvs/lieutenant/bin/
    $ sudo ln -s /home/lieutenant/lieutenant/etc/nginx/lieutenant.conf /etc/nginx/sites-available/lieutenant
    $ sudo ln -s /etc/nginx/sites-available/lieutenant /etc/nginx/sites-enabled/
    $ sudo ln -s /home/lieutenant/lieutenant/etc/supervisor/lieutenant.conf /etc/supervisor/conf.d/

Start the supervisor service:

    $ sudo supervisorctl reread
    $ sudo supervisorctl update
    $ sudo supervisorctl start lieutenant

Start the nginx service:

    $ sudo service nginx restart

Navigate to [http://localhost/][9] in your browser.

[0]: http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/
[1]: https://virtualenv.readthedocs.org/
[2]: https://virtualenvwrapper.readthedocs.org/
[3]: https://pip.readthedocs.org/
[4]: https://pypi.python.org/pypi/psycopg2
[5]: http://gunicorn.org/
[6]: https://pypi.python.org/pypi/supervisor
[7]: https://www.nginx.com/
[8]: https://httpd.apache.org/
[9]: http://localhost/
[10]: https://www.youtube.com/watch?v=psTw2HgnNsc
