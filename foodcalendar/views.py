from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from foodcalendar.models import Day
from foodcalendar.serializers import DaySerializer

# Create your views here.
class CalendarView(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Day.objects.all()
    serializer_class = DaySerializer
