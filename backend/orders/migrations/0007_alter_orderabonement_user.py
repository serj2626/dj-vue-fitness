# Generated by Django 5.0.7 on 2024-08-05 10:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0006_alter_orderabonement_abonement"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderabonement",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="abonements",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Клиент",
            ),
        ),
    ]