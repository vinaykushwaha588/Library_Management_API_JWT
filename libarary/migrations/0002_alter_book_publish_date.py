# Generated by Django 4.0.6 on 2022-07-09 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libarary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.date(2022, 7, 9)),
        ),
    ]
