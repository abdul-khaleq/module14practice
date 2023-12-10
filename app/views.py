from django.shortcuts import render, redirect
from . models import MyModel, Student
from . forms import ExampleForm
# Create your views here.
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'data': students})

def form(request):
    form = ExampleForm()
    return render(request, 'form.html', {'form':form})

def model(request):
    data = MyModel.objects.all()
    return render(request, 'model.html', {'data':data})
