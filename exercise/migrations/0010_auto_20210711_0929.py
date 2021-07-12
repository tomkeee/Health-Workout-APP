# Generated by Django 3.2 on 2021-07-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0009_auto_20210709_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='WEEK_DAY',
        ),
        migrations.AlterField(
            model_name='training',
            name='day',
            field=models.ManyToManyField(to='exercise.Day'),
        ),
    ]
