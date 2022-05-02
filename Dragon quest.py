from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.uix.button import Button
from kivy.core.window import Window




class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text="стерти все", on_press = self.clear_canvas, size = (100, 50), ))
        parent.add_widget(Button(text="ластик", on_press=self.clear, size=(100, 50), pos = (100, 0)))
        parent.add_widget(Button(text="зберегти", on_press=self.save, size=(100, 50), pos = (200, 0)))
        parent.add_widget(Button(background_color = [.25,.41,.88,1],  on_press=self.color,size=(100, 50), pos=(300, 0)))
        parent.add_widget(Button(background_color = [.88,.22,.26,1],  on_press=self.color2,size=(100, 50), pos=(400, 0)))
        parent.add_widget(Button(text="розмір +", on_press=self.size_plus, size=(100, 50), pos = (500, 0)))
        parent.add_widget(Button(text="розмір -", on_press=self.size_minus, size=(100, 50), pos=(600, 0)))
        parent.add_widget(Button(text="скинути розмір", on_press=self.reset, size=(100, 50), pos=(700, 0)))
        return parent
    def reset(self, instance):
        global size
        size = 10
    def size_plus(self, instance):
        global size
        size += 2
    def size_minus(self, instance):
        global size
        size -= 2
    def clear_canvas(self, instance):
        self.painter.canvas.clear()
    def save(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('image1.png')
    def color(self, instance):
        global zero
        zero = .25
        global two
        two = .41
        global three
        three = .88
        global four
        four = 1
    def clear(self, instance):
        global zero
        zero = .0
        global two
        two = .0
        global three
        three = .0
        global four
        four = 1
    def color2(self, instance):
        global zero
        zero = .88
        global two
        two = .22
        global three
        three = .26
        global four
        four = 1
global one
zero = 0
global two
two = 1
global three
three = 0
global four
four = 0
global size
size = 10
class PainterWidget(Widget):
         def on_touch_down(self, touch):
            with self.canvas:
                Color(zero, two, three,four)
                rad = size
                Ellipse(pos=(touch.x - rad / 2, touch.y - rad / 2), size=(rad, rad))
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=size)
         def on_touch_move(self, touch):
            touch.ud['line'].points += (touch.x, touch.y)


if __name__ == "__main__":
    PaintApp().run()

