#!/usr/bin/python
from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput
from foodcalendar import CalendarWidget
#from kivy.resources import resource_add_path
import os
import json
import requests

#class LoginScreen(GridLayout):
#    def __init__(self, **kwargs):
#        super(LoginScreen, self).__init__(**kwargs)
#        self.cols = 2
#        self.add_widget(Label(text='User Name'))
#        self.username = TextInput(multiline=False)
#        self.add_widget(self.username)
#        self.add_widget(Label(text='password'))
#        self.password = TextInput(password=True, multiline=False)
#        self.add_widget(self.password)

class MyApp(App):
    def __init__(self):
        super(MyApp,self).__init__()
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path+'/app.conf','r') as configfile:
            config = json.load(configfile)
        self.server = config["server"]
        print self.server

    def build(self):
#        dir_path = os.path.dirname(os.path.realpath(__file__))
#        resource_add_path(dir_path + "/images")
        data = self.getCalendarData()
        return CalendarWidget(data)
        #return LoginScreen()

    def getCalendarData(self):
        r = requests.get("http://" + self.server + "/api/calendar")
        return r.json()
#        return {}

if __name__ == '__main__':
    MyApp().run()
