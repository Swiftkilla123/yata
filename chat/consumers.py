from pprint import pprint

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import render
from django.template.defaultfilters import slugify
import json

from target.models import TargetInfo
from yata.handy import getPlayer
from . import models
from django.core.serializers import serialize
from django.utils import timezone


def now():
    return timezone.now()


class ChatConsumer(AsyncWebsocketConsumer):
    user = None
    room_name = None
    room_group_name = None
    room = None

    async def connect(self):
        print(self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        pprint(self.scope)
        self.user = await sync_to_async(models.Player.objects.get)(tId=self.scope['session']['player']['tId'])
        print(self.room_name)
        print(self.user)

        self.room, created = await sync_to_async(
            models.PersistentRoom.objects.get_or_create
        )(name=self.room_name,
          defaults={
              'owner': self.user,
              'name': self.room_name,
              'room_staff': False,
              'created': now()
          })
        print(self.room)
        self.room_group_name = 'chat_{}'.format(self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()
        text_data = await sync_to_async(serialize)('json', self.room.roommessage_set.all())
        await self.send(text_data=text_data)

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.user = await sync_to_async(models.Player.objects.get)(tId=self.scope['session']['player']['tId'])
        room_message = models.RoomMessage(sender=self.user, room=self.room, message=message, received=now())
        await sync_to_async(room_message.save)()
        self.room_id = room_message.pk
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.name
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        self.user = await sync_to_async(models.Player.objects.get)(tId=self.scope['session']['player']['tId'])
        room_message = models.RoomMessage.objects.filter(pk=self.room_id).all()
        # Send message to WebSocket
        text_data = await sync_to_async(serialize)('json', room_message)
        await self.send(text_data=text_data)


from channels.generic.websocket import AsyncWebsocketConsumer
import json
from faction.models import Faction, FactionTarget
from channels.db import database_sync_to_async
from django.template import Context, Template

class FactionWarConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_authenticated:
            await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        page = "faction/content-reload.html"
        player = getPlayer(self.scope['session']['player']['tId'])

        # get faction
        faction = Faction.objects.filter(tId=player.factionId).first()

        player_targets = FactionTarget.objects.filter(
            target_id__in=TargetInfo.objects.filter(player=player).values_list('target_id', flat=True)
        ).values_list('target_id', flat=True)

        context = Context({
            "player": player,
            "faction": faction,
            "factioncat": True,
            "view": {"war": True},
            "player_targets": player_targets,
        })

        template = Template("{% include '" + page + "' %}")
        await self.send(text_data=template.render(context))