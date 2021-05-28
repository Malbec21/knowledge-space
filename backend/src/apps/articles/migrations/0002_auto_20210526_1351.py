# Generated by Django 3.1.8 on 2021-05-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="bibliography_reference",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="scopus_indication",
            field=models.BooleanField(),
        ),
    ]
