from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index' ),
    path("signup/", signup, name="signup"),
    path("<str:room_name>/", room, name="room"),
]
