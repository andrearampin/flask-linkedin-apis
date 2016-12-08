# LinkedIn API Calls
This project has the aim to demostrate how to integrate Flask with the LinkedIn APIS.

In order to gain access to LinkedIn through API calls, you will need to create an applicaiton on the LinkedIn platform and get its `client_id` and `client_secret`. An application can be easily created at the following link https://www.linkedin.com/developer/apps.

## Source code
- Application: `app.py`
- Configuration: `config.ini`
- Template: `templates/`

## Installation

### Configuration
Please update `client_id` and `client_secret` in the **config.ini** file.

### Install application through `virtualenv`
Once you have cloned the project:

`$ cd flask-linkedin-apis/`

`$ chmod +x setup.sh && ./setup.sh`

`$ chmod +x activate.sh && ./activate.sh`

when the last command is given, the application will respond at the address: http://127.0.0.1:5000.

## Note
Please feel free to clone my code and turn it in anything that suits your situation. As I said, it is basic implementation but it can esasily be extended thanks to the flexibility of Flask and its libraries.

## Thanks to
- Flask: http://flask.pocoo.org/
- OAuthlib: https://github.com/requests/requests-oauthlib
