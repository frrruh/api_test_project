# Generated by Django 4.2.7 on 2023-12-17 07:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("syrius", "0006_syrius_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="syrius",
            name="user",
        ),
    ]
