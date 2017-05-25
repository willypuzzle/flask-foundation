def _user_logged_in(sender, **kwargs):
    import app.helpers.log as log
    try:
        user = kwargs['user']
        from flask import g
        g.user = user
    except KeyError:
        log.error("No user found, API changed or bug in library")

def init_app(app):
    from flask_login import signals
    signals.user_logged_in.connect(_user_logged_in)
