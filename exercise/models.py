from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

MUSCLE_INVOLVED=(
    ("chest","chest"),
    ("biceps","biceps"),
    ("triceps","triceps"),
    ("back","back"),
    ("abs","abs"),
    ("shoulders","shoulders"),
    ("hamstring","hamstring"),
    ("calves","calves"),
    ("glutes","glutes")
)

class Exercise(models.Model):
    profile=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=9,choices=MUSCLE_INVOLVED,null=True)
    repetition=models.PositiveIntegerField()
    weight=models.FloatField()
    series=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} - {self.name}"

    def get_absolute_url(self):
        return reverse("exercise_detail", kwargs={"pk": self.pk})