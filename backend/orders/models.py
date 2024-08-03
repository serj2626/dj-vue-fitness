from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User


class Abonement(models.Model):
    """
    Абонементы
    """
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    number_of_months = models.SmallIntegerField("Количество месяцев")

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"
        ordering = ["pk"]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"
        ordering = ["-price"]


class OrderAbonement(models.Model):
    """
    Забронировать абонемент
    """

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tickets")
    phone = models.CharField('Телефон', max_length=11, null=True, blank=True)
    abonement = models.ForeignKey("Абонемент",
                                  Abonement, on_delete=models.CASCADE, related_name="orders")
    start = models.DateTimeField('Начало', auto_now_add=True)
    end = models.DateTimeField('Конец', blank=True, null=True)
    status = models.BooleanField('Оплачен', default=False)
    active = models.BooleanField('Активен', default=False)

    def save(self, *args, **kwargs):
        if not self.end:
            count_days = self.abonement.number_of_months * 30
            self.end = self.start + timedelta(count_days)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Забронированный абонемент"
        verbose_name_plural = "Забронированные абонементы"

    def __str__(self):
        return f'Order - {self.abonement} - {self.user.email}'


# class OrderTraining(models.Model):
#     """
#     Забронировать занятие
#     """

#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="trainings")
#     trainer = models.ForeignKey(
#         Trainer, on_delete=models.CASCADE, related_name="user_trainings")
#     rate = models.ForeignKey(
#         Rate, on_delete=models.CASCADE, related_name="user_trainings", blank=True, null=True)
#     start = models.DateTimeField("Дата начала")
#     end = models.DateTimeField('Конец', blank=True, null=True)
#     status = models.BooleanField('Оплачен', default=False)
#     active = models.BooleanField('Активен', default=False)

#     class Meta:
#         verbose_name = "Забронированное занятие"
#         verbose_name_plural = "Забронированные занятия"

#     def __str__(self):
#         return f'Занятие {self.rate} - {self.trainer}'


# class CalendarTrainer(models.Model):
#     """
#     Расписание тренировок тренеров
#     """

#     trainer = models.ForeignKey(
#         Trainer, on_delete=models.CASCADE, related_name="calendars", verbose_name="Тренер")
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="calendars", blank=True, null=True, verbose_name="Клиент")
#     start = models.DateTimeField(
#         blank=True, null=True, verbose_name="начало тренировки")
#     end = models.DateTimeField(
#         blank=True, null=True, verbose_name="конец тренировки")
#     status = models.BooleanField(default=False, verbose_name="занято")

#     class Meta:
#         verbose_name = "Расписание тренера"
#         verbose_name_plural = "Расписание тренеров"
#         ordering = ["start"]

#     def __str__(self):
#         return f'Расписание {self.trainer}'
