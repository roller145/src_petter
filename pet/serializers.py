from rest_framework import serializers

from models import Pet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('author', 'date_created', 'birthday', 'name', 'species', 'avatar')
