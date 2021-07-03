from django.forms import widgets
from profiles.models import Weight
from django import forms

class WeightForm(forms.ModelForm):
    class Meta:
        model= Weight
        fields=["value"]

        widgets={
            "value":forms.TextInput(attrs={"class":"form-control col-4","placeholder":"Current Weight"})
            }