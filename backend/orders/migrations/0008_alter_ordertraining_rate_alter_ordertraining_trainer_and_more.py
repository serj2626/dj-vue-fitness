# Generated by Django 5.0.7 on 2024-08-05 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0007_alter_orderabonement_user"),
        ("workout", "0004_reviews_rating_alter_reviews_trainer_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordertraining",
            name="rate",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_trainings",
                to="workout.rate",
                verbose_name="Тариф",
            ),
        ),
        migrations.AlterField(
            model_name="ordertraining",
            name="trainer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_trainings",
                to="workout.trainer",
                verbose_name="Тренер",
            ),
        ),
        migrations.AlterField(
            model_name="ordertraining",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trainings",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Клиент",
            ),
        ),
    ]