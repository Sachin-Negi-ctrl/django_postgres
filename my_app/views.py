from django.shortcuts import render
from .models import Students
# Create your views here.

def home(request):
    students = Students.objects.all()
    return render(request, 'my_app/home.html',{"students":students})