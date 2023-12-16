# django-graphql (test task)

## LOCAL DEPLOY

1. Create virtualenv and activate it
2. Install requirements
```commandline
pip install -r requirements.txt
```
3. Run server
```commandline
python manage.py runserver
```
4. Run fixtures
```commandline
python manage.py loaddata fixtures/users.json
```

```commandline
python manage.py loaddata shop/fixtures/shops.json
```

```commandline
python manage.py loaddata shop/fixtures/categories.json
```

- Django admin creds:
  - username: admin
  - password: admin