# Generated by Django 4.2.7 on 2023-11-26 15:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("syrius", "0003_delete_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="victorina",
            name="invalid_count",
        ),
    ]