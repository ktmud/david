start: dpyc
	@python app.py

gunicorn:
	@gunicorn app:app --debug --bind localhost:5000 --error-logfile '-'

dpyc:
	@find "`pwd`" \( -name '*.pyc' -o -name '*.ptlc' \) -type f -delete

venv:
	@virtualenv venv

init_db:
	@python tools/init_db.py

fillup: init_db
	@python tools/add_test_data.py

g:
	@export DEBUG="" && cd david/static && grunt watch

pip:
	@pip install -r requirements.txt


npm: 
	@cd david/static && npm install

static: npm
	@cd david/static && grunt build

init: venv pip fillup static

