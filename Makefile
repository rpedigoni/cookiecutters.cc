app:
	cd django/cookiecutters/ && cookiecutter https://github.com/rpedigoni/cookiecutter-django-app

test:
	coverage run --branch --source=django/cookiecutters  django/cookiecutters/./manage.py test django/cookiecutters/ -v 2 --failfast --settings=settings.test
	coverage report --omit=django/cookiecutters/*/migrations*,django/cookiecutters/settings/*,django/cookiecutters/urls.py,django/cookiecutters/wsgi.py,django/cookiecutters/manage.py,django/cookiecutters/*/tests/*,django/cookiecutters/__init__.py

html:
	coverage html --omit=django/cookiecutters/*/migrations*,django/cookiecutters/settings/*,django/cookiecutters/urls.py,django/cookiecutters/wsgi.py,django/cookiecutters/manage.py,django/cookiecutters/*/tests/*,django/cookiecutters/__init__.py
	open htmlcov/index.html

doc:
	$(MAKE) -C docs/ html
	open docs/build/html/index.html

deploy:
	fab -f django/fabfile.py deploy

clean:
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/