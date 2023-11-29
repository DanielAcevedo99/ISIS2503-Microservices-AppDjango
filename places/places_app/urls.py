from django.urls import path
from .views import PlaceListCreateView

urlpatterns = [
    path('places/', PlaceListCreateView.as_view(), name='place-list-create'),

]