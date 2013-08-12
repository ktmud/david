start: dpyc
	@python app.py

dpyc:
	@find "`pwd`/david" \( -name '*.pyc' -o -name '*.ptlc' \) -type f -delete

init_user:
	@python tools/init_db.py

g:
	@cd david/static && grunt watch

pip:
	@pip install -r requirements.txt
