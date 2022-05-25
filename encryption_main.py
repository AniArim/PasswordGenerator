"""
This program generate passwords for different website. Edit login and password to file and  with update in future will
sent file to lock server.
Search password and login for web.site in local password base (with update)
"""
import random
import easygui
import os
import shutil
import tkinter
from tkinter import *
from tkinter import Tk, messagebox
from tkinter.commondialog import Dialog

from libery_text import libery_text_final
from libery_text import libery_numbers_final
from libery_text import libery_symbol


class Message(Dialog):
    "A message box"
    command = "tk_messageBox"


password, login, web_site, args = None, None, None, None
answer = "high"

file = open("password.txt", "a+")
file.close()
path = os.path.abspath("password.txt")


def creat_file(event):
    """
    This function open windows explorer for chose txt file or creat.
    If file is not txt show exception window.

    :return: path. the way to local base
    """
    global path

    try:
        path = easygui.fileopenbox(default=f'{path}', filetypes='*.txt')
        while path.endswith(".txt") is not True:
            tkinter.messagebox.showwarning(title="Warning!", message=f"File have to be txt format.\n  Try again")
            path = easygui.fileopenbox(default=f'{path}', filetypes='*.txt')

        else:
            btn1.place_forget()
            Label1.place_forget()

            if path != os.path.abspath("password.txt"):
                os.remove(os.path.abspath("password.txt"))
            return path, window_2()
    except Exception:
        tkinter.messagebox.showwarning(title="Warning!", message=f"Something is wrong! \n Restart program")
        root.destroy()


def generate_list():
    """
    This function make list_finally with random digits, letters low, letters upper

    :return list_finally
    """
    list_1 = libery_text_final.upper()
    list_finally = list(libery_text_final + list_1 + libery_numbers_final)
    random.shuffle(list_finally)
    return list_finally


def answer_(arg):
    """
    This function assign variable "answer"  value of button used.

    :param arg: 1 = button"Low", 2 = button"high", 3 = button"with symbols". Look btn2, btn3, btn4.

    :return: global answer, call function make_local_BD()
    """
    global answer

    if arg == 1:
        answer = "Low"
    elif arg == 2:
        answer = "high"
    elif arg == 3:
        answer = "with symbol"
    else:
        answer = None
        Label6.place(width=180, height=20, x=200, y=100)
    return answer, make_local_BD()


def generate_password():
    """
    This function generate password with different password difficulty low or high or with symbol, depend which button
    used user. Look function answer_()
    This function call function generate_list()

    :return:password
    """
    global password

    if answer == "Low":
        password = ''.join([random.choice(generate_list()) for x in range(10)])
    elif answer == "high":
        password = ''.join(random.choice(generate_list()) for x in range(15))
    elif answer == "with symbol":  # Add symbols to password
        password = ''.join(random.choice(generate_list()) for x in range(15))
        symbol_tmp = ''.join(random.choice(libery_symbol) for x in range(random.randint(1, 4)))
        password = "".join(sorted((password + symbol_tmp), key=lambda k: random.random()))
    else:
        password = None
    return password


def check_web_site():
    """
    This function check user entry field "web_site".

    :return: web_site
    """
    global web_site
    web_site = Entry_web_site.get()

    try:
        if len(web_site) >= 3:
            if "." in web_site:
                check_login()
            else:
                tkinter.messagebox.showerror(title="Warning!", message=f"web site must have '.' \n Be attentive!")
                web_site = None
        else:
            tkinter.messagebox.showerror(title="Warning!", message=f"It's not web site. \n Don't waste my time!")
            web_site = None
    except:
        tkinter.messagebox.askquestion(title="Warning!", message=f"Sorry. We got Exception... \n Try again?")
        web_site = None
    return web_site


def check_login():
    """
    This function check user entry field "login"

    :return: login
    """
    global login
    login = Entry_login.get()
    try:
        if len(login) >= 2:
            if login.isalnum() or ("@" in login) is True:
                pass
            else:
                tkinter.messagebox.showerror(title="Warning!", message=f"Contains wrong symbols \n Try again")
                login = None
        else:
            tkinter.messagebox.showerror(title="Warning!", message=f"Login have to be longer \n Try again")
            login = None
    except:
        tkinter.messagebox.askquestion(title="Warning!", message=f"Sorry. We got Exception... \n Try again?")
    return login


def make_local_BD():
    """
    Function make local date. Add web_site, login, password to file on way  that was created by function creat_file().
    Call function for check date from users. Entry field "Web_site" and "login" don't have to be empty.
    """
    check_web_site()
    if web_site is not None and login is not None:
        with open(path, 'a+') as local_base:
            try:
                local_base.write(f"{web_site},{login},{str(generate_password())}\n")
                return window_3()
            except Exception:
                tkinter.messagebox.showerror(title="Warning!", message=f"We got IOError! \n Try again")
    else:
        pass


def window_1():
    """
    This function open first window. Call function creat_file()

    :return:
    """

    Label1.place(width=400, height=50, x=0, y=30)
    btn1.place(width=100, height=50, x=160, y=100)
    btn1.bind("<Button-1>", creat_file)
    return


def window_2():
    """
    This function create labels, buttons for windows 2.

    :return:
    """

    Label5.place(width=400, height=20, x=0, y=20)
    Label2.place(width=120, height=20, x=0, y=40)
    Label3.place(width=100, height=20, x=0, y=70)

    Entry_web_site.place(width=220, height=20, x=150, y=50)
    Entry_login.place(width=220, height=20, x=150, y=80)
    window_2_check()


def window_2_check():
    Label11.place(width=318, height=20, x=0, y=110)

    btn10.place(width=70, height=30, x=150, y=140)
    btn10.bind("<Button-1>", check_for_availability)
    btn11.place(width=70, height=30, x=300, y=140)
    btn11.bind("<Button-1>", window_2_close)


def window_2_close(event):
    Label11.place_forget()

    btn10.place_forget()
    btn11.place_forget()

    return window_2_open()


def window_2_open():
    Label4.place(width=180, height=20, x=0, y=100)

    btn2.place(width=70, height=30, x=150, y=110)
    btn3.place(width=70, height=30, x=225, y=110)
    btn4.place(width=70, height=30, x=302, y=110)


def window_3():
    """
    This function creat labels and buttons on window #3.
    If user want make new password for another web_site call function window_2.
    If user finished close program

    :return:
    """
    try:
        Label5.place_forget()
        Label4.place_forget()

        btn2.place_forget()
        btn3.place_forget()
        btn4.place_forget()

        Entry_web_site.delete(0, "end")
        Entry_web_site.place_forget()
        Entry_login.delete(0, "end")
        Entry_login.place_forget()

    except Exception:
        pass

    Label8.place(width=400, height=20, x=10, y=10)
    Label8.configure(text="Generation completed. What next?")
    Label10.place(width=120, height=20, x=0, y=100)

    show_web_site.place(width=220, height=20, x=130, y=40)
    show_web_site["text"] = web_site

    show_login.place(width=220, height=20, x=130, y=70)
    show_login["text"] = login

    show_password.place(width=220, height=20, x=130, y=100)
    show_password["text"] = password

    btn5.place(width=100, height=50, x=275, y=140)  # Continue button
    btn6.place(width=100, height=50, x=150, y=140)  # Exit button
    btn12.place(width=100, height=50, x=25, y=140)  # Refresh button

    btn7.place(width=30, height=20, x=360, y=40)  # Button for img
    btn8.place(width=30, height=20, x=360, y=70)  # Button for img
    btn9.place(width=30, height=20, x=360, y=100)  # Button for img

    btn_image.place(width=30, height=20, x=360, y=40)  # Img copy and function copy to clipboard web.site
    btn_image2.place(width=30, height=20, x=360, y=70)  # Img copy and function copy to clipboard Login
    btn_image3.place(width=30, height=20, x=360, y=100)  # Img copy and function copy to clipboard password


def window_continue():
    """
    This function delete widgets and open window 2 for create new password.
    :param event: <Button-1> on btn5

    :return: window_2()
    """

    Label8.place_forget()
    Label10.place_forget()

    show_web_site.place_forget()
    show_login.place_forget()
    show_password.place_forget()

    btn5.place_forget()
    btn6.place_forget()
    btn7.place_forget()
    btn8.place_forget()
    btn9.place_forget()
    btn12.place_forget()
    btn_image.place_forget()
    btn_image2.place_forget()
    btn_image3.place_forget()

    return window_2()


def copy(arg):
    """
    This function clear clipboard. Copy web_site or login or password, depend which button we use and which line copy
    need.

    :param arg: 1 = txt. web_site", 2 = txt.login, 3 = txt.password". Look btn7, btn8, btn9.

    :return: global args
    """
    global args
    root.clipboard_clear()

    if arg == 1:
        args = root.clipboard_append(show_web_site['text'])
    elif arg == 2:
        args = root.clipboard_append(show_login['text'])
    elif arg == 3:
        args = root.clipboard_append(show_password['text'])
    else:
        args = None
        tkinter.messagebox.showerror(title="Warning!", message="Unexpected Error! Can't copy.")
    return args


def check_for_availability(event):
    """
    This function chek for availability web_site in txt file.
    :param path from creat_file():

    :return: window_2_open() or window_3()
    """
    global web_site, login, password, path

    check_web_site()
    if web_site is not None and login is not None:
        with open(f"{path}", "r", encoding="utf-8") as file1:
            for line in file1:
                if str(web_site) not in line:
                    pass
                else:
                    web_site, login, password = [str(i) for i in line.strip("\n").split(sep=",")]  # assign
                    # the string value
                    Label11.place_forget()
                    btn10.place_forget()
                    btn11.place_forget()
                    return window_3()

    Label11.place_forget()
    btn10.place_forget()
    btn11.place_forget()
    return window_2_open()


def refresh():
    """
    This function create new working.txt file for copy all information except line (web.site, password, login)
    what user want change/refresh. Next step - call function for generate new password.
    After copy done program delete working.txt file.

    :return:
    """
    global web_site, path, password, login

    with open(f"{path}", "r", encoding="utf-8") as file_, open("working_file.txt", "w", encoding="utf-8") as working:
        key_for_search = True
        while key_for_search:
            for line in file_:
                if str(web_site) not in line:
                    working.write(line)
                else:
                    key_for_search = False
    shutil.move("working_file.txt", f"{path}")

    generate_password()

    if web_site is not None and login is not None and password is not None:
        with open(path, 'a+') as local_base:
            try:
                local_base.write(f"{web_site},{login},{password}\n")
            except Exception:
                tkinter.messagebox.showerror(title="Warning!", message=f"We got IOError! \n Try again")
    else:
        tkinter.messagebox.showerror(title="Warning!", message="Unexpected Error!")
        root.destroy()

    show_web_site["text"] = web_site
    show_login["text"] = login
    show_password["text"] = password
    Label8.configure(text="Refreshing completed. What next?")


root = Tk()
root.attributes("-topmost", True)  # Place a window on top of other windows
root.config(cursor="hand2 white")
root.tk_focusFollowsMouse()

root.title("Password generator Application")
root.maxsize(width=400, height=200)
root.minsize(width=400, height=200)

canvas = Canvas(root, width=400, height=200)
canvas.place(x=0, y=0)
image_ = PhotoImage(file="icon1.png")
canvas.create_image(20, 20, image=image_)

frame = Frame(root, width=400, height=400, bg="black")
frame.place(width=400, height=400)

Label1 = Label(root, bg="black", fg="white", width=40, font=("Helvetica", 15), text="Chose directory for save/open"
                                                                                    " file:")
Label2 = Label(root, bg="black", fg="white", width=400, font=("Helvetica", 10), text="Web.site:")
Label3 = Label(root, bg="black", fg="white", width=400, font=("Helvetica", 10), text="Login:")
Label4 = Label(root, bg="black", fg="white", width=400, font=("Helvetica", 10), text="Password difficulty:")
Label5 = Label(root, bg="black", fg="white", width=400, font=("Helvetica", 12), text="Type your personality info:")
Label6 = Label(root, bg="black", fg="red", width=400, font=("Helvetica", 10), text="Warning!!! Error of answer!")
Label7 = Label(root, bg="black", fg="red", width=200, font=("Helvetica", 10), text="Line have to be not empty!")
Label8 = Label(root, bg="black", fg="red", width=200, font=("Helvetica", 15), text="Generation completed. What next?")
Label10 = Label(root, bg="black", fg="white", width=400, font=("Helvetica", 10), text="Password:")
Label11 = Label(root, bg="black", fg="white", width=400, font=("Helvetica", 10), text="Check for password in file for "
                                                                                      "this web site?", justify="left")

show_web_site = Label(root, bg="white", fg="black", width=160, font=("Helvetica", 10), bd=3)
show_login = Label(root, bg="white", fg="black", width=160, font=("Helvetica", 10), bd=3)
show_password = Label(root, bg="white", fg="black", width=160, font=("Helvetica", 10), bd=3)

Entry_web_site = Entry(root, bg="black", fg="white", width=40, bd=3,
                       insertbackground="white")  # insertbackground = white color for see cursor
Entry_login = Entry(root, bg="black", fg="white", width=40, bd=3, insertbackground="white")

btn1 = Button(root, text="OK", font=("Helvetica", 25), bg="black", fg="white")
btn2 = Button(root, text="Low", font=("Helvetica", 8), bg="black", fg="white", command=lambda: answer_(1))
btn3 = Button(root, text="High", font=("Helvetica", 8), bg="black", fg="white", command=lambda: answer_(2))
btn4 = Button(root, text=r"Symbols +", font=("Helvetica", 8), bg="black", fg="white", command=lambda: answer_(3))
btn5 = Button(root, text="Continue", font=("Helvetica", 15), bg="black", fg="white", command=window_continue)
btn6 = Button(root, text="Exit", font=("Helvetica", 15), bg="black", fg="white", command=root.destroy)
btn10 = Button(root, text="Yes", font=("Helvetica", 15), bg="black", fg="white")
btn11 = Button(root, text="No", font=("Helvetica", 15), bg="black", fg="white")
btn12 = Button(root, text="Refresh", font=("Helvetica", 15), bg="black", fg="white", command=refresh)

btn7 = Button(root, bg="white", fg="black")
btn8 = Button(root, bg="white", fg="black")
btn9 = Button(root, bg="white", fg="black")

btn_image = Button(root, image=image_, command=lambda: copy(1))
btn_image2 = Button(root, image=image_, command=lambda: copy(2))
btn_image3 = Button(root, image=image_, command=lambda: copy(3))

window_1()

root.mainloop()
