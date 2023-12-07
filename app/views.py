from django.shortcuts import render, redirect
from . import models
from . forms import ExampleForm
# Create your views here.
def home(request):
    students = models.Student.objects.all()
    return render(request, 'home.html', {'data': students})

def model(request):
    data = models.MyModel.objects.all()
    return render(request, 'model.html', {'data':data})

def contact(request):
    form = ExampleForm()
    return render(request, 'contact.html', {'form':form})