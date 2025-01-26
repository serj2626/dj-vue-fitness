import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.timesince import timesince
from django_ckeditor_5.fields import CKEditor5Field

from .service import get_path_for_avatar_for_trainer

User = get_user_model()


# class FitnessClub(models.Model):
#     """
#     Фитнес клуб
#     """

#     title = models.CharField("Название клуба", max_length=100, unique=True)
#     city = models.CharField("Город", max_length=100)
#     address = models.CharField("Адрес", max_length=100, unique=True)
#     phone = models.CharField("Телефон", max_length=11, unique=True)
#     mail = models.EmailField("Почта", unique=True)
#     site = models.URLField("Сайт", unique=True)

#     class Meta:
#         verbose_name = "Фитнес клуб"
#         verbose_name_plural = "Фитнес клубы"

#     def __str__(self):
#         return self.title


# # create class by all images for fitness club


# class FitnessClubImage(models.Model):
#     image = models.ImageField(upload_to=get_path_for_avatar_for_trainer)
#     fitness_club = models.ForeignKey(FitnessClub, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Изображение {self.fitness_club}"

#     class Meta:
#         verbose_name = "Изображение"
#         verbose_name_plural = "Изображения"


class Rate(models.Model):
    """
    Цены индивидульных тренировок
    """

    title = models.CharField("Название тарифа", max_length=100)
    count_minutes = models.SmallIntegerField("Количество минут", blank=True, null=True)
    price = models.SmallIntegerField("Цена", default=1000)
    description = models.TextField("Описание тарифа", blank=True)

    class Meta:
        verbose_name = "Тариф тренера"
        verbose_name_plural = "Тарифы тренеров"
        ordering = ["-price"]

    def __str__(self):
        return (
            f"Индивидуальное занятие на {self.count_minutes} минут - тариф {self.title}"
        )


class Trainer(models.Model):
    """
    Тренер
    """

    POSITIONS = [
        ("fitness", "Инструктор тренажерного зала"),
        ("pool", "Инструктор бассейна"),
        ("yoga", "Инструктор йоги"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField("Должность", max_length=100, choices=POSITIONS)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Телефон", max_length=11, unique=True)
    avatar = models.ImageField(
        "Аватар",
        upload_to=get_path_for_avatar_for_trainer,
        default="trainers/trainer.jpg",
        blank=True,
    )
    bio = models.TextField("Биография", blank=True)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_position_display()}"


class RatingStar(models.Model):
    """
    Звезда рейтинга
    """

    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["value"]


class Reviews(models.Model):
    """
    Отзывы
    """

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="пользователь",
        related_name="user_reviews",
    )
    rating = models.ForeignKey(
        RatingStar, on_delete=models.SET_NULL, verbose_name="рейтинг", null=True
    )
    trainer = models.ForeignKey(
        Trainer,
        verbose_name="тренер",
        on_delete=models.CASCADE,
        related_name="trainer_reviews",
    )
    text = models.TextField("Текст отзыва", max_length=5000, null=True)
    created_at = models.DateTimeField(verbose_name="Создано", default=timezone.now)

    def date_age(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Отзыв о тренерах"
        verbose_name_plural = "Отзывы о тренерах"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Отзыв от {self.user.email}" if self.user else "Anonymous"

    @property
    def time_age(self):
        return timesince.timesince(self.created_at)


class Post(models.Model):
    """
    Модель статьи
    """

    title = models.CharField("Заголовок статьи", max_length=100)
    category = models.CharField("Категория", max_length=100)
    content = CKEditor5Field(blank=True, verbose_name="Описание", config_name="extends")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ("pk",)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    """
    Подписка на рассылку
    """

    email = models.EmailField("Почта", unique=True)

    class Meta:
        verbose_name = "Подписка на рассылку"
        verbose_name_plural = "Подписки на рассылку"

    def __str__(self):
        return self.email
