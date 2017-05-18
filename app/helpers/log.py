from logging.handlers import TimedRotatingFileHandler
import logging
import os
import app.helpers.fs as fs
import json
import datetime
import app.helpers.object as object

_infoLogger = None

def _defineInfoLogger():
    _info_logger = logging.getLogger("Info")
    _info_logger.setLevel(logging.INFO)

    path = _setupLogDirectory() + os.path.sep + 'info.log'
    handler = TimedRotatingFileHandler(path, when="d", interval=1, backupCount=15)

    _info_logger.addHandler(handler);

    return _info_logger;

def _setupLogDirectory():

    dir = fs.createApplicationDirectory('logs');

    return dir;

def info(input_p):
    global _infoLogger
    if _infoLogger == None:
        _infoLogger = _defineInfoLogger()
    if isinstance(input_p, dict):
        input_p = json.dumps(input_p, skipkeys=True, default=lambda *args: '*Not serializable field*')
    else:
        if object.is_method(input_p, '__str__'):
            input_p = input_p.__str__()
        else:
            input_p = 'Object of ' + input_p.__class__.__name__ + ' class is not stringifable, I cannot log it';
    output_string = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ': ' + input_p;
    _infoLogger.info(output_string)