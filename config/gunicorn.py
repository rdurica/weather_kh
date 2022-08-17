# Gunicorn production config file"""

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "config.wsgi:application"
# The granularity of Error log outputs
loglevel = "info"
# The number of worker processes for handling requests
workers = 5
# The socket to bind
bind = "0.0.0.0:8000"

# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/weatherkh.pid"

# Write access and error info to /var/log
accesslog = "/var/log/weatherkh-access.log"
errorlog = "/var/log/weatherkh-error.log"
