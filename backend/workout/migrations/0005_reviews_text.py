# Generated by Django 5.0.7 on 2024-08-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0004_reviews_rating_alter_reviews_trainer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviews",
            name="text",
            field=models.TextField(
                max_length=5000, null=True, verbose_name="Текст отзыва"
            ),
        ),
    ]
