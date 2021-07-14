# Generated by Django 3.2 on 2021-07-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20210625_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('chest', 'chest'), ('biceps', 'biceps'), ('triceps', 'triceps'), ('back', 'back'), ('abs', 'abs'), ('shoulders', 'shoulders'), ('hamstring', 'hamstring'), ('calves', 'calves'), ('glutes', 'glutes')], max_length=9, null=True)),
                ('exercises', models.ManyToManyField(to='exercise.Exercise')),
            ],
        ),
    ]