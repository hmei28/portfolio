# Resume with django
Introducing a Django application that allows you to create a digital version of your resume. Utilizing this app can help make you stand out from the competition and increase your chances of landing your dream job.

## Pre-deploy

### collect static file
If you edit style of this project, don't forget to run this commande line:

```
python manage.py collectstatic
```

## Deploy with docker manually

### Run db pgsql

```
docker run --name pgsql -p 5455:5432 -e POSTGRES_USER=django -e POSTGRES_PASSWORD=django -e POSTGRES_DB=portfolio -d postgres
```

### Django migrate db
```
docker build -t portfolio:latest .  && docker run --rm -it  -v /home/kkroto/Documents/learning/python/django/env_portfolio:/app/portfolio/.env portfolio:latest python manage.py migrate
```

### Django add SuperUser
```
docker run --rm -it  -v /home/kkroto/Documents/learning/python/django/env_portfolio:/app/portfolio/.env -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=admin -e DJANGO_SUPERUSER_EMAIL=admin@local.fr portfolio:latest python manage.py managesuperuser
```

### Django Run
```
docker run --rm -it  -v /home/kkroto/Documents/learning/python/django/env_portfolio:/app/portfolio/.env -p 8000:8000 portfolio:latest gunicorn --bind 0.0.0.0:8000 portfolio.wsgi
```

