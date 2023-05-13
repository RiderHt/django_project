from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=73, verbose_name="Имя:")
    age = models.IntegerField(verbose_name="Возраст:")
    email = models.EmailField(verbose_name="Email:")
    poll = [
        ('n', ' мужской'),
        ('n', ' женский')
    ]
    poll = models.CharField(choices=poll, max_length=1, verbose_name="Ваш пол")
    password = models.CharField(max_length=70, verbose_name='Password', default='12345')
    def __str__(self):
        return self.name

class Addres(models.Model):
    region = models.CharField(max_length=30, verbose_name= "Регион:")
    town = models.CharField(max_length=15, verbose_name= "Город:")
    street = models.CharField(max_length=10, verbose_name= "Улица:")
    house = models.IntegerField(max_length=10, verbose_name= "Номер дома:")

class Work(models.Model):
    plase_of_work = models.CharField(max_length=30, verbose_name="Место работы:")
    adress_of_work = models.IntegerField(max_length=20, verbose_name= "Адрес работы:")
    education = [
        ('n', ' Среднее профессиональное'),
        ('a', ' Бакалавриат'),
        ('t', ' Специалитет, магистратура'),
        ('e', ' Подготовка кадров высшей квалификации')
    ]
    education = models.CharField(choices=education, max_length=1, verbose_name="Образование:")

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    text = models.TextField(verbose_name='Текст статьи')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='images/news', verbose_name='Картинка', default='1.jpg')

    def __str__(self):
        return self.title
# Create your models here.
