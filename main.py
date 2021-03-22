from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip


def storeKey(k):
    if (os.path.exists("passwd")):
        pass
    else:
        t = open("passwd", "a")
        t.close()
    f=open("passwd", "wb")
    f.write(k)
    f.write(b'\n')
    f.close()
def checkExist():
    if (os.path.exists("passwd")):
        return True
    else:
        return False

def getKey():
    if(checkExist()):
        f=open("passwd","rb")
        k=f.read(77)
        f.close()
        return k
    else:
        messagebox.showwarning(title="Warning!",message="Can't find passwd file")
        return False

def storePasswd(name,passwd):
    if(checkExist()):
        f=open("passwd","ab+")
        f.write(name)
        f.write(b'\n')
        f.write(passwd)
        f.write(b'\n')
        f.close()
        messagebox.showinfo(title="Store",message="Sucessed!")
k=""
def getPasswds(key):
    if (checkExist()):
        d={"":""}
        f=open("passwd","rb")
        f.seek(45)
        t=f.readline().decode('ascii')
        c1 = t[:len(t)-1]
        while(c1!=""):
            t=f.readline().decode('ascii')
            c2=t[:len(t) - 1]
            d[decodeNP(key,c1)]=decodeNP(key,c2)
            t = f.readline().decode('ascii')
            c1 = t[:len(t) - 1]
        f.close()
        return d
def getPasswd(name):
    dic=getPasswds(k)
    res=dic[name]
    pyperclip.copy(res)
    messagebox.showinfo(title="Tip",message="Already cpoy to your clipboard!")

def encodeNP(key,s):
    f = Fernet(key)
    return f.encrypt(s.encode('ascii'))
def decodeNP(key,s):
    f = Fernet(key)
    return f.decrypt(s.encode('ascii')).decode('ascii')
def store(w):
    win=tk.Toplevel(w)
    storeGui(win)

def storeGui(win):
    win.title("Store Passwd")
    win.geometry("500x100")
    tip1=tk.StringVar()
    tip1.set('Password for:')
    tip1T = tk.Label(win, textvariable=tip1)
    tip1T.pack(side='left')
    t1 = tk.StringVar()
    t1.set('')
    name_text = tk.Entry(win, textvariable=t1)
    name_text.pack(side='left')

    tip2 = tk.StringVar()
    tip2.set(' Password:')
    tip2T= tk.Label(win, textvariable=tip2)
    tip2T.pack(side='left')

    t2 = tk.StringVar()
    t2.set('')
    passwd_text=tk.Entry(win, textvariable=t2)
    passwd_text.pack(side='left')

    b = ttk.Button(win, text="Store", width=7,
                   command=lambda: (storePasswd(encodeNP(k, name_text.get()), encodeNP(k, passwd_text.get())),win.destroy()))
    b.pack(side='right')
    win.mainloop()


def init():
    global k
    k = getKey()
    if(k==False):
        exit()

def mainGui(w):
    w.title("Safe Passwd")
    w.geometry("500x100")
    t1_1 = tk.StringVar()
    t1_1.set('Password for:')
    nameText = tk.Label(w, textvariable=t1_1)
    nameText.pack(side='left')
    t1 = tk.StringVar()
    t1.set('')
    name_text = tk.Entry(w, textvariable=t1)
    name_text.pack(side='left')
    b = ttk.Button(w, text="Get", width=7,
                   command=lambda:(getPasswd(name_text.get())))
    b.pack(side='right')
    s=ttk.Button(w, text="Store", width=7,
                   command=lambda:(store(w)))
    s.pack(side='right')
    w.mainloop()

if __name__=="__main__":
    #storeKey(Fernet.generate_key())
    init()
    window = tk.Tk()
    mainGui(window)
    # storePasswd(encodeNP(k,"Jim"),encodeNP(k,"123456"))
    # getPasswd(k)





