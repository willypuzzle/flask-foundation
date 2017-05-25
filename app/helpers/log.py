from logging.handlers import TimedRotatingFileHandler
import logging
import os
import app.helpers.fs as fs
import json
import datetime
import app.helpers.object as object
import inspect
import traceback

_loggers = dict();

def _defineLogger(name, file, level):
    _info_logger = logging.getLogger(name)
    _info_logger.setLevel(level)

    path = _setupLogDirectory() + os.path.sep + file
    handler = TimedRotatingFileHandler(path, when="d", interval=1, backupCount=15)

    _info_logger.addHandler(handler)

    return _info_logger

def _setupLogDirectory():

    dir = fs.createApplicationDirectory('logs')

    return dir


def _log(input_p, name, file, level, print_stack_information = True):
    global _loggers
    if _loggers.get(name, None) == None:
        _loggers[name] = _defineLogger(name, file, level)

    if(print_stack_information):
        frame = inspect.currentframe()
        stack_trace = traceback.format_stack(frame)
        try:
            stack_information = '(' + stack_trace[-3][:-1] + '  ): '
        except IndexError:
            stack_information = '( Stack information not available )'
    else:
        stack_information = ''

    if isinstance(input_p, dict):
        input_p = json.dumps(input_p, skipkeys=True, default=lambda *args: '*Not serializable field*')
    else:
        if object.is_method(input_p, '__repr__'):
            input_p = input_p.__repr__()
        elif object.is_method(input_p, '__str__'):
            input_p = input_p.__str__()
        else:
            input_p = 'Object of ' + input_p.__class__.__name__ + ' class is not stringifable, I cannot log it'
    output_string = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + ': ' + stack_information + input_p
    if level == logging.INFO:
        _loggers[name].info(output_string)
    elif level == logging.WARNING:
        _loggers[name].warning(output_string)
    elif level == logging.ERROR:
        _loggers[name].error(output_string)

def info(input_p, print_stack_information = True):
    _log(input_p, name='Info', file='info.log', level=logging.INFO, print_stack_information=print_stack_information)

def error(input_p, print_stack_information = True):
    _log(input_p, name='Error', file='errors.log', level=logging.ERROR, print_stack_information=print_stack_information)

def warning(input_p, print_stack_information = True):
    _log(input_p, name='Warning', file='warning.log', level=logging.WARNING, print_stack_information=print_stack_information)