from django.urls import path
from .views import CreateFamilyAdmin, InviteFamilyMember, AcceptInvite, GetFamilyMembers
urlpatterns = [
    path('create-family-admin/', CreateFamilyAdmin.as_view(), name='create-family-admin'),
    path('invite/', InviteFamilyMember.as_view()),
    path('accept-invite/', AcceptInvite.as_view(), name='accept-invite'),
    path('members/<int:family_id>/', GetFamilyMembers.as_view(), name='family-members'),
    path('members/', GetFamilyMembers.as_view(), name='family-members'),
]
