from django.contrib.auth.models import Group, User
from rest_framework import serializers

from patinetes.models import Patinete


class PatineteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patinete
        fields = ['url', 'tipo', 'numero', 'precio_desbloqueo', 'precio_minuto']
