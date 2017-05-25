from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
import app.helpers.log as log
import app.helpers.session as session

def init_app(app):

    @app.before_request
    def set_session_stuff_in_g():
        try:
            from app.modules.auth.models import User
            userId = session.get_user_id(True)
            user = User.get_by_primary_key(userId)
            from flask import g
            g.user = user
        except session.NoUserIdStoredInSession:
            pass
        except MultipleResultsFound:
            log.error(User.__name__ + " with id " + userId + " stored in session was found multiple times in database", True)
        except NoResultFound:
            log.warning(User.__name__ + " with id " + userId + " stored in session was not found in database", True)