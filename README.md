Template for Flask based webapps (mostly based on the Flask Mega-Tutorial series that begins at http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Installation
------------
# python3 -m venv flask --without-pip
# source flask/bin/activate
# ./flask_venv.sh
 
# deactivate

The sqlite database must also be created before the application can run, and the `db_create.py` script takes care of that. See the [Database tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) for the details.

Running
-------
Run run.py (or) flask/bin/gunicorn --log-file - app:app (starts on localhost:5000 or localhost:8000)

Deploying (after intalling heroku toolbelt)
---------
heroku login
heroku apps:create flask-template
heroku addons:add heroku-postgresql:dev
heroku pg:promote HEROKU_POSTGRESQL_CHARCOAL_URL
heroku config:set HEROKU=1
git push heroku master
heroku run init --app flask-template1

Celery
------
ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
celery -A app.celery worker --loglevel=info &

Curl
----
curl -i http://localhost:5000/books/1
curl -i http://localhost:5000/books?limit=10
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"D", "author":"D"}' http://localhost:5000/books
curl -i -H "Content-Type: application/json" -X PUT -d '{"title":"Darva"}' http://localhost:5000/books/11
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/books/11
