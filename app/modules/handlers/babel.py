from flask_babel import Babel, refresh as babel_cache_refresh

_babel = None


def init_app(app):
    global _babel
    _babel = Babel(app)

    @_babel.localeselector
    def get_locale():
        from flask import g, request
        # if a user is logged in, use the locale from the user settings
        user = getattr(g, 'user', None)
        if user is not None and hasattr(user, 'locale') and user.locale is not None and user.locale.strip() != '':
            return user.locale
        # otherwise try to guess the language from the user accept
        # header the browser transmits.  We support de/fr/en in this
        # example.  The best match wins.
        return request.accept_languages.best_match(['en'])

    @_babel.timezoneselector
    def get_timezone():
        from flask import g
        user = getattr(g, 'user', None)
        if user is not None and hasattr(user, 'timezone') and user.timezone is not None and user.timezone.strip() != '':
            return user.timezone


def refresh():
    babel_cache_refresh()