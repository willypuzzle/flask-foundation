def initialize_models(app):
    import app.modules.models as Model

    Model.db.init_app(app)
    Model.migrate.init_app(app)

def register_blueprints(app):
    from app.modules.auth.controllers import mod as auth_mod
    from app.modules.home.controllers import mod as home_mod

    app.register_blueprint(auth_mod)
    app.register_blueprint(home_mod)

def init_app(app):
    initialize_models(app)
    register_blueprints(app)