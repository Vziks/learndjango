Django
========================

### Installs

pip install -r requirements.txt

### Doc

1) Run server

$ python manage.py runserver 8080

2) Статичние файлы

$ python manage.py collectstatic

#### Dump all static file here to this folder

#### Example
STATIC_ROOT = '/home/user/prodhub/django/app/collectstatic'

#### Example
STATICFILES_DIRS = [
    #collect all file form "static" folders in project
    os.path.join(BASE_DIR, "static"),
]

3) Миграции

Создание
$ python manage.py makemigrations
Миграция
$ python manage.py migrate

4) Создание админа

$ python manage.py createsuperuser

