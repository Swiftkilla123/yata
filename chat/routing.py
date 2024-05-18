from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', consumers.ChatConsumer.as_asgi(), name='chat'),
    path('ws/ranked_war_line/', consumers.FactionWarConsumer.as_asgi(), name='ranked_war_line'),
]
