from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.

def get_data(request):
    # GET request to the API
    response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')

    # Parse the JSON response
    data = response.json()
    return JsonResponse(data)
