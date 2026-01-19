# familyaccount/urls.py
from django.urls import path
from .views import CreateFamilyAccountView

urlpatterns = [
    path('create-family-account/', CreateFamilyAccountView.as_view(), name='create-family-account'),
]
