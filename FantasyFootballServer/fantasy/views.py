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

    queryset = Club.objects.all()

    @extend_schema(responses=ClubSerializer)
    def list(self, request):
        selializer = ClubSerializer(self.queryset, many=True)
        return Response(selializer.data)




class FootballerViewSet(viewsets.ViewSet):

    queryset = Footballer.objects.all()

    @extend_schema(responses=FootballerSerializer)
    def list(self, request):
        selializer = FootballerSerializer(self.queryset, many=True)
        return Response(selializer.data)