from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'telecombat_app/index.html')
def telecombat18(request):
            return render(request,'telecombat_app/telecombat18.html')
def telecombat19(request):
    return render(request,'telecombat_app/telecombat19.html')
def studentachievements(request):
    return render(request,'telecombat_app/studentachievements.html')
# Create your views here.
def departmentactivities(request):
    return render(request,'telecombat_app/departmentactivities.html')
