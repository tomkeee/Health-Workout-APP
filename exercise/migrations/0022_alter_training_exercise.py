# Generated by Django 3.2 on 2021-07-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0021_auto_20210713_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='exercise',
            field=models.ManyToManyField(null=True, to='exercise.Exercise'),
        ),
    ]
