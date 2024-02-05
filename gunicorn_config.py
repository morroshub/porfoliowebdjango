command = '/var/www/porfoliowebdjango/venv/bin/gunicorn'
pythonpath = '/var/www/porfoliowebdjango/venv/bin/python'
bind = '192.168.1.41:8000' #ifconfig 
workers = 3
worker_class = 'sync'  # Use Gunicorn's synchronous worker
app_module = 'firstdjango.wsgi:application'  # Specify your WSGI application module here
