from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import config
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.secret_key = config.api.get('secret', 'SECRETK3Yzz')

# Comment the logging setup for using Heroku
# Setting up the logging
'''
handler = RotatingFileHandler(config.log.get('file', './app.log'),
                              maxBytes=config.log.get('limit', 10000),
                              backupCount=config.log.get('keep', 1))

log_format = config.log.get('format', None)
if log_format:
    handler.setFormatter(logging.Formatter(log_format))

app.logger.setLevel(config.log.get('level', 'info').upper())
app.logger.addHandler(handler)
'''
# End comments

from views import *

if __name__ == '__main__':
    ''' Running the application '''
    app.run(config.service.get('host', '127.0.0.1'),
            config.service.get('port', 5000),
            debug=True)
