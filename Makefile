start: dpyc
	@python app.py

dpyc:
	@find "`pwd`/david" \( -name '*.pyc' -o -name '*.ptlc' \) -type f -delete

g:
	@cd david/static && grunt watch

pip:
	@pip install -r requirements.txt
