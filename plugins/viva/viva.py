__author__ = 'adam'

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from bs4 import BeautifulSoup
import requests
import os

__directory__ = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(__directory__, "viva.kv"))

class my_screen(Screen):

    def setup(self):
        self.name = 'viva'
        self.update()

    def update(self):
        page = requests.get("http://tripplanner.yrt.ca/hiwire?Date=Today&TimeHour=9&TimeMinute=20&Meridiem=p&.a=iNextBusFind&.s=89519c04&ShowTimes=1&NumStopTimes=5&GetSchedules=1&EndGeo=&StopAbbr=4259&.a=iNextBusFind")
        bs = BeautifulSoup(page.text)
        table = bs.find_all('table')[1]
        rows = table.find_all('tr')
        for row in rows[1:]:
            cols = row.find_all('td')
            route_name, route_num, direction, scheduled, status, departure, map = [col.text for col in cols]
            print route_name, route_num, direction, scheduled, status, departure

        print("Done")