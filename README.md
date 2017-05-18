# Flask Foundation 

This is a Flask foundation scaffolding to help building Flask python application. It is based on [Flask Foundation](https://github.com/JackStouffer/Flask-Foundation) but modified.

It has:
* .env file support
* wsgi support
* some helper
* Support for migrations see [Flask-Migrate](https://flask-migrate.readthedocs.io/en/)

In order to use this scaffolding set the .env file (you can copy one of examples)

Use make env or make env-light to setup the enviroment.
Use manage.wsgi in order as entry point for wsgi applications.
When you develop your application you can use flask run to start the development server (after you started env/bin/activate see [here](http://flask.pocoo.org/docs/0.12/installation/#virtualenv) for better explanation).

## License

Flask foundation is licensed under the BSD license. For more info see LICENSE.md

