# Generated by Django 4.2.7 on 2023-11-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("syrius", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("clues_count", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Victorina",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("answer", models.TextField(max_length=255)),
                ("question", models.TextField()),
                ("value", models.IntegerField(null=True)),
                ("airdate", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("category_id", models.IntegerField()),
                ("game_id", models.IntegerField()),
                ("invalid_count", models.IntegerField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name="syrius",
            old_name="content",
            new_name="description",
        ),
        migrations.AlterField(
            model_name="syrius",
            name="image",
            field=models.ImageField(upload_to="photos/"),
        ),
    ]
