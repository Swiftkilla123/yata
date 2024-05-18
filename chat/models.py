from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.timezone import now

from player.models import Player


# Create your models here.


class CustomDateTimeField(models.DateTimeField):

    def __init__(self, default=None):
        super(CustomDateTimeField, self).__init__()

    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        return val


class PersistentRoom(models.Model):

    owner = models.ForeignKey(Player, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, unique=True)
    room_staff = models.BooleanField(default=False, null=False)
    version = models.IntegerField(default=1)
    slug = models.SlugField(max_length=35)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return '{} ver.{}'.format(self.name, self.version)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        self.updated = now()
        super(PersistentRoom, self).save()


class RoomMessage(models.Model):

    class Meta:
        ordering = ['received']

    room = models.ForeignKey(PersistentRoom, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=200)
    sender = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    received = CustomDateTimeField(default=now)

    def __str__(self):
        return self.message

    def get_messages(self, room):
        return self.objects.filter(room=room)


class RoomSubscription(models.Model):

    subscriber = models.ForeignKey(Player, on_delete=models.CASCADE)
    room = models.ManyToManyField(PersistentRoom)

    def __str__(self):
        return "{}'s subscriptions" if not self.subscriber.name[-1] == 's' else "{}' subscriptions"
