from django.urls import path, include
from . import views

urlpatterns = [
    path ('api/', views.api, name='api'),
    path ('test/', views.test, name='test'),

]