#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class Example(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Dynamic Routing-RYU Controller-OpenvSwitch")
        
        # Setup Canvas and use grid instead of pack
        self.canvas = Canvas(self, width=200, height=100)
        self.canvas.grid(row=0, column=0, columnspan=3, sticky=E+W+S+N)

        # Uncomment and adjust path to use an image
        # self.image = ImageTk.PhotoImage(file="/path/to/your/image.jpg")
        # self.canvas.create_image(10, 10, image=self.image, anchor=NW)

        # Grid configuration for layout
        self.columnconfigure(0, pad=10)
        self.columnconfigure(1, pad=10)
        self.columnconfigure(2, pad=10)
        
        self.rowconfigure(1, pad=10)
        self.rowconfigure(2, pad=10)
        self.rowconfigure(3, pad=20)

        # Define button actions
        def m1():
            exec(open("/home/onos/dynamic_routing/mininet/SDN-Project/ryu/Run_topo.py").read())
        c1 = Button(self, text="Create Mininet Topology", command=m1)
        c1.grid(row=1, column=0, padx=10, pady=10, sticky=E+W+S+N)

        def m2():
            exec(open("/home/onos/dynamic_routing/mininet/SDN-Project/ryu/Run_controller.py").read())
        c2 = Button(self, text="Run Controller", command=m2)
        c2.grid(row=1, column=1, padx=10, pady=10, sticky=E+W+S+N)

        def m3():
            exec(open("/home/onos/dynamic_routing/mininet/SDN-Project/ryu/Run_dumper.py").read())
        c3 = Button(self, text="Log Link Details", command=m3)
        c3.grid(row=1, column=2, padx=10, pady=10, sticky=E+W+S+N)

        def m4():
            exec(open("/home/onos/dynamic_routing/mininet/SDN-Project/ryu/Run_shortest_path.py").read())
        c4 = Button(self, text="Run Shortest Path", command=m4)
        c4.grid(row=2, column=0, padx=10, pady=10, sticky=E+W+S+N)

        def m5():
            exec(open("/home/onos/dynamic_routing/mininet/SDN-Project/ryu/5.py").read())
        c5 = Button(self, text="Use Table to Run Flows", command=m5)
        c5.grid(row=2, column=1, padx=10, pady=10, sticky=E+W+S+N)

        def m6():
            import sys
            sys.exit()
        c6 = Button(self, text="Exit", command=m6)
        c6.grid(row=3, column=1, padx=30, pady=30, sticky=E+W+S+N)

        def m9():
            exec(open("/home/onos/dynamic_routing/mininet/SDN-Project/ryu/remove.py").read())
        c9 = Button(self, text="Delete Log Files", command=m9)
        c9.grid(row=2, column=2, padx=10, pady=10, sticky=E+W+S+N)

        self.grid(row=0, column=0, sticky=N+S+E+W)

def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()

