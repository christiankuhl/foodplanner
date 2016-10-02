#!/usr/bin/python
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
import json
import requests
import sys

class MyApp(App):
    def __init__(self):
        super(MyApp,self).__init__()
        with open('app.conf','r') as configfile:
            config = json.load(configfile)
        self.server = config["server"]
        print self.server

    def build(self):
        try:
            x = sys.argv[1]
            data = self.getCalendarData()
        except:
            data = {}
        return CalendarWidget(data)

    def getCalendarData(self):
        r = requests.get("http://" + self.server + "/api/calendar")
        return r.json()

class CalendarWidget(RelativeLayout):
    def __init__(*args):
        pass

if __name__ == '__main__':
    MyApp().run()
