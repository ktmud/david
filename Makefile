start: dpyc
	@python app.py

dpyc:
	@find "`pwd`/david" \( -name '*.pyc' -o -name '*.ptlc' \) -type f -delete

init_db:
	@python tools/init_db.py

fillup: init_db
	@python tools/add_test_data.py

g:
	@export DEBUG="" && cd david/static && grunt watch

pip:
	@pip install -r requirements.txt
