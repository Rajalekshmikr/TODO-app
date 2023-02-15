from django.shortcuts import render, redirect

from . forms import TodoForms
# from django.http import HttpResponse
from .models import Study
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here
class Studylistview(ListView):
    model=Study
    template_name='home.html'
    context_object_name='values1'
class StudyDetailview(DetailView):
    model=Study
    template_name='detail.html'
    context_object_name='value'
class StudyUpdateView(UpdateView):
    model=Study
    template_name='update.html'
    context_object_name='value'
    fields=('Topic','Imp_level_of_topic','No_of_revision','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class StudydeleteView(DeleteView):
    model = Study
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')

def fun1(request):
    # return HttpResponse("hello world")
    values1 = Study.objects.all()
    if request.method=='POST':

        topic=request.POST.get('Topic','')
        imp_lvl_top=request.POST.get('imp level of topic','')
        no_of_rvtn=request.POST.get('no of revision','')
        date=request.POST.get('date','')
        values=Study(Topic=topic,Imp_level_of_topic=imp_lvl_top,No_of_revision=no_of_rvtn,date=date)
        values.save()
    return render(request,'home.html',{'values1':values1})
def delete(request,studyid):
    value=Study.objects.get(id=studyid)
    if request.method=='POST':
        value.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    print('update')
    value=Study.objects.get(id=id)
    f=TodoForms(request.POST or None,instance=value)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'value':value})
#
# def details(request):
#
#     return render(request,'detail.html')
        # print(topic)
        # print(imp_lvl_top)
        # print(no_of_rvtn)


