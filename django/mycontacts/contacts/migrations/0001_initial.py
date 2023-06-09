# Generated by Django 4.1.5 on 2023-05-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("first", models.CharField(blank=True, max_length=255, null=True)),
                ("last", models.CharField(blank=True, max_length=255, null=True)),
                ("phone", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
