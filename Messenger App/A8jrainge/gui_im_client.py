# Justin Rainge, CIS 345, 12:00-1:15pm, A8

from socket import *
from threading import Thread
from tkinter import *
from tkinter import ttk, messagebox

PORT = 49000
BUFSIZE = 1024
EXIT = '[Q]'

global socket, IPaddress, screen_name, connect_disconnectbutton, window,chat_frame

def connect():
    global socket, IPaddress, screen_name, connect_disconnectbutton, window,chat_frame


    if len(IPaddress)> 6 and screen_name == '':
        try:
            ADDR = (IPaddress, PORT)
            socket = socket(AF_INET, SOCK_STREAM)
            socket.bind(ADDR)
            socket.send(screen_name.encode())
        except:
            socket.close()
            socket = None
        else:
            X = Thread(target=receive_msg, daemon=True)
            X.start()
    else:
        messagebox.showinfo('Error, you have entered the data incorrectly')

    window.geometry("300x500")
    connect_disconnectbutton = Button(bg="blue", text="Disconnect", command=disconnect)
    chat_frame.grid(sticky=N + S + W + E)



def disconnect():
    global socket,screen_name, connect_disconnectbutton, window,chat_frame
    try:
       socket.send(EXIT.encode())
    except:
        pass
    finally:
        socket = None
        socket.close()

    button = Button(window,text="Connect",bg="SystemButtonFace",command=connect)
    button.grid_forget()
    window.geometry("350x200")



def receive_msg():
    global socket, screen_name
    while True:
        try:
            received_message = socket.recv(1024)
        except OSError:
            received_message=None
        if not received_message:
            disconnect()
            break
    received_message.decode()



def send_msg():
    global socket, entered_message
    message = StringVar()
    message.get(entered_message)
    if message == '[Q]':
        disconnect()
    else:
        try:
            socket.send(message.encode())
        except OSError:
            disconnect()
    message.set('')




def window_closing(event=None):
    if socket == True:
        disconnect()
    window.quit()


def ip_key_entry(event):
    valid_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '\b', '']
    if event not in valid_keys:
        return 'break'
    else:
        pass

window = Tk()
window.config(bg = 'green')
window.title("CIS IM Client")
window.geometry('400x300')

ip_address= StringVar()
screenname= StringVar()
entry_box = StringVar()

fLbl= Label(window, text='Ip Address',justify=LEFT)
fLbl.grid()
fEntry = Entry(window, textvariable=ip_address,justify=LEFT)
fEntry.grid(row= 1,column=1)
lLbl= Label(window, text='Screen Name',justify=LEFT)
lLbl.grid()
fEntry = Entry(window, textvariable=screenname,justify=LEFT)
fEntry.grid(row= 2,column=1)
frame = Frame(window)
frame.grid()
scrollbar = Scrollbar(window)
Lb1 = Listbox(window,yscrollcommand=scrollbar.set)
scrollbar.grid()
scrollbar.config(command= Lb1.yview)
eEntry = Entry(window, textvariable=entry_box,justify=CENTER)
eEntry.grid()
button = Button(window, text ="Send Message", command = send_msg)
button.grid()
window.protocol('WM_DELETE_WINDOW',window_closing)





window.mainloop()