from kivy.app import App
from kivy.lang import Builder
class TemperaturesConverterApp(App):
    def build(self):
        self.title = "Temperatures Converter"
        self.root = Builder.load_file('temperatures.kv')
        return self.root

    def get_validated_number(self):
        try:
            number = float(self.root.ids.input_number.text)
            return number
        except ValueError:
            return 0.0

    def celcius_to_fahrenheit(self):
        celcius = self.get_validated_number()
        fahrenheit = celcius * 9.0 / 5 + 32
        self.root.ids.output_label.text = str(fahrenheit)

    def fahrenheit_to_celcius(self):
        fahrenheit = self.get_validated_number()
        celcius = 5 / 9 * (fahrenheit - 32)
        self.root.ids.output_label.text = str(celcius)
TemperaturesConverterApp().run()

