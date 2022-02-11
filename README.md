# cookiwoo-api

## Commands

### Create superuser

```
docker-compose run app sh -c "python manage.py createsuperuser"
```

### Migrate tables

```
docker-compose run app sh -c "python manage.py migrate"
```

### Run tests and flake8

```
docker-compose run app sh -c "python manage.py test && flake8" 
```