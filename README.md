Backend webdev test project 2020-10
===
Example setup of Django web app with REST API. Includes:
- ORM setup with admin;
- customized user model with additional field;
- API interface with `django-filter` and `dj-rest-auth` enabled;
- permissions setup for data access;
- simple Docker config for development.

Running in local environment:
-
1) In project root, create `.env` file with:
`SECRET_KEY=<key>`
and optionally `DB_NAME`, `DB_USER`, `DB_PASSWORD` variables.

2) Build and run docker image:

`docker-compose build`

`docker-compose run web python manage.py migrate`

Optionally: `docker-compose run web python manage.py createsuperuser`

`docker-compose up`

3) Hence, ready to accept connections at:

`http://0.0.0.0:8000/<api_url>`

API entry points:
-
-  __/api__ - common root;
	-  __/categories__, __/companies__, __/products__ - respective lists, with other options available through certain permissions;
-  __/auth__ - auth root;
	-  __/login__, __/logout__, __/user__, __/password/reset__, __/password/reset/confirm__, __/password/change__, __/registration__ - respective actions.