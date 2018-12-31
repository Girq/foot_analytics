from django.urls import path

from teams import views as teams_views

urlpatterns = [

    path('pl1/', teams_views.pleague1),
]
