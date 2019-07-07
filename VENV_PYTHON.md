
## virtualenv

### Configuration file

nano ~/.virtualenv/virtualenv.ini

```sh

# first step using two commands
# create virtual env inside a pwd path
virtualenv env
# use one python version
virtualenv --python=/usr/bin/python3 env

# first step using only one command
python3 -m venv env

# second step
# to activate the virtual env
source env/bin/activate

# to leave
deactivate

```

## To run using gunicorn use:

Pay atention, do not use the eventlet worker class "-k eventlet". It's break the connection before the response was sent to client.

```sh
gunicorn -w 1 -b 127.0.0.1:5000 wsgi:app

# this will start in port: 8000
gunicorn -w 1 wsgi:app
```