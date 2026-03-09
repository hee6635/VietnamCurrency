from kivy.app import App
from kivy.uix.label import Label

class CurrencyApp(App):
    def build(self):
        return Label(text="Vietnam Currency")

CurrencyApp().run()
