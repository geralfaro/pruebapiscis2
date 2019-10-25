from django.urls import path
from . import views

urlpatterns = [
        path('', views.pag_ppal, name = 'pag_ppal')]
