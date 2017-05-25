def init_app(app):

    import app.modules.signals.login as login
    login.init_app(app)