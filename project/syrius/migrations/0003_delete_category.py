# Generated by Django 4.2.7 on 2023-11-26 15:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "syrius",
            "0002_category_victorina_rename_content_syrius_description_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="Category",
        ),
    ]