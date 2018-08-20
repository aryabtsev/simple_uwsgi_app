## Simple WSGI framework

### Quick start
````bash
git clone https://github.com/aryabtsev/ssimple_wsgi_framework.git
pip install -r requirements.txt
````

You should configure uwsgi.ini
````ini
[uwsgi]
http= 127.0.0.1:9090
chdir = /Users/Artem/Documents/OTUS/simple_uwsgi_app/
plugin = python, corerouter, http
processes = 4
threads = 2
stats = 127.0.0.1:9191
wsgi-file = wsgi_app.py
````

For adding some page for web-site, you have to fill the urls.yaml config file:

````yaml
url_path: ['path/to/html/template', 'Status header', 'Content-type', 'Content-type']


EXAMPLE

/ : ['templates/main_page.html', '200 OK', 'Content-Type', 'text/html']
````
### How to start
````bash
uwsgi --ini uwsgi.ini
````