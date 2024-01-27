from tkinter import *


def leftclick(event):
    print('leftclicked : ' + str(event.x) + "," + str(event.y))
    canvas.create_oval(event.x,
                       event.y,
                       event.x + 20,
                       event.y + 20,  # no parenthesis()
                       fill='white',
                       width=2)


def scroll(event):
    print('scrollclicked at : ' + str(event.x) + "," + str(event.y))


def rightclick(event):
    print('rightclicked : ' + str(event.x) + "," + str(event.y))
    canvas.create_oval(event.x,
                       event.y,
                       event.x + 20,
                       event.y + 20,  # no parenthesis()
                       fill='gold',
                       width=2)


def release(event):
    print('released at : ' + str(event.x) + "," + str(event.y))


def enter(event):
    print('Mouse entered window @ : ' + str(event.x) + "," + str(event.y))


def leave(event):
    print('Mouse leaved window @ : ' + str(event.x) + "," + str(event.y))


def constant(event):
    print('mouse is at : ' + str(event.x) + "," + str(event.y))
    canvas.create_oval(event.x,
                       event.y,
                       event.x + 10,
                       event.y + 10,  # no parenthesis()
                       fill='red',
                       width=2)


window = Tk()
window.title("Art maker")
canvas = Canvas(window, height=500, width=500)

# window.bind(key,function)
window.bind('<Button-1>', leftclick)  # left Click
window.bind('<Button-2>', scroll)  # Scroll Click
window.bind('<Button-3>', rightclick)  # right Click
window.bind('<ButtonRelease>', release)  # trigger when button is released
window.bind('<Enter>', enter)  # trigger when mouse enters to a window
window.bind('<Leave>', leave)  # trigger when mouse leaves from a window
window.bind('<Motion>', constant)  # TRACK MOUSE CONSTANTLY (Used in Games)

canvas.pack()
window.mainloop()
