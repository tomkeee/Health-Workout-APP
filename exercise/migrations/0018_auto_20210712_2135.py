# Generated by Django 3.2 on 2021-07-12 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercise', '0017_rename_training_workout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('chest', 'chest'), ('biceps', 'biceps'), ('triceps', 'triceps'), ('back', 'back'), ('abs', 'abs'), ('shoulders', 'shoulders'), ('hamstring', 'hamstring'), ('calves', 'calves'), ('glutes', 'glutes')], max_length=9, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('day', models.ManyToManyField(related_name='day_of_the_week', to='exercise.Day')),
            ],
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
