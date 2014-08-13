Example repository that reproduces a problem with django-tagging and master of pytest_dev

To run it:

	git clone https://github.com/gandalfar/pytest-example.git

Create a new virtual env and inside:

	pip install -r requirements.txt

and run tests:

	./manage.py test

Migrations themselves work:

	./manage.py syncdb
	./manage.py migrate

		
