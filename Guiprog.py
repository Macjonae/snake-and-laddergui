from tkinter import *
import tkinter as tk
from tkinter import messagebox

def snakegame():
    print('Snake and Ladder Game')

def StartGame():
    print('Play')

def newgame():
    print('New Game')

def score():
    print('High Score')

def aboutus():
    print('About Game')

def Help():
    print('Help')    

def Exit():
    print('Goodbye')


def userprofile():
    global userprofilewin
    userprofilewin = Toplevel()
    userprofilewin.title('User Profile')
    userprofilewin.geometry("500x500+500+100")

    menubar = Menu(userprofilewin)
    userprofilewin.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label ='File', menu=filemenu)
    filemenu.add_command(label='Snake and Ladder Game',command =snakegame)
    filemenu.add_command(label='Play', command=StartGame)
    filemenu.add_command(label='New Game', command=newgame)
    filemenu.add_command(label='High Score', command=score)
    filemenu.add_command(label='About us', command=aboutus)
    filemenu.add_command(label='Help', command=Help)
    filemenu.add_command(label='Exit', command=Exit)

    tk.Label(userprofilewin, text='Welcome '+signin_username.get(), font ="none 20 bold"). place(x=100, y=10)

    userprofilewin.mainloop()




def login():
    loginfile  = open("game_register.txt","r")

    for line in loginfile:
        if ':' in line:
            key,value = line.split(':',1)
            cvalue = len(value)-1
            value = value[0:cvalue]
            user_dictionary[key] = value
        else:
            pass
    temp_username = user_dictionary.get('username')
    temp_password = user_dictionary.get('password')
    if(temp_username == signin_username.get() and temp_password ==signin_pwd.get()):
        userprofile()
    else:
        messagebox.showinfo("information", "Incorrect password or username")
    loginfile.close()
        


def signin():
    global signin_frame, signin_username, signin_pwd
    signin_frame = Toplevel()
    signin_username = StringVar()
    signin_pwd= StringVar()
    
    signin_frame.title("Sign in Section")
    signin_frame.geometry("500x500+500+100")
    signin_img = PhotoImage(file='signin.png')
    Label(signin_frame,  image=signin_img).place(x = 110, y = 15)
    Label(signin_frame, text = "Username").place(x=130,y=200)
    entry_username = Entry(signin_frame, width=20, textvariable=signin_username)
    entry_username.place(x=120, y=220)

    Label(signin_frame, text = "Password").place(x=120,y=260)
    entry_pwd = Entry(signin_frame, width=20, show="*", textvariable=signin_pwd)
    entry_pwd.place(x=120, y=280)
    
    btn_login = PhotoImage(file='imgsignin.png')
    tk.Button(signin_frame,bg='#ffffff', image = btn_login, highlightbackground='#ffffff', highlightcolor ='#ffffff',
                   highlightthickness=0,  command=login).place (x = 130, y = 310)

    entry_username.focus()
    entry_pwd.focus()
    signin_frame.mainloop()

def register():
    registerfile = open("game_register.txt","w")
    extract_username = reg_username.get()
    extract_pwd = reg_pwd.get()
    extract_fname= reg_fname.get()
    extract_lname= reg_lname.get()
    extract_phone= reg_phone.get()



    user_dictionary['username'] = extract_username
    user_dictionary['password'] = extract_pwd
    user_dictionary['first name']= extract_fname
    user_dictionary['last name']= extract_lname
    user_dictionary['phone']= extract_phone


    
    for key,value in user_dictionary.items():
        registerfile.write('%s:%s\n'%(key,value))
    registerfile.close()
    messagebox.showinfo("information", "Your account has been successfully created")

    reg_username.set("")
    reg_pwd.set("")
    reg_fname.set("")
    reg_lname.set("")
    reg_phone.set("")

def signup(event):
    global reg_fname, reg_lname, reg_username, reg_pwd, reg_phone
    regwin = Toplevel()

    reg_fname = StringVar()
    reg_lname = StringVar()
    reg_username = StringVar()
    reg_pwd = StringVar()
    reg_phone = StringVar()
    regwin.title("Registration")
    regwin.geometry("500x600+500+100")
    img = PhotoImage(file='signup.png')
    Label(regwin,  image=img).place(x = 140, y = 5)
    

    Label(regwin, text = "Username").place(x=120,y=200)
    reguname = Entry(regwin, width=20, textvariable=reg_username)
    reguname.place(x=120, y=220)

    Label(regwin, text = "Password").place(x=120,y=260)
    regpwd = Entry(regwin, width=20, show="*",textvariable=reg_pwd)
    regpwd.place(x=120, y=280)

    Label(regwin, text = "First Name").place(x=120,y=320)
    regfname = Entry(regwin, width=20, textvariable=reg_fname)
    regfname.place(x=120, y=340)

    Label(regwin, text = "Last Name").place(x=120,y=380)
    reglname = Entry(regwin, width=20, textvariable=reg_lname)
    reglname.place(x=120, y=400)

    Label(regwin, text = "Phone").place(x=120,y=440)
    regphone = Entry(regwin, width=20, textvariable=reg_phone)
    regphone.place(x=120, y=460)

    reguname.focus()

    Button(regwin, text="Register", command = register).place(x=250, y = 500)
    

    regwin.mainloop()


user_dictionary = { }
winframe = tk.Tk()
winframe.title("My first GUI program")
winframe.geometry("400x400+500+150")
winframe['background'] = '#aadc23'
lblimage = PhotoImage(file='snake.png')
Label(winframe, text="Snake and Ladder Game", bg='#aadc23',fg='#020100', font =('Time New Roman', 18, 'bold')).place(x=65, y=10)

Label(winframe, bg='#aadc23', image=lblimage).place(x=100, y=70)


btn_signin = PhotoImage(file='imgsignin.png')
tk.Button(winframe,  bg='#aadc23', image = btn_signin, highlightbackground='#aadc23', highlightcolor ='#aadc23',
                   highlightthickness=0,  command=signin).place (x = 130, y = 310)

lbl_signup = Label(winframe, text="Don't have an Account? Create an Account", bg='#aadc23', fg='#0c043e', cursor="hand2")
lbl_signup.place(x=65, y=360)
lbl_signup.bind("<Button-1>",signup)
winframe.mainloop()
