from kivy.app import App
# Importando a classe App do módulo Kivy.app. A classe App é fundamental para criar aplicativos Kivy
from kivy.uix.button import Button
# Aqui importa a classe Button do módulo kivy.ui.Button. Essa classe representa um botão na irteface gráfica
class MyApp(App):
# Aqui se cria uma nova classe chamada MyApp que herda da classe App. Significa que MyApp é um aplicativo Kivy
    def build(self):
        return Button(text='''Hello World! This is
        my first program in kivy \n I´m a SESIANO 
        student, and I love my teacher''')
''' Este é um método dentro da classe MyApp. O método build é obrigatorio em qualquer aplicativo kivy. 
Ele é chamado quando o aplicativo é iniciado e deve retornar o widge '''
    
if __name__ == '__main__':
    MyApp().run()