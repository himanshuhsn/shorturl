### How to setup the project?
1. Clone the project.
1. Set up the `virtualenv` for the project.
    1. `pip3 install virtualenv`
    1. `virtualenv venv`
    1. `source venv/bin/activate`
1. Install the requirements
    1. `pip3 install -r requirements.txt`
1. Run the project
    1. `FLASK_APP=./src/shorturl/run.py FLASK_DEBUG=1 flask run`
1. Access the swagger-ui at following url.
    - `http://127.0.0.1:5000/v1/ui`