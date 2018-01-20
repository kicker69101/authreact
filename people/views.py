from django.shortcuts import render
from people.models import Person
from people.serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    """
    Jesus take the wheel
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # authentication_classes = (BaseAuthentication, SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )
