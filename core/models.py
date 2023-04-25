from django.db import models


class Service(models.Model):
    name = models.CharField('Название службы', max_length=50)
    cod = models.IntegerField('Код службы')
    phone = models.IntegerField('Номер телефона')

    class Meta:
        ordering = ['cod']
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Список экс. служб'

    def __str__(self):
        return self.name


class Declarer(models.Model):
    men = 'men'
    woman = 'women'
    gender_choices = [
        (men, 'Мужчина'),
        (woman, 'Женщина')
    ]
    name = models.CharField('ФИО', max_length=50)
    age = models.DateField('Дата рождения')
    gender = models.CharField('Ваш пол', max_length=7, choices=gender_choices)
    phone = models.IntegerField('Номер телефона', blank=True, null=True)
    photo = models.ImageField('Фото', blank=True)
    health_status = models.TextField(
        'Состояние здоровья',
        blank=True,
        default='Практичеки здоров',
        help_text='Аллергоgeанамнез, хронические заболевания и т.п.'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Список заявителей'

    def __str__(self):
        return self.name


class Appeal(models.Model):
    in_work = 'В работе'
    complited = 'Завершено'
    status_choices = [
        (in_work, 'В работе'),
        (complited, 'Завершено')
    ]
    declarer = models.ForeignKey(Declarer, verbose_name='Заявитель', on_delete=models.CASCADE, related_name='appeals')
    services = models.ManyToManyField(Service, verbose_name='Службы', blank=True, related_name='appeals')
    created = models.DateField('Время обращения', auto_now_add=True)
    number = models.IntegerField('Номер обращения', db_index=True, unique=True, blank=True,)
    status = models.CharField('Статус', max_length=10, choices=status_choices, default='В работе')
    casualties = models.IntegerField('Количество пострадавших')
    dont_call = models.BooleanField('Не звонить', null=True, blank=True)

    class Meta:
        ordering = ['created', 'number']
        verbose_name = 'Обращение'
        verbose_name_plural = 'Список обращений'

    def __str__(self):
        return f'{self.number} - {self.created}'
