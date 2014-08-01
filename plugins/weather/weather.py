__author__ = 'adam'

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
import pywapi
import os

__directory__ = os.path.dirname(os.path.realpath(__file__))
graphics_dir = os.path.join(__directory__, "images")

Builder.load_file(os.path.join(__directory__, "weather.kv"))

class my_screen(Screen):

    def change_image(self, current_image, day_image):
        self.current_image.source = current_image
        self.day_image.source = day_image

    def setup(self):
        self.name = 'weather'
        self._image_path = os.path.join(graphics_dir, "na.png")
        self.change_image(self._image_path, self._image_path)
        self._weather_updater()
        Clock.schedule_interval(self._weather_updater, 300)

    def _weather_updater(self, *args):
        print('updating weather')
        weather = pywapi.get_weather_from_weather_com('CAXX0401')
        print(weather)
        current_temp = weather['current_conditions']['temperature'] + u'\N{DEGREE SIGN}' + "C"
        high_temp = weather['forecasts'][0]['high']
        low_temp = weather['forecasts'][0]['low']
        self.temp.text = current_temp
        self.high_temp.text = high_temp
        self.low_temp.text = low_temp
        self._image_path = os.path.join(graphics_dir, weather['current_conditions']['icon'] + ".png")
        if weather['forecasts'][0]['day']['icon'] <> '':
            day_image = os.path.join(graphics_dir, weather['forecasts'][0]['day']['icon'] + ".png")
        else:
            day_image = os.path.join(graphics_dir, weather['forecasts'][0]['night']['icon'] + ".png")
        self.change_image(self._image_path, day_image)


class Weather(object):

    """
    def build(self):
        self.ws = WeatherScreen()
        self._image_path = os.path.join(graphics_dir, "na.png")
        self.ws.change_image(self._image_path, self._image_path)
        self._weather_updater()
        Clock.schedule_interval(self._weather_updater, 300)
        return self.ws
    """
    def my_screen(self):
        self.ws = WeatherScreen()
        self._image_path = os.path.join(graphics_dir, "na.png")
        self.ws.change_image(self._image_path, self._image_path)
        self._weather_updater()
        Clock.schedule_interval(self._weather_updater, 300)
        return self.ws

    def _weather_updater(self, *args):
        weather = pywapi.get_weather_from_weather_com('CAXX0401')
        print(weather)
        current_temp = weather['current_conditions']['temperature'] + u'\N{DEGREE SIGN}' + "C"
        high_temp = weather['forecasts'][0]['high']
        low_temp = weather['forecasts'][0]['low']
        self.ws.temp.text = current_temp
        self.ws.high_temp.text = high_temp
        self.ws.low_temp.text = low_temp
        self._image_path = os.path.join(graphics_dir, weather['current_conditions']['icon'] + ".png")
        if weather['forecasts'][0]['day']['icon'] <> '':
            day_image = os.path.join(graphics_dir, weather['forecasts'][0]['day']['icon'] + ".png")
        else:
            day_image = os.path.join(graphics_dir, weather['forecasts'][0]['night']['icon'] + ".png")
        self.ws.change_image(self._image_path, day_image)