from django.urls import path
from .views import CreateFamilyAdmin, InviteFamilyMember, AcceptInvite

urlpatterns = [
    path('create-family-admin/', CreateFamilyAdmin.as_view(), name='create-family-admin'),
    path('invite/', InviteFamilyMember.as_view()),
    path('accept-invite/', AcceptInvite.as_view(), name='accept-invite'),
]
