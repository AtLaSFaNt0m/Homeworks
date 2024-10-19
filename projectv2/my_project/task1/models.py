from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)  # имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # баланс
    age = models.PositiveIntegerField()  # возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)  # название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # размер файлов игры
    description = models.TextField()  # описание
    age_limited = models.BooleanField(default=False)  # ограничение возраста
    buyers = models.ManyToManyField(Buyer, related_name='games')  # покупатели

    def __str__(self):
        return self.title
