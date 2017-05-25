class NoUserIdStoredInSession(Exception):
    pass

def set_user_id(id):
    from flask import session

    session['user_id'] = id


def get_user_id(throw_exception=True):
    from flask import session

    try:
        return session['user_id']
    except KeyError:
        if not throw_exception:
            return None
        else:
            raise NoUserIdStoredInSession