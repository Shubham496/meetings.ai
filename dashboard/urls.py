from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('dashboard/', views.DashboardPage, name="dashboard"),
    
]


"""
# meetingsAI/dashboard/urls.py
from django.urls import path
#from .views import loginPage, DashboardPage

urlpatterns = [
    path('', loginPage, name="login"),
    path('dashboard/', DashboardPage, name="dashboard"),
]

"""