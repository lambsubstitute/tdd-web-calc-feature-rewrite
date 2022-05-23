[![Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg)](COPYING)

TDD Web Calculator
==================

🏫 For educational purposes 🏫

![Picture of the TDD Web Calculator skeleton](images/tdd-web-calc-skeleton.png){width="400px"}

This repo provides a skeleton web application of a calculator. Each
button press will combine into a command that gets sent to the backen
Python app when a operator button is pressed (i.e. C,%,+,-,/,x,=).

**Your challenge is to add the functionality to get this calculator
working.**

All development of the app should use test driven development (TDD)
techniques.

This readme will guide you through setting up your dev environment,
running locally, writing and running tests, and deploying into AWS.

Getting Started
---------------

To start coding you will need a few basics setup first

### Development Environment

You will need the following:

[Please follow the official docs for each pre-req as required on how to
install for your environment.]{.title-ref}

-   [VSCode](https://code.visualstudio.com/) installed (or another IDE
    of your choosing)
-   [Python](https://www.python.org/downloads)
-   [Git](https://git-scm.com/download)

We then need some additional packages required for this app.

Create a virtual Env to isolate requirements for Python :

    pip install virtualenvwrapper
    mkvirtualenv tdd-web-calc

Install the requirements into the virtual environment :

    pip install -r requirements.txt

Running Locally
---------------

Once you have all the required components installed we can run the code
locally to help test and develop.

Navigate to the repo :

    cd tdd-web-calc

Ensure you are in the python virtual env that contains the requirements
:

    workon tdd-web-cald

Run the local server :

    python ./app/app.py

A message will show you the status of the run and a URL to see the app.

[This is run in debug mode so any changes to the app will live reload
the web application.]{.title-ref}

Note: This will not show changes to any css parameters in the html file.
See [Developing the Web page](#developing-the-web-page) for more
information on how to do this.

### Running the Tests

\# TODO: Testing, how to run, where to save

Tests are saved under the `/tests` directory

    python -m pytest

Deploying to AWS
----------------

\# TODO

Developing the Web Page
-----------------------

[For testing changes to the webapp you\'ll also need]{.title-ref}

-   [NodeJS](https://nodejs.org/en/download/)
-   [TailwindCSS CLI](https://tailwindcss.com/docs/installation)

Install the additional requirements: :

    cd tdd-web-calc
    npm install

You can now compile a new output.css stylesheet using: :

    npx tailwindcss -i .\src\input.css -o .\src\static\css\output.css --watch     <<-- For Windows
    npx tailwindcss -i ./src/input.css -o ./src/static/css/output.css --watch     <<-- For Linux/MacOS

License
-------

GNU General Public License v3.0 or later

See [COPYING](COPYING) to see the full text.
