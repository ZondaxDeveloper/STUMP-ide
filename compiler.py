from tkinter import *
from tkinter.messagebox import showwarning
import tkinter.filedialog
from tkinter.filedialog import *
from os import *
from sys import*
from io import *
from platform import *
user_windows = popen("echo %USERNAME%").read()

root = Tk()
root.title("STUMP-LW")
root.iconbitmap("icon.ico")
root.geometry("200x200")

yes_python = popen("python --version")
if str(yes_python).startswith("\"python\""):
    showwarning("Install python: with command = pip install python")
    if platform.system() == 'Windows':
        os.system("start powershell")
    root.destroy()
    exit()


def traduct(archivo=("stmp.STMP_sc")):
    archivo_abierto = open(archivo, "r")
    content = archivo_abierto.read()
    archivo_abierto.close()
    content = content.replace("prt","print")
    content = content.replace("integer","int")
    content = content.replace("string","str")
    content = content.replace("flt","float")
    content = content.replace("repl","replace")
    content = content.replace("len_f","len")
    content = content.replace("else","else")
    content = content.replace("imp","import")
    content = content.replace("frxm","from")
    content = content.replace("getvalue","get")
    content = content.replace("rstrip","rstrip")
    content = content.replace("comm","command")
    content = content.replace("+","+")
    content = content.replace("-","-")
    content = content.replace("x","*")
    content = content.replace("/","/")
    
    
    
    
    
    return content

def compilar():
    pass
def ejecutar():

    archivo = askopenfilename(title="Ejecutar",filetypes=(("Proyecto stump",".stumpProject"),("STUMP-scripts",".STMP_sc"),("eventos de stump",".stumpevent"),) , initialdir="C:/Users/{}/Documents".format(str(user_windows)))
    traduction = traduct(archivo)
    py = open("ejecutor.py", "w")
    py.write(traduction)
    py.close()
    os.system("python ejecutor.py")
    remove("ejecutor.py")


def QIT():
    quit()
boton_preview = Button(root, text="Compile", font="Arial", background="blue", fg="white", command=lambda: ejecutar())
boton_exit = Button(root, text="Exit", command=QIT, font="Arial", background="red")
boton_exit.grid(row=0, column=1)
boton_preview.grid(row=0,column=0)

root.mainloop()
