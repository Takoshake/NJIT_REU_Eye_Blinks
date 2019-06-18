import kivy  # importing main package
import matplotlib.pyplot as plt
from kivy.app import App  # required base class for your app.
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.gridlayout import GridLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


kivy.require("1.11.0")  # make sure people running py file have right version

video = VideoPlayer(source='2019-06-13 14-35-16.flv', play=True)


plt.plot([1, 23, 2, 4])
plt.ylabel('some numbers')


class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.rows = 2
        self.add_widget(video)
        self.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class EpicApp(App):
    def build(self):
        return MainWindow()


# Run the app.
if __name__ == "__main__":
    EpicApp().run()
