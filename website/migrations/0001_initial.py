# Generated by Django 4.1.2 on 2022-10-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pastes",
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
                ("uuid", models.CharField(max_length=100)),
                ("data", models.CharField(max_length=10000)),
            ],
        ),
    ]
