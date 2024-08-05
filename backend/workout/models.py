from django.utils import timezone
import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
from .service import get_path_for_avatar_for_trainer
from django_ckeditor_5.fields import CKEditor5Field

User = get_user_model()


class Rate(models.Model):
    ''' 
    Цены индивидульных тренировок
    '''

    title = models.CharField('Название тарифа', max_length=100)
    count_minutes = models.SmallIntegerField(
        'Количество минут', blank=True, null=True)
    price = models.DecimalField(
        'Цена', max_digits=10, decimal_places=2, default=1000)
    description = models.TextField('Описание тарифа', blank=True)

    class Meta:
        verbose_name = 'Тариф тренера'
        verbose_name_plural = 'Тарифы тренеров'
        ordering = ['-price']

    def __str__(self):
        return f'Индивидуальное занятие на {self.count_minutes} минут - тариф {self.title}'


class Trainer(models.Model):
    ''' 
    Тренер 
    '''

    POSITIONS = [
        ('fitness', 'Инструктор тренажерного зала'),
        ('pool', 'Инструктор бассейна'),
        ('yoga', 'Инструктор йоги'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField('Должность', max_length=100, choices=POSITIONS)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Телефон', max_length=11, unique=True)
    avatar = models.ImageField('Аватар',
                               upload_to=get_path_for_avatar_for_trainer,
                               default='trainers/trainer.jpg', blank=True)
    bio = models.TextField('Биография', blank=True)

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.get_position_display()}'

    # @property
    # def total_rating(self):
    #     try:
    #         total = round(self.ratings.aggregate(models.Sum('star__value'))[
    #                       'star__value__sum'] / self.ratings.count(), 2)
    #     except:
    #         total = 0
    #     return total


class RatingStar(models.Model):
    """
    Звезда рейтинга
    """
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["value"]


class Reviews(models.Model):
    """
    Отзывы
    """
    user = models.ForeignKey(
        User,  on_delete=models.SET_NULL, null=True, verbose_name="пользователь", related_name="user_reviews")
    rating = models.ForeignKey(
        RatingStar, on_delete=models.SET_NULL, verbose_name="рейтинг", null=True)
    trainer = models.ForeignKey(
        Trainer, verbose_name="тренер", on_delete=models.CASCADE, related_name="trainer_reviews")
    created_at = models.DateTimeField(
        verbose_name="Создано", default=timezone.now)

    class Meta:
        verbose_name = "Отзыв о тренерах"
        verbose_name_plural = "Отзывы о тренерах"

    def __str__(self):
        return f"{self.name} - {self.email}"

    @property
    def time_age(self):
        return abs((timezone.now() - self.created_at).seconds // 3600)


class Post(models.Model):
    '''
    Модель статьи
    '''

    title = models.CharField('Заголовок статьи', max_length=100)
    category = models.CharField('Категория', max_length=100)
    content = CKEditor5Field(
        blank=True, verbose_name='Описание', config_name='extends')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
