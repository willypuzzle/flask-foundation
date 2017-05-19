#! ../env/bin/python

from flask import Flask
from flask_dotenv import DotEnv
from webassets.loaders import PythonLoader as PythonAssetsLoader

from app import assets
import app.modules as modules
import os
import app.helpers.fs as fs
import app.helpers.log as log


from app.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager
)


def create_app():
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    """

    app = Flask(__name__)

    #app.config.from_object(object_name)
    env = DotEnv();
    env.init_app(app=app, env_file=fs.getApplicationDirectory() + os.path.sep + '.env')

    for k,v in app.config.items():
        if isinstance(v, str):
            v = v.lower().strip();
            if v == 'true':
                app.config[k] = True
            elif v == 'false':
                app.config[k] = False

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    login_manager.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    modules.init_app(app)

    return app
