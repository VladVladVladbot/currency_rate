from django.urls import path
from .views import *

urlpatterns = [
    path('', ApiView.as_view(), name='apiview')
]
