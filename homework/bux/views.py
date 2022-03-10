from django.shortcuts import render
from .models import Project
from.forms import GuysFoms

def views_home(request):
    return render(request,'bux.html')
def views_home2(request):
    return render (request,'bux.html')
def views_aboute(request):
    project = Project.objects.all()
    context = {'project': project}
    return render (request,'aboute.html',context)
def views_services(request):
    return render (request,'services.html')

def views_contact(request):
    form = GuysFoms(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data

        print(data['name'])
        new_form = form.save()
    return render (request,'contact.html',locals())

def views_server(request):
   form = GuysFoms(request.POST or  None)
   if request.method == 'POST' and form.is_valid():
       print(request.POST)
       print(form.cleaned_data)
       data = form.cleaned_data

       print(data['name'])
       new_form = form.save()
   return  render (request,'new.html',locals())