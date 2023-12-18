# Django-GraphQL (Test Task)

This is a test task for Django-GraphQL.

## Local Deploy

1. **Create Virtual Environment and Activate It:**
```bash
   python -m venv venv
   source venv/bin/activate
```
2. **Install requirements**
```commandline
pip install -r requirements.txt
```
3. **Make and run migrations**
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
4. **Run fixtures**
```commandline
python manage.py loaddata fixtures/users.json
```

```commandline
python manage.py loaddata shop/fixtures/shops.json
```

```commandline
python manage.py loaddata shop/fixtures/categories.json
```

```commandline
python manage.py loaddata shop/fixtures/products.json
```
5. **Run server**
```commandline
python manage.py runserver
```

---

### Django admin creds:
  - username: admin
  - password: admin
