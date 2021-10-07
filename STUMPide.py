def tt_scan():
	print("-[STUMP-IDE is charge archive]-")
	print("[--loading--]")
	print("[--compiler.py is loaded--]")
	print("[++copiler.py = True]")
	print("[--icons.py is loaded]")
	print("[++icons.py = True]")
	print("[extencions = False]")
	print("-[STUMP-IDE is running]-")

import os


print("-[STUMP-IDE is running]-")
var_restiple = "-[STUMP-IDE is running]-"
var_cleardest = "console cls"
from tkinter import *
from tkinter import filedialog as f
from io import open
import io
import os
import platform
from main_coder import *


title = "STAMP-IDE-windows"
root = Tk()
root.title(title)
root.config(background="grey")
root.iconbitmap("icon.ico")

url_file = ""
def new_file():
	global url_file
	text.delete(1.0, "end")
	url_file = ""
	root.title(url_file + title)

def open_file():
	global url_file
	url_file = f.askopenfilename(initialdir = ".", filetype = (("Abrir cualquier archivo", "*"),("Abrir: stump_prj",".stumpProject"),("Abrir: stump_script",".STMP_sc"),("Abrir: stumpevent",".stumpEvent"),("Abrir: python",".py"),), title = "Abrir evento en STUMP-ide")

	if url_file != "":
		file = open(url_file, "r")
		content = file.read()
		text.delete(1.0, "end")
		text.insert("insert",content)
		file.close()
	root.title(url_file + title)
	tt_scan()

def save_file():
	global url_file
	if url_file != "":
		content = text.get(1.0,"end")
		file = open(url_file, "w+")
		file.write(content)
		root.title("Evento Guardado" + url_file + title)
		file.close()
def sugerence():
	try:
		save_file()
	except Exception as e:
		print("not saved")
	else:
		print("_/|_")
def finSugerence():
	try:
		print("-[EXIT: True]-")
	except Exception as e:
		print("-[execution is errror code: 'script-error-raise e']-")
		print("ELSED-exept==code'2512556456463233476'")
		print("your file is not saved")
	else:
		print("-[}Suseffuly{]-")

def makeDirectory():
    if platform.system() == 'Windows':
    	os.system("mkdir STUMP_conf")
    	os.system("mkdir Extencions")	
    if platform.system() == 'Windows':
    	os.system("mkdir STUMP_root_raiz")
    if platform.system() == 'Windows':
    	os.system("mkdir .ResS")
def ejecuteProject():
    if platform.system() == 'Windows':
    	os.system("mkdir appExtencions")
    	os.system("python app.py")
def ejecut():
	if platform.system() == 'Windows':
		os.system("start powershell")
def NewProject_files(rute, text):
    makeDirectory()
    file_stumpProject = text
    NP_stprFILE = open(rute, "w")
    NP_stprFILE.write(file_stumpProject)
    NP_stprFILE.close()
def NeW():
	nw1 = NewProject_files("STUMP_conf/prj.stumpProject", "stumpProject[structure]{] settings: type=project name=project.stumpname adds=SYS_NRMls {]")
	nw6 = NewProject_files("STUMP_conf/stumpProject.py", "print('stumpProject[structure]{] settings: type=project name=project.stumpname adds=SYS_NRMls {]')")
	nw2 = NewProject_files(".ResS/__register__.py", "print('reg: .ResS/*, Extencion, STUMP_conf/*, STUMP_root_raiz/*')")
	nw3 = NewProject_files("STUMP_root_raiz/info.stumpProject", "pnt(------------------------------SCCSL-----------------------------created BY StickInFireStudios)")
	nw4 = NewProject_files("Extencions/makeprj.stumpevent", "mkdir = STUMP_conf, Extencions, STUMP_root_raiz, .ResS ; files..")
	nw5 = NewProject_files("Extencions/apps.stumpevent", "imp pygame")
def ejecuteProject_part3():
	if platform.system() == 'Windows':
		os.system("python .ResS/__register__.py")
def ejecuteProject_part4():
	if platform.system() == 'Windows':
		os.system("python STUMP_conf/stumpProject.py")
def NewCompl():
	if platform.system() == 'Windows':
		os.system("python compiler.py")
#MENU
bar = Menu(root)
file_menu = Menu(bar, tearoff = 0, background="grey", fg="white")
file_menu.add_command(label = "Ejecutar ventana de powerShell", command=ejecut)
file_menu.add_command(label = "refrescar-pantalla", command = new_file)
file_menu.add_command(label = "Abrir archivo", command = open_file)
file_menu.add_command(label = "Guardar archivos", command = save_file)
file_menu.add_command(label = "Salir de el archivo", command = new_file)



projectMn = Menu(bar, tearoff = 0, background="grey", fg="white")
projectMn.add_command(label = "Nuevo Proyecto STUMP", command=NeW)
projectMn.add_command(label = "Compilar archivos stump", command=NewCompl)
projectMn.add_command(label = "Ejecutar Proyecto", command = ejecuteProject)
projectMn.add_command(label = "Ejecutar Rejistro", command = ejecuteProject_part3)
projectMn.add_command(label = "Ejecutar type archivo .stumpProject", command = ejecuteProject_part4)
projectMn.add_command(label = "Sugerencias de codigo simples para Stump-lenguage", command=Root_raiz)

dev_options = Menu(bar, tearoff=0, background="grey", fg="white")
def cls():
    os.system("cls")
def mkdir():
	os.system("mkdir app_extended")
dev_options.add_command(label = "console clear 'cls'", command=cls)
dev_options.add_command(label = "console makedirectoryExtencions 'mkdir'", command=mkdir)
#Despleg
bar.add_cascade(menu = file_menu, label = "Archibo", background="grey")
bar.add_cascade(menu = projectMn, label = "Ajustes del proyecto")
bar.add_cascade(menu = dev_options, label = "dev_options")

#txt
text = Text(root)
text.pack(fill = "both", expand = 1)
text.config(bd = 0, padx = 6, pady = 5, font = ("Courier",14), background="green", fg="white")
root.config(menu = bar)

root.mainloop()
sugerence()
finSugerence()
