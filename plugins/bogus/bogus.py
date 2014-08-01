__author__ = 'adam'

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import os

__directory__ = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(__directory__, "bogus.kv"))

class my_screen(Screen):

    def setup(self):
        self.name='bogus'