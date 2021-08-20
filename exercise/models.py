from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectFormField

MUSCLE_INVOLVED=(
    ("chest","chest"),
    ("biceps","biceps"),
    ("triceps","triceps"),
    ("back","back"),
    ("abs","abs"),
    ("shoulders","shoulders"),
    ("hamstring","hamstring"),
    ("calves","calves"),
    ("glutes","glutes"),
    ("training","training")
)

WEEK_DAY=(
    ("Monday","Monday"),
    ("Tuesday","Tuesday"),
    ("Wednesday","Wednesday"),
    ("Thursday","Thursday"),
    ("Friday","Friday"),
    ("Saturday","Saturday"),
    ("Sunday","Sunday"),
)

class Exercise(models.Model):
    profile=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=9,choices=MUSCLE_INVOLVED,null=True)
    repetition=models.PositiveIntegerField(blank=True,null=True)
    weight=models.FloatField(blank=True,null=True)
    series=models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.type} - {self.name}"

    def get_absolute_url(self):
        return reverse("exercise_detail", kwargs={"pk": self.pk})

class Training(models.Model):
    account=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    day=models.CharField(max_length=10,choices=WEEK_DAY,null=True)
    exercise=models.ManyToManyField(Exercise,null=True)

    def get_exercises(self):
        return self.exercise.all()

    def __str__(self):
        return f"{self.day} exercises"