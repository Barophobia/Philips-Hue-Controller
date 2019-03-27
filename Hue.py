from phue import Bridge
import random
import tkinter
import tkinter.messagebox
import webbrowser

#GUI Stuff
top = tkinter.Tk()
top.geometry("400x330")
top.title('Hue Controller')
top.iconbitmap('ico_color2.ico')
colvar = tkinter.IntVar()

def lightoff():
	b.set_light([2,3],'on', False)

def lighton():
	b.set_light([2,3],'on', True)

def colourloop():
	b.set_light([2,3],{'effect':'colorloop'})

def noeffect():
	b.set_light([2,3],{'effect':'none'})

def randcol():
	for light in lights:
		light.brightness = 254
		light.xy = [random.random(),random.random()]

def bri():
	b.set_light([2,3],'bri', int(Bri.get()))

def selec():
	if int(colvar.get()) == 1:	
		b.set_light([2,3],{'xy':[0.25,0.25]})
	if int(colvar.get()) == 2:
		b.set_light([2,3],{'xy':[0.675, 0.322]})
	if int(colvar.get()) == 3:
		b.set_light([2,3],{'xy':[0.97, 0.97]})
	if int(colvar.get()) == 4:
		b.set_light([2,3],{'xy':[0.14,0.13]})
	if int(colvar.get()) == 5:
		b.set_light([2,3],{'xy':[0.409, 0.518]})
	if int(colvar.get()) == 6:
		b.set_light([2,3],{'xy':[0.36, 0.36]})

def bridgeip():
	contents = Ipe.get()
	print("connected to: " + Ipe.get())
	global b 
	b = Bridge(Ipe.get())
	lights = b.get_light_objects()
	b.connect()

new = 1
url = 'https://www.meethue.com/api/nupnp'
def hubip():
	webbrowser.open_new(url)

def credits():
	tkinter.messagebox.showinfo("Credits", "Created by George Rose - Ver. 270319")

#IP Input for hub
Ipframe = tkinter.LabelFrame(top, text = "Hub IP Address")
Ipe = tkinter.Entry(Ipframe, textvariable = "192.168.1.190")
Ipbutt = tkinter.Button(Ipframe, text = "Connect", command = bridgeip)
getipbutt = tkinter.Button(Ipframe, text = "Hub IP Info", command = hubip)
#Buttons
Buttframe = tkinter.LabelFrame(top, text = "Options")
Buttloff = tkinter.Button(Buttframe, text = "Off", command = lightoff, width = 25)
Buttlon = tkinter.Button(Buttframe, text = "On", command = lighton, width = 25)
Buttloop = tkinter.Button(Buttframe, text = "Colourloop", command = colourloop, width = 25)
Buttnone = tkinter.Button(Buttframe, text = "No Effect", command = noeffect, width = 25)
Buttrandom = tkinter.Button(Buttframe, text = "Random", command = randcol, width = 25)

#Brightness
Briframe = tkinter.LabelFrame(top, text = "Brightness (0-254)")
Bri = tkinter.Spinbox(Briframe, from_=0, to=254, width=17 , command = bri)

#Colour Choices
Colframe = tkinter.LabelFrame(top, text = "Colour Picker")
Col1 = tkinter.Radiobutton(Colframe, text ="Light Blue", variable = colvar, value = 1, command = selec)
Col2 = tkinter.Radiobutton(Colframe, text = "Red", variable = colvar, value = 2, command = selec)
Col3 = tkinter.Radiobutton(Colframe, text = "Yellow", variable = colvar, value = 3, command = selec)
Col4 = tkinter.Radiobutton(Colframe, text ="Purple", variable = colvar, value = 4, command = selec)
Col5 = tkinter.Radiobutton(Colframe, text = "Green", variable = colvar, value = 5, command = selec)
Col6 = tkinter.Radiobutton(Colframe, text = "White", variable = colvar, value = 6, command = selec)

#Credits
creds = tkinter.Button(top, text = "Credits", command = credits)

#GUI ORDERING 
#IP Input for Hub
Ipframe.pack(fill = None, expand = False)
Ipe.pack()
Ipbutt.pack(side='left', padx=2, pady=2)
getipbutt.pack(side='left', padx=2, pady=2)

#Buttons
Buttframe.place(x = 25, y = 75)
Buttlon.pack(padx=2, pady=2)
Buttloff.pack(padx=2, pady=2)
Buttloop.pack(padx=2, pady=2)
Buttnone.pack(padx=2, pady=2)
Buttrandom.pack(padx=2, pady=2)

#Brightness
Briframe.place(x = 135, y = 250)
Bri.pack(padx=2, pady=2)

#Colour Choices
Colframe.place(x= 225, y= 75)
Col1.pack()
Col2.pack()
Col3.pack()
Col4.pack()
Col5.pack()
Col6.pack()
label = tkinter.Label(top)
label.pack()
creds.pack(padx=2, pady=2, side = 'bottom')
top.mainloop()
