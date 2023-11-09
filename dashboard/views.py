from django.shortcuts import render
from dashboard import models


def DashboardPage(request):
    #meetings = models.Meeting.objects.all() , {'meetings': meetings}
    return render(request, 'dashboard/dashboard.html')


def loginPage(request):
    return render(request, 'dashboard/login.html')

# meetingsAI/dashboard/views.py
#from django.shortcuts import render
#from .models import Meeting

