from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView
from django.views.generic.edit import UpdateView
from profiles.models import Weight
from .forms import WeightForm

import pandas as pd

from django.db.models.functions import ExtractWeek

class WeighList(ListView):
    model=Weight
    template_name="body/weightList.html"
    queryset=Weight.objects.order_by("-date")

    def get_queryset(self) :
        user=self.request.user
        return super().get_queryset().filter(owner=user)

class WeightDelete(DeleteView):
    model=Weight
    template_name="body/weightDelete.html"
    success_url=reverse_lazy("weight-list")

class WeightUpdate(UpdateView):
    model=Weight
    form_class=WeightForm
    template_name="body/weightUpdate.html"
    success_url=reverse_lazy("weight")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

class WeightAdd(CreateView):
    model=Weight
    form_class=WeightForm
    template_name='body/weight.html'
    success_url=reverse_lazy("weight")

    def form_valid(self, form: WeightForm):
        user=self.request.user
        form.instance.owner=user
        return super().form_valid(form)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
########################################### WEEKLY/DAILY ASC/DESC ################################################
        try:
            type= self.request.POST.get("type") or self.request.session['type']
            method=self.request.POST.get("method") or self.request.session['method']
        except:
            type="daily"
            method="ascending"


        self.request.session['type']=type
        context['type']=type

        self.request.session['method']=method

        user=self.request.user
        weight=Weight.objects.filter(owner=user).order_by("date")
################################################## WEEKLY ###################################################
        x=weight.annotate(week=ExtractWeek('date'))

        weeks=[]
        date_value=[]
        for each in x:
            print(each.id)
            if each.week in weeks:
                index=weeks.index(each.week)
                date_value[index][1] += each.value
                date_value[index][2] += 1
                date_value[index][3] = date_value[index][1] / date_value[index][2]
                if len(date_value) > 1:
                    date_value[index][6]=date_value[index][1]/date_value[-1][1]
            else:
                package=[]
                weeks.append(each.week)

                week_of_the_year=each.week
                package.append(week_of_the_year)

                weight_value=each.value
                package.append(weight_value)

                number_of_records_in_a_week=1
                package.append(number_of_records_in_a_week)

                average=each.value
                package.append(average)

                
                

                start = pd.Series(pd.date_range(start='2021-1-1',periods=(each.week),normalize=True, freq='W'))[(each.week-1)].strftime("%-d %B, %Y")
                package.append(start)

                end = pd.Series(pd.date_range(start='2021-1-1',periods=(each.week+1), normalize=True, freq='W'))[(each.week)].strftime("%-d %B, %Y")
                package.append(end)

                if len(date_value) > 1:
                    week_change=(each.value/date_value[-1][1])
                    package.append(week_change)

                date_value.append(package)


        if method == "descending":
            date_value.reverse()

        context['week']=date_value
        

################################################## DAILY ###################################################
        dates=[]
        data=[]
        for instance in weight:
            package=[]
            if instance.date in dates:
                pass
            else:
                new_day=instance.date
                dates.append(new_day)

                day=instance.date.strftime("%-d %B, %Y") 
                package.append(day)
                day_weight=instance.value
                package.append(day_weight)

                if data:
                    day_change=((day_weight/data[-1][1])-1)*100
                    package.append(day_change)

                    if day_change > 0:
                        arrow="up"
                    elif day_change < 0:
                        arrow="down"
                    else:
                        arrow="none"
                    package.append(arrow)
                    
                data.append(package)

        print(data)


        if method =="ascending":
            data.reverse()

        context["data"]=data

        return context
    
def WeightController(request):
    user=request.user
    print(user)
    weight=Weight.objects.filter(owner=user).order_by("-date")
    for i in weight:
        print(i)
        print(i.value)
        print(i.date)

    print(weight)
    context={"weight":weight}
    return render(request,"body/weight.html",context)