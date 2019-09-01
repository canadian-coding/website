# website


## Local Development

### Virtual environment

A virtual environment is useful for housing your python environment to avoid version and package conflicts with your primary python install. It is however not necessary so if you do decide to not use it you can skip ahead to the Dependencies section.

#### Creating a virtual environment

You will need to install virtualenvwrapper(macOS/linux) or virtualenvwrapper-win(Windows) first. This can be done using ```pip install virtualenvwrapper(macOS/linux)/virtualenvwrapper-win(Windows)``` or ```pip3 install virtualenvwrapper(macOS/linux)/virtualenvwrapper-win(Windows)``` (if you have more than one python version installed).

After installation you can create a new virtual environment for the first time using ```mkvirtualenv <whatever name you want>```. Once created your current terminal window will be using the environment (you can tell because the environment name will showup where your path usually would be). Once inside the environment you can run ```pip install -r requirements.txt``` to grab all dependencies (this means you can skip the dependencies section). 

You can tell that this worked by running ```pip list``` you should see something like the following:

```
Package               Version
--------------------- -------
Django                2.2.4
pip                   19.2.3
pytz                  2019.2
setuptools            41.2.0
sqlparse              0.3.0
virtualenv            16.7.4
virtualenvwrapper-win 1.2.5
wheel                 0.33.6
```

#### Accessing existing virtual environment

You can access an existing virtual environment using ```workon <environment name>```

### Dependencies

All dependencies can be installed using python3's pip package manager by running:
```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt```

Alternatively you can individually install the dependencies, you will need:

(required)

- Django; High level web framework used to create the site

Optional:

- virtualenv or virtualenvwrapper(macOS/linux)/virtualenvwrapper-win(Windows); Highly recommended to segment your python environment and avoid version conflicts (See virtual environment section)

## Getting production ready

### Secret Key

Note that Django requires the use of a secret key to run. This key should be kept secret (obviously), as such I have setup this repository to **NOT** commit files called ```secretkey.txt```. If you plan to copy the source code and use it in production [generate a secret key](https://randomkeygen.com/) and put it in a ```secretkey.txt``` file in the ```/canadiancoding``` directory.

### Debug mode

Disable debug mode in ```/canadiancoding/settings.py``` before using in production.

### Allowed host

Add the necessary host domain name to ALLOWED_HOSTS in ```/canadiancoding/settings.py```.

## Running

Change directory into the canadiancoding directory ```cd /canadaiancoding``` then run ```python manage.py runserver```.
