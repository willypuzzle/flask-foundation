def init_app(app):
    import app.modules.handlers.errors as errors;

    errors.init_app(app)