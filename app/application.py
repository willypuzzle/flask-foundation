from app import create_app

_app = None;

def create():
    global _app;
    if _app == None:
        _app = create_app()
    return _app;