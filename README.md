# Cookiwoo API

Cookiwoo API gives us the ability to manage our favorite recipes.

## Up and running

In this section you will learn how to up and running this project on your machine.

### Docker

The Cookiwoo API has been Dockerized. 

1. Copy `./.env.example file` as `./.env` file and set variables
2. Run `docker-compose build` to build the Docker container
3. Run `docker-compose up`

### Admin panel

1. Run `docker-compose run app sh -c "python manage.py createsuperuser"` to create superuser
2. Go to http://127.0.0.1:8000/admin and use credentials for the superuser

## Commands

### Create superuser

```
docker-compose run app sh -c "python manage.py createsuperuser"
```

### Create migration files

```
docker-compose run app sh -c "python manage.py makemigrations core --name='migration_name'"
```

### Migrate tables

```
docker-compose run app sh -c "python manage.py migrate"
```

### Run tests and flake8

```
docker-compose run app sh -c "python manage.py test && flake8" 
```

### Show urls

```
docker-compose run app sh -c "python manage.py show_urls"
```
