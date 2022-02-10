### How to setup the project?
1. Clone the project.
1. Set up the `virtualenv` for the project.
    1. `pip3 install virtualenv`
    1. `virtualenv venv`
    1. `source venv/bin/activate`
1. Install the requirements.
    1. `pip3 install -r requirements.txt`
1. Run the project for produciton server with `gunicorn`.
    1. `cd` to the `shorturl` folder. (i.e. root folder of the project)
    1. `gunicorn --workers 4 --bind 0.0.0.0:8000 src.shorturl.run:flask_app`
1. Access the swagger-ui at following url.
    - `http://0.0.0.0:8000/v1/ui`