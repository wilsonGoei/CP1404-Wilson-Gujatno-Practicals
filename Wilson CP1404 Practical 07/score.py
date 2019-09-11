from kivy.app import App
from kivy.lang import Builder



class BoxLayoutDemo(App):
    def build(self):
        self.title = "Score"
        self.root = Builder.load_file('score.kv')
        return self.root
    def handle_greet(self):
        score = int(self.root.ids.input_name.text)
        if score > 100 or score < 0:
            self.root.ids.output_label.text = 'Invalid input'
        elif score >= 65 and score <= 75:
            self.root.ids.output_label.text = 'Credit'
        elif score > 50:
            self.root.ids.output_label.text = 'Pass'
        else:
            self.root.ids.output_label.text = 'Fail'
    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your score'

BoxLayoutDemo().run()
