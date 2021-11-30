# PyLadies Advent

## Description

This is the code for the PyLadies advent, a Twitter bot that posts a resource everyday during December.

## Local setup

This project has been written using Python 3.9, the easiest way to run it locally is to create a virtual env using [venv](https://docs.python.org/3/library/venv.html) and run all the commands within the virtual environment.

### Create virtual environment

```sh
python3.9 -m venv venv
```

#### Activate virtual environment

```sh
venv\Scripts\activate
# or on linux
source venv/bin/activate
```

#### Deactivate virtual environment

```sh
deactivate
```

### Intall Requirements

```sh
# after activating the virtual env
pip install -r requirements.txt
```

### Handling secrets and environment variables

Copy the `.env.template` file and rename it to `.env` add your secrets here. These values will then be loaded as environment variables and used to create a config object in the config package.

### Running locally

```sh
python src/main.py
```

## Linting

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

## Deployment

This github repo is connected to the PyLadies Berlin Heroku account, new versions are automatically deployed from the `main` branch when code is pushed there. The [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler) runs the code once per day.

## Creative Commons License
This project is under the [MIT](./LINCENSE) creative commons license. It's code has been influenced, inspired and in parts taken from the project [Named After Men](https://github.com/TaiLinhares/named-after-men) by [Tai Linhares](https://github.com/TaiLinhares).