# Generated by Django 5.0.7 on 2024-08-05 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "orders",
            "0008_alter_ordertraining_rate_alter_ordertraining_trainer_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderabonement",
            name="phone",
            field=models.CharField(
                blank=True, max_length=12, null=True, verbose_name="Телефон"
            ),
        ),
    ]
