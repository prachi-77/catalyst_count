from django.urls import path

from . import views

urlpatterns =[
    path('company/filters', views.getCompanyFilters),
     path('query/count', views.getQueryCount),
   
]