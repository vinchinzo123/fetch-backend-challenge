## Table of contents
* [Project info](#project-info)
* [Requirements and Installation](#requirements-and-installation)
* [Getting Started](#getting-started)
* [Thank You](#thank-you)

## Project Info
fetch-coding-challenge is the fulfillment of the backend job application presented in [Fetch Rewards's](https://www.fetchrewards.com/) backend [coding challenge](https://fetch-hiring.s3.us-east-1.amazonaws.com/points.pdf). As per the challenge expectations I have provided routes that:
  - Add points to user account for specific payer and date
  - Deduct points from the user account using above constraints and return a list of [payer, points deducted] for each call to spend points
  - Return point balance per user that would list all positive points per payer

## Requirements and Installation
  - Python 3.9
  - Django
  - Django Rest Framework
[*Instructions for installing pipenv and virutal environments found here*](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) And below:

Ensure you have Python 3.9 available and that you can acess it from your command line. Check with the command:

```
$ python --version
```

If you get something like ```3.9.0``` great! If not follow install python 3.9.0 from [python.org](python.org) or check out *The Hitchhikers Guide to Python* section [Installing Python](http://docs.python-guide.org/en/latest/starting/installation/)

Please make sure you have pip available too. Check with the command:
```
$ pip --version
$ pip 20.2.4
```

If you installed Python from source, with an installer from python.org, via Homebrew or via Linuxbrew you should already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip separately.

Once you have pip, continue to install Pipenv:

```
$ pip install --user pipenv
```

Confirm pipenv is installed. Simply check with the command:
```
$ pipenv --version
pipenv, version 2020.11.15
```

Now that python and pipenv are available we can run the web service.

## Getting Started
Follow the commands to clone the repository and change into the project directory.
```
$ git clone git@github.com:vinchinzo123/fetch-backend-challenge.git
$ cd fetch-coding-challenge
```

Create a python virtual environment with needed dependencies from the Pipfile by running the command:

```
$ pipenv install
```

Enter your virtual environment with:

```$ pipenv shell```

When working with Django and there changes to our model or our database is not created we need to run the command:

  ```
  $ python manage.py makemigrations
  ```
to let django know we have made changes.

To create the model tables for our database simply run the command

  ```
  $ python manage.py migrate
  ```

Finally we can start the server by running the command:

  ```
  python manage.py runserver
  ```

Now that the server is up and running we can start sending data to the server.

Following the challenge example we will start by adding points to the payers accounts.

We will be sending a POST request with JSON data to the route: 

- http://127.0.0.1:8000/add-points/

The POST request's body must be in JSON format
EXAMPLE:

       {
         "payer": "DANNON", "points": 1000, "date" : "11/2 2PM"
        }

This post structure is based on the example given in the coding challenge: 

```add [DANNON, 1000 points 11/2 2PM] to user```

When we are ready to deduct points from the account we will be sending
a PUT request with JSON data to the route: 
  - http://127.0.0.1:8000/remove-points/

The PUT request's body must be in JSON format
EXAMPLE:

       {
         "points": 100
        }

This PUT structure is based on the example given in the coding challenge
  - deduct 5000 points from user

Once the PUT call is made you will get a response in JSON format
EXAMPLE:

        {
            "response": {
                "0": {
                    "payer": "DANNON",
                    "points": -100,
                    "date": "01/10 04:11 PM"
                }
            }
        }

  **NOTE "01/10 04:11 PM" represents time when PUT call was placed**

Lastly, a GET request to the route: 
- http://127.0.0.1:8000/balances/

returns a response in JSON format
EXAMPLE:

        {
            "balances": {
                "0": {
                    "payer": "DANNON",
                    "points": 900
                }
            }
        }

## Thank You
To anyone who viewed this webservice, Thank you.

I am a devloper who loves to solve problems, to grow.

I'd love to head from you!
Email me @ vnewsom90@gmail.com. 
