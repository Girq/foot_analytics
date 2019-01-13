from django.urls import path

from test1 import views as test1_views

urlpatterns = [

    path('bootstrap/', test1_views.test),
    path('blabla/', test1_views.foot)
]
