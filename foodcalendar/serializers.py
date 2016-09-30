from foodcalendar.models import Day
from rest_framework import serializers

class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ('account', 'member', 'date', 'meal', 'whoiscooking',
                  'ingredient', 'created', 'ingredient_there')
