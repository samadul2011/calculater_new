import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock
import math

# Configure Kivy
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', False)

class CalculatorWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]
        self.spacing = 5
        
        # Calculator state
        self.memory = 0
        self.last_result = 0
        self.result_displayed = False
        
        # Create display
        self.display = TextInput(
            text='',
            font_size=32,
            size_hint_y=None,
            height=60,
            background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
            readonly=True,
            multiline=False,
            halign='right',
            valign='middle'
        )
        self.add_widget(self.display)
        
        # Create button grid
        button_layout = GridLayout(
            cols=4,
            spacing=5,
            size_hint_y=None,
            height=300
        )
        
        # Button texts and their respective functions
        buttons = [
            ('MC', 'MR', 'M+', 'M-'),
            ('C', 'CE', '←', '±'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        
        # Create buttons
        for row in buttons:
            for button_text in row:
                btn = Button(
                    text=button_text,
                    font_size=20,
                    background_color=(0.2, 0.2, 0.2, 1),
                    color=(1, 1, 1, 1),
                    size_hint_y=None,
                    height=50
                )
                btn.bind(on_press=lambda x: self.button_press(x.text))
                button_layout.add_widget(btn)
        
        self.add_widget(button_layout)
        
        # Bind keyboard events
        Window.bind(on_keyboard=self.on_keyboard)
        
        # Set focus to capture keyboard events
        Clock.schedule_once(lambda dt: self.display.focus_set(), 0.1)
    
    def on_keyboard(self, window, key, *args):
        """Handle keyboard input"""
        key_code = key
        
        # Handle number keys (48-57 are number keys)
        if 48 <= key_code <= 57:
            if self.result_displayed:
                self.display.text = ''
                self.result_displayed = False
            self.display.text += str(key_code - 48)
        # Handle operators
        elif key_code in [43, 45, 42, 47, 46, 61]:  # +, -, *, /, ., =
            if key_code == 46:  # Period
                if self.result_displayed:
                    self.display.text = ''
                    self.result_displayed = False
                self.display.text += '.'
            elif key_code == 61:  # Equals
                self.button_press('=')
            else:  # Other operators
                self.result_displayed = False
                operators = {43: '+', 45: '-', 42: '*', 47: '/'}
                self.display.text += operators[key_code]
        # Handle special keys
        elif key_code == 32:  # Space (could be used for equals)
            self.button_press('=')
        elif key_code == 8:   # Backspace
            text = self.display.text
            if len(text) > 0:
                self.display.text = text[:-1]
                if not self.display.text:
                    self.result_displayed = False
        elif key_code == 27:  # Escape
            self.button_press('C')
        
        return True
    
    def button_press(self, button_text):
        """Handle button press"""
        current = self.display.text
        
        if button_text == '=':
            self.calculate()
        elif button_text == 'C':
            self.clear()
        elif button_text == 'CE':
            self.display.text = ''
            self.result_displayed = False
        elif button_text == '←':
            if current:
                self.display.text = current[:-1]
                if not self.display.text:
                    self.result_displayed = False
        elif button_text == '±':
            self.toggle_sign()
        # Memory functions
        elif button_text == 'MC':
            self.memory = 0
        elif button_text == 'MR':
            self.display.text = str(self.memory)
            self.result_displayed = True
        elif button_text == 'M+':
            try:
                self.memory += float(current)
            except:
                pass
        elif button_text == 'M-':
            try:
                self.memory -= float(current)
            except:
                pass
        else:
            # Handle digits and decimal point
            if self.result_displayed:
                self.display.text = ''
                self.result_displayed = False
            self.display.text += button_text
    
    def calculate(self):
        """Perform calculation"""
        try:
            # Replace operators for Python eval
            expression = self.display.text.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            self.last_result = result
            self.display.text = str(result)
            self.result_displayed = True
        except Exception as e:
            self.display.text = "Error"
            self.result_displayed = False
    
    def clear(self):
        """Clear display and reset state"""
        self.display.text = ''
        self.last_result = 0
        self.result_displayed = False
    
    def toggle_sign(self):
        """Toggle positive/negative sign"""
        try:
            if self.display.text.startswith('-'):
                self.display.text = self.display.text[1:]
            elif self.display.text:
                self.display.text = '-' + self.display.text
            self.result_displayed = False
        except:
            pass

class CalculatorApp(App):
    def build(self):
        # Set app properties
        self.title = "Calculator"
        self.icon = 'icon.png'
        
        # Return the calculator widget
        return CalculatorWidget()
    
    def on_start(self):
        # This method is called when the app starts
        pass

if __name__ == '__main__':
    CalculatorApp().run()
