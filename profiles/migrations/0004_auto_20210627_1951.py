# Generated by Django 3.2 on 2021-06-27 19:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='weight_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight_starting',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2021, 6, 27, 19, 51, 0, 378018, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(),
        ),
    ]
