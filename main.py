# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# Set dark background
Window.clearcolor = get_color_from_hex('#000000')

class CalculatorApp(App):
    def build(self):
        self.title = "Simple Calculator"
        self.memory = 0
        self.last_result = 0
        self.result_displayed = False

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Display
        self.display = TextInput(
            text="",
            font_size=40,
            size_hint_y=None,
            height=100,
            halign="right",
            valign="middle",
            multiline=False,
            readonly=True,
            background_color=get_color_from_hex('#000000'),
            foreground_color=get_color_from_hex('#FFFFFF'),
        )
        self.display.bind(size=self._update_text_size)
        main_layout.add_widget(self.display)

        # Button layout
        buttons = [
            ['MC', 'MR', 'M+', 'M-'],
            ['C', 'CE', '←', '±'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=5)
            for label in row:
                button = Button(
                    text=label,
                    font_size=24,
                    background_color=get_color_from_hex('#333333'),
                    color=get_color_from_hex('#FFFFFF'),
                    size_hint=(0.25, 1)
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def _update_text_size(self, instance, value):
        instance.text_size = (instance.width, None)

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == '=':
            try:
                # Replace × and ÷ if used (not in your case, but safe)
                expr = current.replace('×', '*').replace('÷', '/')
                result = eval(expr)
                self.last_result = result
                self.display.text = str(result)
                self.result_displayed = True
            except Exception:
                self.display.text = "Error"
                self.result_displayed = False

        elif button_text == 'C':
            self.display.text = ""
            self.last_result = 0
            self.result_displayed = False

        elif button_text == 'CE':
            self.display.text = ""
            self.result_displayed = False

        elif button_text == '←':
            self.display.text = current[:-1]
            if not self.display.text:
                self.result_displayed = False

        elif button_text == '±':
            if current.startswith('-'):
                self.display.text = current[1:]
            else:
                self.display.text = '-' + current
            self.result_displayed = False

        elif button_text == 'MC':
            self.memory = 0

        elif button_text == 'MR':
            self.display.text = str(self.memory)
            self.result_displayed = True

        elif button_text == 'M+':
            try:
                self.memory += float(current if current else '0')
            except:
                pass

        elif button_text == 'M-':
            try:
                self.memory -= float(current if current else '0')
            except:
                pass

        else:
            # Regular input (digits, operators)
            if self.result_displayed and button_text not in '+-*/':
                self.display.text = ""
                self.result_displayed = False
            self.display.text += button_text

if __name__ == "__main__":
    CalculatorApp().run()
