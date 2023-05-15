### What is this project about?
- This is a [url shortening](https://en.wikipedia.org/wiki/URL_shortening) service that provides a shorturl for any given longurl.
- For design documentation of the project look at [design_doc.pdf](https://github.com/himanshuhsn/shorturl/blob/master/design_doc.pdf).
- For API documentation do one of following
    - Look at [api_doc.pdf](https://github.com/himanshuhsn/shorturl/blob/master/api_doc.pdf)
    - Set up the app locally and look at `swagger-ui`

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

### Learning outcome
1. Write code by following the openAPI spec (Generated stubs from openAPI [specificaion.yml](https://github.com/himanshuhsn/shorturl/blob/master/openapi/specification.yml) file).
2. Write a basic architecture for url shortening that can easily scale on aws.
3. Various tools available on AWS for scaling the deployed service (i.e. autoscaling group, load balancer).
4. Write an application using `python` and `flask`.
