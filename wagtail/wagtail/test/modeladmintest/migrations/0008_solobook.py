# Generated by Django 2.1.10 on 2019-07-17 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("modeladmintest", "0007_friend"),
    ]

    operations = [
        migrations.CreateModel(
            name="SoloBook",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="modeladmintest.Author",
                    ),
                ),
            ],
        ),
    ]
