from rest_framework import generics
from rank.models import Team,Racer
from .serializers import TeamSerializer,RacerSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
#base de custom quyen tuy chinh
from rest_framework.permissions import SAFE_METHODS, BasePermission,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly
class TeamList(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Team, name=item)
    # Define Custom Queryset
    def get_queryset(self):
        return Team.objects.all()
class RacerList(viewsets.ModelViewSet):
    serializer_class=RacerSerializer
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Racer,name=item)
    # Define Custom Queryset
    def get_queryset(self):
        return Racer.objects.all()
