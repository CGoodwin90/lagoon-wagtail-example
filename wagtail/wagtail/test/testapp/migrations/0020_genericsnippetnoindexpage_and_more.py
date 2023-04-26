# Generated by Django 4.0.8 on 2023-01-21 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("tests", "0019_fullfeaturedsnippet_translatable"),
    ]

    operations = [
        migrations.CreateModel(
            name="GenericSnippetNoIndexPage",
            fields=[
                (
                    "genericsnippetpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="tests.genericsnippetpage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("tests.genericsnippetpage",),
        ),
        migrations.CreateModel(
            name="GenericSnippetNoFieldIndexPage",
            fields=[
                (
                    "genericsnippetpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="tests.genericsnippetpage",
                    ),
                ),
                (
                    "snippet_content_type_nonindexed",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("tests.genericsnippetpage",),
        ),
    ]