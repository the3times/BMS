##图书管理系统(BMS)
####建表
```python
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=32, verbose_name='书名')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish_date = models.DateField(auto_now_add=True, verbose_name='出版日期')
    publish = models.ForeignKey(to='Publish', verbose_name='出版社')
    authors = models.ManyToManyField(to='Author',
                                     through='Book2Author',
                                     through_fields=['book', 'author'])


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    phone = models.BigIntegerField()
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender_choices = (
        (0, '女'),
        (1, '男'),
        (2, '保密')
    )
    gender = models.IntegerField(choices=gender_choices, verbose_name='性别')
    info = models.TextField(verbose_name='作者简介')

    def __str__(self):
        return f'{self.name}'


class Book2Author(models.Model):
    book = models.ForeignKey(to='Book')
    author = models.ForeignKey(to='Author')
```