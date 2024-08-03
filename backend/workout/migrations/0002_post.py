# Generated by Django 5.0.7 on 2024-08-03 13:36

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Заголовок статьи"),
                ),
                (
                    "category",
                    models.CharField(max_length=100, verbose_name="Категория"),
                ),
                (
                    "content",
                    django_ckeditor_5.fields.CKEditor5Field(
                        blank=True, verbose_name="Описание"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
                "ordering": ("-created_at",),
            },
        ),
    ]
