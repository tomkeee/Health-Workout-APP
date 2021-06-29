from .models import Exercise
from django.forms import ModelForm
from django import forms

MUSCLE=(
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

class UpdateForm(ModelForm):
    class Meta:
        model=Exercise
        fields=["name","repetition","series","weight","type"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Name your new exercise"}),
            "series":forms.NumberInput(attrs={"class":"form-control","placeholder":"  Series", "style":"font-size:0.9em"  }),
            "repetition":forms.NumberInput(attrs={"class":"form-control","placeholder":"   Reps", "style":"font-size:0.9em" }),
            "weight":forms.NumberInput(attrs={"class":"form-control","placeholder":"   Kg", "style":"font-size:0.9em" }),
            "type":forms.Select(choices=MUSCLE ,attrs={"class":"form-select col-md-2"})
        }
    def clean_name(self):
        data=self.cleaned_data.get("name")
        if data.isdigit():
            raise forms.ValidationError("Name of your exercise should be a value not a number")
        return data