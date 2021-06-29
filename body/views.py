from django.shortcuts import render,HttpResponse
from django.views.generic import CreateView
from profiles.models import Profile, Weight
from django.utils import timezone
from .forms import WeightForm

class WeightUpdate(CreateView):
    model=Weight
    form_class=WeightForm
    template_name='body/weightUpdate.html'
    success_url="/"

    def form_valid(self, form: WeightForm):
        user=self.request.user
        profile=Profile.objects.get(account=user)
        form.instance.owner=profile
        return super().form_valid(form)
    
def WeightController(request):
    user=request.user
    print(user)
    weight=Weight.objects.filter(owner=user)
    for i in weight:
        print(i)
        print(i.value)
        print(i.date)

    print(weight)
    return HttpResponse("HEllo")
