# PyLadies Advent

## Description

This is the code for the PyLadies advent, a Twitter bot that posts a resource everyday during December.

## Local setup

### Create virtual environment on the project root folder

```sh
python3.9 -m venv venv
```

#### Activate virtual environment

```sh
venv\Scripts\activate
# or on linux
source venv/bin/activate
```

#### Intall Requirements

```sh
# after activating the virtual env
pip install -r requirements.txt
```

#### Deactivate virtual environment

```sh
deactivate
```

### Handling secrets and environment variables

Copy the `.env.template` file and rename it to `.env` add your secrets here. These values will then be loaded as environment variables and used to create a config object in the config package.

### Linting

This project is linted using both [Black](https://pypi.org/project/black/) and [Pycodestyle](https://pypi.org/project/pycodestyle/). Both can be installed locally and ran with the following commands.

```sh
black .
pycodestyle .
```

Use [autopep8](https://pypi.org/project/autopep8/) to automatically lint the code.

```sh
autopep8 --in-place --aggressive --aggressive .\script_name.py
```

Configuration for pycodestyle can be found in the `./setup.cfg` file. The linters will also run as github actions when code is pushed to Github.


