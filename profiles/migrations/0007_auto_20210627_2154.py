# Generated by Django 3.2 on 2021-06-27 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210627_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='weight',
        ),
        migrations.AddField(
            model_name='weight',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]