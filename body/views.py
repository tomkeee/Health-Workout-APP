from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView
from django.views.generic.edit import UpdateView
from profiles.models import Weight
from .forms import WeightForm
from .utils import get_chart
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models.functions import ExtractWeek

class WeighList(LoginRequiredMixin,ListView):
    model=Weight
    template_name="body/weightList.html"
    queryset=Weight.objects.order_by("-date")

    def get_queryset(self) :
        user=self.request.user
        return super().get_queryset().filter(owner=user)

class WeightDelete(LoginRequiredMixin,DeleteView):
    model=Weight
    template_name="body/weightDelete.html"
    success_url=reverse_lazy("weight-list")

class WeightUpdate(LoginRequiredMixin,UpdateView):
    model=Weight
    form_class=WeightForm
    template_name="body/weightUpdate.html"
    success_url=reverse_lazy("weight")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

class WeightAdd(LoginRequiredMixin,CreateView):
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

            if each.week in weeks:
                index=weeks.index(each.week)
                previous_weeks=weeks.copy()
                previous_weeks.pop(index)
                try:
                    max_nr=max(previous_weeks)
                except:
                    max_nr=date_value[index]['week_of_the_year']
                previous_index=weeks.index(max_nr)

                date_value[index]['weight_value'] += each.value
                date_value[index]['number_of_records_in_a_week'] += 1
                date_value[index]['average'] = (date_value[index]['weight_value'] / date_value[index]['number_of_records_in_a_week'])
                if len(date_value) > 1:
                    date_value[index]['week_change']=((date_value[index]['average']/date_value[previous_index]['average'])-1)*100

                    if  date_value[index]['week_change'] > 0:
                        arrow="up"
                    elif date_value[index]['week_change'] < 0:
                        arrow="down"
                    else:
                        week_change="none"
                    date_value[index]['arrow']=arrow
            else:
                package={}
                weeks.append(each.week)

                week_of_the_year=each.week
                package['week_of_the_year']=week_of_the_year

                weight_value=each.value
                package['weight_value']=weight_value

                number_of_records_in_a_week=1
                package['number_of_records_in_a_week']=number_of_records_in_a_week

                average=each.value
                package['average']=average

                start = pd.Series(pd.date_range(start='2021-1-1',periods=(each.week),normalize=True, freq='W'))[(each.week-1)].strftime("%-d %B, %Y")
                package['start']=start
                print(each.week)

                end = pd.Series(pd.date_range(start='2021-1-1',periods=(each.week+1), normalize=True, freq='W'))[(each.week)].strftime("%-d %B, %Y")
                package['end']=end

                if len(date_value) >= 1:
                    week_change=((each.value/date_value[-1]['average'])-1)*100
                    package['week_change']=week_change
                    if  week_change> 0:
                        arrow="up"
                    elif week_change < 0:
                        arrow="down"
                    else:
                        arrow="none"
                    package['arrow']=arrow
                date_value.append(package)
        context['week']=date_value
################################################## DAILY ###################################################
        dates=[]
        data=[]
        for instance in weight:
            package={}
            if instance.date not in dates:
                new_day=instance.date
                dates.append(new_day)

                day=instance.date.strftime("%-d %B, %Y") 
                day_chart=instance.date.strftime("%-d.%m")
                package['day_chart']=day_chart
                package['day']=day

                day_weight=instance.value
                package['weight']=day_weight

                if data:
                    day_change=((day_weight/data[-1]['weight'])-1)*100
                    package['weight_change']=day_change
                    if day_change > 0:
                        arrow="up"
                    elif day_change < 0:
                        arrow="down"
                    else:
                        arrow="none"
                    package['arrow']=arrow
                data.append(package)
        

        context["data"]=data
        if data:
            if type=="daily":
                df=pd.DataFrame(data)
                chart=get_chart(df,y='weight',x='day_chart')
                context["chart"]=chart
            else:
                df=pd.DataFrame(date_value)
                chart=get_chart(df,y='average',x='start')
                context["chart"]=chart  

        if method == "descending":
            date_value.reverse()
            data.reverse()
        return context

@login_required
def WeightController(request):
    user=request.user

    weight=Weight.objects.filter(owner=user).order_by("-date")

    context={"weight":weight}
    return render(request,"body/weight.html",context)