from django.urls import path

from . import views

urlpatterns =[
    path('signin', views.signin, name='home'),
    path('application', views.app),
    
    path('user/details',views.getUserData)
]