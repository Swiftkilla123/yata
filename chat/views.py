from django.utils.safestring import mark_safe
import json
from django.shortcuts import render
from django.views.generic import TemplateView

from yata.handy import getPlayer
from .models import PersistentRoom, RoomSubscription, RoomMessage

from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    player = getPlayer(request.session.get('player', {}).get('tId'))
    print(player)
    if not player:
        return render(request, 'chat/index.html', {})
    persistent_room, created = PersistentRoom.objects.get_or_create(
        name=room_name,
        defaults={
            'owner': player,
        }
    )
    print(persistent_room)
    if created:
        persistent_room.save()

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'player': player
    })


class RoomView(TemplateView):

    template_name = 'chat/room.html'

    def get(self, request, *args, **kwargs):

        room_name_json = mark_safe(json.dumps(request.GET.get('room_name')))
        player = _get_current_player(request)

        return render(request, self.template_name)
