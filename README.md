# Flask Foundation 

This is a Flask foundation scaffolding to help building Flask python application. It is based on [Flask Foundation](https://github.com/JackStouffer/Flask-Foundation) but modified.

It has:
* .env file support (It loads everything there is in .env file in app.config)
* wsgi support
* some helper (with log helper)
* Support for migrations see [Flask-Migrate](https://flask-migrate.readthedocs.io/en/)

In order to use this scaffolding set the .env file (you can copy one of examples)

* Use make env or make env-light to setup the enviroment.
* Use manage.wsgi in order as entry point for wsgi applications. (Note: wsgi file is configured for python3.5, add or modify the path in the file in order to use other versions of python)
* When you develop your application you can use flask run to start the development server (after you started env/bin/activate see [here](http://flask.pocoo.org/docs/0.12/installation/#virtualenv) for better explanation).

## License

Flask foundation is licensed under the BSD license. For more info see LICENSE.md

