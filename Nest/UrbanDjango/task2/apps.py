from django.apps import AppConfig

INSTALLED_APPS = [
    ...,
    'task2',
]


class Task2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task2'
