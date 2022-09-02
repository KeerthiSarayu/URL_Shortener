import pyperclip 
import pyshorteners
from tkinter import *

gui = Tk()
gui.geometry('600x300')
gui.title("URL Shortener")
gui.configure(bg = '#FFFFD3')
url = StringVar()
url_address = StringVar()

def shorten():
    address = url.get()
    shortened = pyshorteners.Shortener().tinyurl.short(address)
    url_address.set(shortened)

def copyurl():
    shortened = url_address.get()
    pyperclip.copy(shortened)

Label(gui, text = 'Shorten your URLs', font = 'Times 20 italic bold').pack(pady = 10)
Entry(gui, textvariable = url).pack(pady = 5)
Button(gui, text = 'Get Shortened URL', command = shorten).pack(pady = 7)
Entry(gui, textvariable = url_address).pack(pady = 5)
Button(gui, text = "Copy URL", command = copyurl).pack(pady = 5)

gui.mainloop()