from django.urls import path
from .views import *

urlpatterns=[
    path('item/',FoodView.as_view()),
    path('item/<int:id>',FoodViewById.as_view()),
]