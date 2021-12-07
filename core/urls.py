from django.urls import path
from .views import ListContact, DetailContact

urlpatterns = [
    path('', ListContact.as_view()),
    path('<int:pk>', DetailContact.as_view())
]