from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('hola_mundo/',views.hola_mundo),
    path('hola_mundo/<str:name>',views.hola_mundo),
]