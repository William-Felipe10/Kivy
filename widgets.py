from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Label(text='Olá William', font_size= 100, font_name='Times', color = get_color_from_hex ('#FF1493'))
    
if __name__ == '__main__':
    MinhaApp().run()