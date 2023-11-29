from rest_framework import generics
from .models import Place
from .serializers import PlaceSerializer
from django.http import HttpResponse
import requests
from django.conf import settings
import json

def check_place(data):
    r = requests.get(settings.PLACES_API_PATH, headers={"Accept": "application/json"})
    places = r.json()
    for place in places:
        if data["place"] == place["id"]:
            return True
    return False

class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        if check_place(data) is True:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponse("Unsuccessfully created place. Place does not exist")

