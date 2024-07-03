from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.targets_list, name= "include"),
    path("<int:month>", views.targets_by_num ),
    path("<str:month>", views.targets, name= "month_target"),
]
