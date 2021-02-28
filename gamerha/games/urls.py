from django.conf.urls import url, include
from . import views
from .views import GameCreate

urlpatterns = [
    url(r'^add/$(?i)', views.add_new_game_view, name='add_new_game'),
    url(r'^api/$(?i)', views.api_view, name='api'),
    url(r'^create/$(?i)', GameCreate.as_view(), name='game_create'),
]
