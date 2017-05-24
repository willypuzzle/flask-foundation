def init_app(app):
    import app.modules.handlers.errors as errors;
    import app.modules.handlers.babel as babel;

    errors.init_app(app)
    babel.init_app(app)