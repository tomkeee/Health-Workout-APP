from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView
from django.urls import reverse_lazy,reverse
from .models import Exercise, Training
from .forms import UpdateForm,UpdateTraining

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

class UpdateExercise(LoginRequiredMixin,UpdateView):
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
    if request.method == "POST":
        training_id=request.POST.get("exercise_id",-1)
        if training_id != 0 :
            Exercise.objects.filter(id=training_id).delete()


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

class TrainingView(LoginRequiredMixin,ListView):
    model=Training
    template_name="exercise/training.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        user=self.request.user
        week_template=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

        qs=Training.objects.filter(account=user)
        data=[]

        trained_muscles_week=[]
        for instance in qs:
            package={}
            package['day']=instance.day
            package['id']=instance.id

            data_form=UpdateTraining(instance=instance)
            package['form']=data_form
            
            nr=week_template.index(instance.day)
            package['week_nr']=nr

            trained_muscles_day=[]
            for exercise in instance.exercise.all():

                if exercise.type not in trained_muscles_day:
                    trained_muscles_day.append(exercise.type)

                    if exercise.type not in trained_muscles_week:
                        trained_muscles_week.append(exercise.type)

            package['muscles']=trained_muscles_day
            data.append(package)
        
        context['trained_muscles_week']=trained_muscles_week

        sorted_data=sorted(data,key=lambda x:x['id'])
        context['sorted_data']=sorted_data

        return context

class TrainingUpdate(LoginRequiredMixin,UpdateView):
    model=Training
    template_name="exercise/trainingUpdate.html"
    form_class=UpdateTraining
    success_url=reverse_lazy("training")