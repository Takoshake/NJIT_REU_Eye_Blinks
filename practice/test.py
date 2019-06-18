#import kivy  # importing main package
#from kivy.app import App  # required base class for your app.
#from kivy.uix.videoplayer import VideoPlayer
#from kivy.uix.gridlayout import GridLayout
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation


#kivy.require("1.11.0")  # make sure people running py file have right version

#fig, ax = plt.subplots()

#x = np.arange(0, 2*np.pi, 0.01)
#line, = ax.plot(x, np.sin(x))


#def init():  # only required for blitting to give a clean slate.
    #line.set_ydata([np.nan] * len(x))
    #return line,


#def animate(i):
    #line.set_ydata(np.sin(x + i / 100))  # update the data.
    #return line,


#ani = animation.FuncAnimation(
    #fig, animate, init_func=init, interval=2, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

#plt.show()


#video = VideoPlayer(source='2019-06-13 14-35-16.flv', play=True)


#class MainWindow(GridLayout):
    #def __init__(self, **kwargs):
        #super().__init__(**kwargs)

        #self.rows = 2
        #self.add_widget(video)
        #self.add_widget(FigureCanvasKivyAgg(plt.gcf()))



#class EpicApp(App):
    #def build(self):
        #return MainWindow()


# Run the app.
#if __name__ == "__main__":
    #EpicApp().run()

import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
canvas = fig.canvas


class MyApp(App):
    def build(self):
        box = BoxLayout()
        self.i = 0
        self.line = [self.i]
        box.add_widget(canvas)
        #plt.show()
        Clock.schedule_interval(self.update, 1)
        return box

    def update(self, *args):
        plt.plot(self.line, self.line)
        self.i += 1
        self.line.append(self.i)
        canvas.draw_idle()


MyApp().run()
