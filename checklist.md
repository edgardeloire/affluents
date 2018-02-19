# Check list for building application
## Setup developpements environment

```

mkdir affluents
virtualenv venv -p python3
source ./venv/bin/activate
mkdir code
cd code
git init
git remote add origin https://github.com/edgardeloire/affluents.git
git pull https://github.com/edgardeloire/affluents.git
pip freeze > requirements.txt

```
update .gitignore

## Application structure

```affluents
└── affluents
    ├── venv
    └── code
          └── app
              ├── models
              ├── templates
              ├── utils
              └── test
```

11. create run.py for test
12. assign FLASK_APP

## Application setup and parameter configuration
1. create config.py file
2. utilisation du module flask-environment
3. affectation variable FLASK_ENV

## Logging
1. Creation module logmanager
2. paramétrage de la destination avec  variables : FILE_LOGGING et MAIL_LOGGING


## environment variable
| Name                  |  Values                                 | Explaination          |
|-----------------------|-----------------------------------------|-----------------------|
|  FLASK_ENV            |   DevelopmentConfig  or TestConfig      |                       |
|  SECRET_KEY           |   textkey or random                     |                       |
|  FLASK_APP            |   run.py                                |                       |
