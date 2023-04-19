from django.urls import path
from .views import register_user, record, retrieve

urlpatterns = [
    path('register/', register_user, name='register'),
    path('record/', record, name="record"),
    path('retrieve/', retrieve, name="retrieve"),
]