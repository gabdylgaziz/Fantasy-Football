from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django.views.generic.edit import CreateView

from .serializers import *
from .models import *
from account.models import *


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



def player_list(request):
    goalkeepers = Footballer.objects.filter(position='GK').values()
    defenders = Footballer.objects.filter(position='DEF').values()
    midfielders = Footballer.objects.filter(position='MID').values()
    forwards = Footballer.objects.filter(position='FWD').values()

    context = {
        'goalkeepers': list(goalkeepers),
        'defenders': list(defenders),
        'midfielders': list(midfielders),
        'forwards': list(forwards),
    }

    return JsonResponse(context)

def getTopPlayers(request):
    top = UserData.objects.filter(is_active=True).order_by('-score')
    print(top)
    out = []
    for query in top:
        out.append({'id': query.id, 'name': query.name, 'score': query.score})
    res = {
        'top' : out
    }
    return JsonResponse(res)

def getClub(request, id):
    top = Club.objects.filter(id=id)
    players = Footballer.objects.filter(club=id)
    out = []
    for query in top:
        out.append({'id': query.id, 'name': query.name, 'country': query.country})
    player = []
    for p in players:
            player.append({"id": p.id, "nick_name": p.nick_name, "jersy_number": p.jersy_number})
    res = {
        'Club' : out,
        'Players' : player
    }
    return JsonResponse(res)

def getFootballer(request, id):
    player = Footballer.objects.filter(id=id)
    res = {
        'Players' : list(player.values())
    }
    return JsonResponse(res)




