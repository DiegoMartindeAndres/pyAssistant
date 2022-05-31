import datetime
import os
import constants

pwd = constants.attributes['pwd']


def log(origin_class, method, log_text):
    log_command = 'echo ' + '\'' + str(datetime.datetime.now()) + ' CLASS: ' + origin_class + ', '+ 'METHOD: ' \
                        + method + ' LOG: ' + log_text + '\'' + \
                  ' >> ' + pwd + 'logs/logs.txt'
    os.system(log_command)


def exception(origin_class, method, exception_text):
    exception_command = 'echo ' + '\'' + str(datetime.datetime.now()) + ' CLASS: ' + origin_class + ', '+ 'METHOD: ' \
                        + method + ' EXCEPTION: '   + exception_text + '\'' + \
                        ' >> ' + pwd + 'logs/exceptions.txt'
    os.system(exception_command)