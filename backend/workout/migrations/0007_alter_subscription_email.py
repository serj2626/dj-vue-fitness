# Generated by Django 5.0.7 on 2024-08-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0006_subscription_alter_post_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Почта"),
        ),
    ]
