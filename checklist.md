# Check list for building application
## Setup developpements environment
1. mkdir affluents
2. virtualenv venv -p python3
3. source ./venv/bin/activate
3. mkdir code
4. cd code
5. git init
6. git remote add origin https://github.com/edgardeloire/affluents.git
7. git pull https://github.com/edgardeloire/affluents.git
8. pip freeze > requirements.txt
9. update .gitignore

11. create run.py for test
12. assign FLASK_APP

## Application setup and parameter configuration
1. create config.py file


## environment variable
| Name                  |  Values                                 | Explaination          |
|-----------------------|-----------------------------------------|-----------------------|
|  FLASK_ENV            |   DevelopmentConfig  or TestConfig      |                       |
|  SECRET_KEY           |   textkey or random                     |                       |
|  FLASK_APP            |   run.py                                |                       |
