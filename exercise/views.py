from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView
from django.urls import reverse_lazy,reverse
from .models import Exercise, Training, Day
from .forms import UpdateForm,NewTraining

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin


class NewExercise(LoginRequiredMixin,CreateView):
    model=Exercise
    form_class=UpdateForm
    template_name="exercise/record.html"
    success_url=reverse_lazy("exercise-add")

    def form_valid(self, form=UpdateForm):
        self.object=form.save(commit=False)
        self.object.profile=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class UpdateExercise(UpdateView):
    model=Exercise
    form_class=UpdateForm
    template_name="exercise/record.html"

    def get_success_url(self):
        return reverse ('exercise-detail', kwargs={'muscle': self.object.type})

@login_required
def ExerciseList(request):
    user=request.user
    qs=Exercise.objects.filter(profile=user).order_by('type')

    muscle_history=[]
    for instance in qs:
        if instance.type in muscle_history:
            pass
        else:
            muscle_history.append(instance.type)

    context={
        "qs":qs,
        "muscles":muscle_history
    }
    return render (request,"exercise/list.html",context)

@login_required
def ExerciseRecord(request,muscle):
    user=request.user
    if muscle == "All":
        qs=Exercise.objects.filter(profile=user).order_by("type")
    else:
        qs=Exercise.objects.filter(profile=user,type=muscle)
    
    class Exercisez:
        def __init__(self,muscle,name,rep,ser,weight,form,id,formID):
            self.muscle=muscle
            self.name=name
            self.rep=rep
            self.ser=ser
            self.weight=weight
            self.form=form
            self.id=id
            self.formID=formID

        def __str__(self):
            return f"{self.name},{self.rep},{self.ser}"

    data=[]
    for instance in qs:
        
        single=Exercise.objects.get(id=instance.id)
        data_form=UpdateForm(instance=single)

        obj=Exercisez(instance.type,instance.name,instance.repetition,instance.series,instance.weight,data_form,instance.id,instance.name.replace(" ","_"))
        data.append(obj)

    context={
        "muscle":muscle,
        "data":data
    }
    return render(request,"exercise/test.html",context)

class TrainingList(ListView):
    model=Training
    template_name="exercise/training.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user=self.request.user
        data=[]
        trained_muscles=[]
        week_day=Day.objects.all()
        for i in week_day:
            day_data={}
            day_data['day']=i.day
            muscles=[]
            muscle=i.day_of_the_week.filter(account=user)
            for instance in muscle:
                if instance.type not in trained_muscles:
                    trained_muscles.append(instance.type)
                muscles.append(instance.type)
            day_data['muscles']=muscles
            data.append(day_data)
        print(trained_muscles)
        context['muscle']=trained_muscles
        context['qs']=data
        return context

class TrainingAdd(CreateView):
    model=Training
    template_name="exercise/AddTraining.html"
    form_class=NewTraining
    success_url="/training/add/"

    def form_valid(self, form: NewTraining):
        user=self.request.user
        form.instance.account=user
        return super().form_valid(form)