import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class FirstLayout(BoxLayout):
    pass

class Test(App):
    def build(self):
        layout1 = FirstLayout(orientation = 'vertical')
        layout1.add_widget(Button(text='FirstButton'))
        layout1.add_widget(Label(text = 'FirstButton'))
        return layout1
    
Test().run()

