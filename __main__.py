from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('my2.kv')
expression = ''

class MyLayout(Widget):
    def press1(self):
        global expression
        expression = ''
        self.ids.Id_Label.text = expression
    def press2(self):
        global expression
        expression = expression[:len(expression)-1]
        self.ids.Id_Label.text = expression
    def press3(self):
        global expression
        expression += '%'
        self.ids.Id_Label.text = expression
    def press4(self):
        global expression
        expression += '**'
        self.ids.Id_Label.text = expression
    def press5(self):
        global expression
        expression += '7'
        self.ids.Id_Label.text = expression
    def press6(self):
        global expression
        expression += '8'
        self.ids.Id_Label.text = expression
    def press7(self):
        global expression
        expression += '9'
        self.ids.Id_Label.text = expression
    def press8(self):
        global expression
        expression += '/'
        self.ids.Id_Label.text = expression
    def press9(self):
        global expression
        expression += '4'
        self.ids.Id_Label.text = expression
    def press10(self):
        global expression
        expression += '5'
        self.ids.Id_Label.text = expression
    def press11(self):
        global expression
        expression += '6'
        self.ids.Id_Label.text = expression
    def press12(self):
        global expression
        expression += '*'
        self.ids.Id_Label.text = expression
    def press13(self):
        global expression
        expression += '1'
        self.ids.Id_Label.text = expression
    def press14(self):
        global expression
        expression += '2'
        self.ids.Id_Label.text = expression
    def press15(self):
        global expression
        expression += '3'
        self.ids.Id_Label.text = expression
    def press16(self):
        global expression
        expression += '-'
        self.ids.Id_Label.text = expression
    def press17(self):
        global expression
        expression += '0'
        self.ids.Id_Label.text = expression
    def press18(self):
        global expression
        expression += '.'
        self.ids.Id_Label.text = expression
    def press19(self):
        global expression
        try:
            expression = eval(expression)
        except ZeroDivisionError:
            expression='=Can\'t divide by zero'
        except SyntaxError:
            expression = 'Invalid Expression'
        except :
            expression = ''
        expression = str(expression)
        self.ids.Id_Label.text = expression
    def press20(self):
        global expression
        expression += '+'
        self.ids.Id_Label.text = expression
    

class my2App(App):
    def build(self):
        return MyLayout()


my2App().run()