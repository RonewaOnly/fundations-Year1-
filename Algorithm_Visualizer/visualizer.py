from tkinter import Canvas, Frame, Scrollbar, VERTICAL, HORIZONTAL, RIGHT, LEFT, BOTTOM, TOP, X, Y, BOTH
from tkinter import Tk, Button, Label, Entry, StringVar

import itertools, threading, time, sys
done = False
def animate():
   for c in itertools.cycle(['|', '/', '-', '\\']):
       if done:
           break
       sys.stdout.write(f'\rLoading Title Screen {c}')
       sys.stdout.flush()
       time.sleep(0.1)
   sys.stdout.write('\rWelcome to My Game! \n')
t = threading.Thread(target=animate)
t.start()
time.sleep(3) # Simulate loading
done = True
t.join()