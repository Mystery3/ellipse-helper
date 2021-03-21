'''
Author = Flaps#9562
Year = 2021
Function = Returns a grid of pixels to help with making circles and ellipses in block-based games or in pixel art.
'''

import tkinter as tk

# for ellipse showing
def BoxInput():

    # get from entries
    a = float(widthbox.get())/2
    b = float(heightbox.get())/2

    # define extras for later use
    inta = int(a)
    intb = int(b)
    maxab = int(max([a, b]))

    # adjust grid screen size
    scrsize = "%dx%d" % (inta * 10 + 20, intb * 10 + 20)

    # ellipse screen
    gridscreen = tk.Tk()
    gridscreen.title("Your Ellipse")
    gridscreen.geometry(scrsize)
    gridframe = tk.Frame(gridscreen)

    '''
    # scrollbars
    vscroll = tk.Scrollbar(gridscreen, orient = "vertical")
    vscroll.pack(side = "right", fill = "y")
    hscroll = tk.Scrollbar(gridscreen, orient = "horizontal")
    hscroll.pack(side = "bottom", fill = "x")
    '''
    # lists and variables
    elements = []
    xlist = []
    ylist = []
    xcount = 0
    ycount = 0
    color1 = "blue"
    color2 = "red"

    # for each coordinate, check if the coordinate in between the ellipse that is 1 block taller & wider and the ellipse that is 1 block shorter & less wide, append a frame object if true and append coordinates
    for x in range(1, maxab + 1):
        for y in range(1, maxab + 1):
            if (x**2 / (a + .5)**2) + (y**2 / (b + .5)**2) < 1 and (x**2 / (a - .5)**2) + (y**2 / (b - .5)**2) > 1:
                elements.append(tk.Frame(gridframe, width = 10, height = 10))
                xlist.append(x)
                ylist.append(y)
                
    # display each saved frame
    for frame in elements:
        color1, color2 = color2, color1
        frame.config(bg = color1)
        frame.grid(column = xlist[xcount], row = ylist[ycount])
        ycount+= 1
        xcount+= 1

    # pack
    gridframe.pack()

# start menu

# create and name window
root = tk.Tk()
root.title("Ellipse")
root.geometry("500x200")

# start frame
menuframe = tk.Frame(root)

# height
heightlabel = tk.Label(menuframe, text = "Enter Height.")
heightlabel.grid(column = 0, row = 0, padx = 20, pady = 20)

heightbox = tk.Entry(menuframe, width = 20)
heightbox.grid(column = 0, row = 1, padx = 20)

# width
widthlabel = tk.Label(menuframe, text = "Enter Width.")
widthlabel.grid(column = 2, row = 0, padx = 20, pady = 20)

widthbox = tk.Entry(menuframe, width = 20)
widthbox.grid(column = 2, row = 1, padx = 20)

# go
startbutton = tk.Button(menuframe, text = "Go!", width = 40, command = lambda:BoxInput())
startbutton.grid(column = 0, columnspan = 3, row = 2, padx = 20, pady = 60)

# initiate
menuframe.pack()

# loop
root.mainloop()