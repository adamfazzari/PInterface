__author__ = 'afazzari'

from kivy.app import App
from kivy.uix.screenmanager import Screen
import os
import imp
import datetime

__directory__ = os.path.dirname(os.path.realpath(__file__))
plugin_dir = os.path.join(__directory__, "plugins")
plugin_script = 'screen.py'     # Name of the plugin's main file
plugin_module = 'screen'
min_screen_time_s = 1

class MainScreen(Screen):
    pass

class MainApp(App):

    def build(self):
        self.ms = MainScreen()
        self.ms.bind(on_touch_move=self.move_event)
        ts = self.get_screens()
        self.screens = dict()
        j = 0
        for i in ts:
            i.setup()
            self.ms.smanager.add_widget(i)
            self.screens[j] = i.name
            j+=1
        self.last_screen_change = datetime.datetime.now()
        self.ms.smanager.current = self.screens[0]
        return self.ms

    def move_event(self, instance, touch):
        self.next_screen()

    def next_screen(self):
        if (datetime.datetime.now() - self.last_screen_change).seconds > min_screen_time_s:
            self.last_screen_change = datetime.datetime.now()
            self.ms.smanager.current = self.ms.smanager.next()

    def previous_screen(self):
        self.ms.smanager.current = self.ms.smanager.previous()

    def get_plugins(self):
        plugins = []
        possibleplugins = os.listdir(plugin_dir)
        for i in possibleplugins:
            location = os.path.join(plugin_dir, i)
            if not os.path.isdir(location) or not (i + ".py") in os.listdir(location):
                continue
            info = imp.find_module(i, [location])
            plugins.append({"name": i, "info": info})
        return plugins

    def load_plugin(self, plugin):
        return imp.load_module(plugin["name"], *plugin["info"])

    def get_screens(self):
        a = []
        for i in self.get_plugins():
            plugin = self.load_plugin(i)
            loadedscreen = plugin.my_screen() #getattr(plugin, i['name'])
            a.append(loadedscreen)

        return a


if __name__ == "__main__":
    MainApp().run()
