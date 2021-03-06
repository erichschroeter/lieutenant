Lieutenant is an app with the intent on providing an efficient way of tracking
anything in its users' lives. A big part of tracking something is the how easy
it is to log individual entries, and this is a major goal of Lieutenant.
Another big part is to analyze the data logged to discover trends and
hopefully learn from from the data.

![Sign up page](docs/Screenshot_signup.png)
![Entry list page](docs/Screenshot_entry_list.png)
![Entry update page](docs/Screenshot_entry_update.png)
![Entry create page](docs/Screenshot_entry_create.png)

# Instructions

These instructions provide the steps to get a development environment up and
running.

### Create a virtual environment

_**Note:** These instructions should only have to be done once._

1. `source /usr/local/bin/virtualenvwrapper.sh`
1. `mkvirtualenv lieutenant`

### Initial Setup

These instructions explain how get the development server up an running.

1. `source /usr/local/bin/virtualenvwrapper.sh`
1. `workon lieutenant`
1. `pip install -r requirements.txt`
1. `cd lieutenant/`
1. `./manage.py migrate`
1. `./manage.py runserver 0.0.0.0:8000`

After the server is running, navigate to [http://localhost:8000/entries][0] in your
browser.

[0]: http://localhost:8000/entries
