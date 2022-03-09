# cookiwoo-api

## Commands

### Create superuser

```
docker-compose run app sh -c "python manage.py createsuperuser"
```

### Create migration files

```
docker-compose run app sh -c "python manage.py makemigrations --name=migration_name"
```

### Migrate tables

```
docker-compose run app sh -c "python manage.py migrate"
```

### Run tests and flake8

```
docker-compose run app sh -c "python manage.py test && flake8" 
```