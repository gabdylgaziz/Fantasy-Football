from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .serializers import *
from .models import *


# Create your views here.

def main(request):
    return JsonResponse({'FIRST PAGE': 'HELLO WORLD'})

class ClubViewSet(viewsets.ViewSet):
    """

    A simple viewset for viewing club
    """

    queryset = Club.objects.all()

    @extend_schema(responses=ClubSerializer)
    def list(self, request):
        selializer = ClubSerializer(self.queryset, many=True)
        return Response(selializer.data)




class FootballerViewSet(viewsets.ViewSet):
    """

    A simple viewset for viewing Foot baller
    """

    queryset = Footballer.objects.all()

    @extend_schema(responses=FootballerSerializer)
    def list(self, request):
        selializer = FootballerSerializer(self.queryset, many=True)
        return Response(selializer.data)