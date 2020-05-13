from kivy.config import Config
Config.set('graphics', 'window_state', 'visible')
#Config.set('graphics', 'width', '400')
#Config.set('graphics', 'height', '125')
#Config.set('graphics', 'height', '125')

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

class WindowManager(ScreenManager):
    pass

class LoginScreen (Screen):
    pass

class Dashboard (Screen):
    pass

class Register (Screen):
    pass

class HelpTick(App):
    title = 'Helpdesk Ticket Manager Login'
    pass


if __name__ == '__main__':

    HelpTick().run()
