from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.targets_list),
    path("<month>", views.targets, name= "month_target"),
]
