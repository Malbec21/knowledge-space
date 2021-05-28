# Generated by Django 3.1.8 on 2021-05-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20210526_1345"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="place_of_work",
            field=models.ManyToManyField(
                blank=True, related_name="employees", to="accounts.WorkPlace"
            ),
        ),
    ]
