# Generated by Django 3.2.5 on 2021-08-20 11:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210816_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 22, 11, 14, 21, 56315, tzinfo=utc)),
        ),
    ]
