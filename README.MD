## Simple WSGI framework

### Quick start
````bash
git clone https://github.com/aryabtsev/ssimple_wsgi_framework.git
pip install -r requirements.txt
````

You should configure uwsgi.ini.
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