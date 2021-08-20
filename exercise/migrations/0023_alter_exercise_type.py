# Generated by Django 3.2 on 2021-08-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0022_alter_training_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='type',
            field=models.CharField(choices=[('chest', 'chest'), ('biceps', 'biceps'), ('triceps', 'triceps'), ('back', 'back'), ('abs', 'abs'), ('shoulders', 'shoulders'), ('hamstring', 'hamstring'), ('calves', 'calves'), ('glutes', 'glutes'), ('training', 'training')], max_length=9, null=True),
        ),
    ]