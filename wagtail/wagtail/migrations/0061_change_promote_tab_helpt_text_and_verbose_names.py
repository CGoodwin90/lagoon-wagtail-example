# Generated by Django 3.0.12 on 2021-02-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0060_fix_workflow_unique_constraint"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="search_description",
            field=models.TextField(
                blank=True,
                help_text="The descriptive text displayed underneath a headline in search engine results.",
                verbose_name="meta description",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="seo_title",
            field=models.CharField(
                blank=True,
                help_text="The name of the page displayed on search engine results as the clickable headline.",
                max_length=255,
                verbose_name="title tag",
            ),
        ),
    ]
