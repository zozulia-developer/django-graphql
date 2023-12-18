# Django-GraphQL (Test Task)

This is a test task for Django-GraphQL.

## Local Deploy

1. **Create Virtual Environment and Activate It:**
```bash
python -m venv venv
source venv/bin/activate
```
2. **Install requirements**
```bash
pip install -r requirements.txt
```
3. **Make and run migrations**
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
4. **Run fixtures**
```bash
python manage.py loaddata fixtures/users.json
```

```bash
python manage.py loaddata shop/fixtures/shops.json
```

```bash
python manage.py loaddata shop/fixtures/categories.json
```

```bash
python manage.py loaddata shop/fixtures/products.json
```
5. **Run server**
```bash
python manage.py runserver
```

---

### Django admin creds:
  - username: admin
  - password: admin
