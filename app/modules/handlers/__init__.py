def init_app(app):
    import app.modules.handlers.errors as errors
    import app.modules.handlers.babel as babel
    import app.modules.handlers.request as request

    errors.init_app(app)
    babel.init_app(app)
    request.init_app(app)