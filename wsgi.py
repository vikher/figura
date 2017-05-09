# -*- coding utf-8 -*-
#!/usr/bin/python
import config
from server import app as application
application.secret_key = config.api.get('secret', 'SECRETK3Yzz')
if __name__ == "__main__":
    application.run()
