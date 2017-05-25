def _initialize_models(app):
    import app.modules.models as Model

    Model.db.init_app(app)
    Model.migrate.init_app(app)

def _register_blueprints(app):
    from app.modules.auth.controllers import mod as auth_mod
    from app.modules.home.controllers import mod as home_mod

    app.register_blueprint(auth_mod)
    app.register_blueprint(home_mod)


def _register_handlers(app):
    import app.modules.handlers as handlers

    handlers.init_app(app)

def _register_signals(app):
    import app.modules.signals as signals

    signals.init_app(app)

def init_app(app):
    _initialize_models(app)
    _register_blueprints(app)
    _register_handlers(app)
    _register_signals(app)