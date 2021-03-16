from rest_framework import serializers
from .models import PropertyMaster, User


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class JournalSerializer(serializers.ModelSerializer):
    AllDetails = StringSerializer(many=False)
    User = StringSerializer(many=True)

    class Meta:
        model = PropertyMaster
        fields = ('__all__')
