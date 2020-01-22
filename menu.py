from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import os


raiz=Tk()
raiz.config()
raiz.title("Archivo")
raiz.geometry("600x600")


def info():
	messagebox.showinfo("Programa de Nacho","Hola que tal")



def explorer():
	fichero=filedialog.askopenfilename(title="Abrir Archivo",initialdir="C:",filetypes=(("Ficheros Excel","*.xlsx"),("Ficheros Texto","*.txt")))
	print(fichero)




def salir():
	raiz.destroy()



def nuevo():
	raiz.start()




def guardar():
	valor=messagebox.askquestion("Guardar","Desea guardar el archivo")

	if valor=="yes":
		messagebox.showinfo("Guardar","Guardado con exito")
		
barramenu=Menu(raiz)
raiz.config(menu=barramenu)

filemenu=Menu(barramenu, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_separator()
filemenu.add_command(label="Abrir", command=explorer)
filemenu.add_separator()
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_separator()
filemenu.add_command(label="Cerrar",command=salir)





editmenu=Menu(barramenu)
editmenu=Menu(barramenu, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_separator()
editmenu.add_command(label="Copiar")
editmenu.add_separator()
editmenu.add_command(label="Pegar")
editmenu.add_separator()
editmenu.add_command(label="Eliminar")
editmenu.add_separator()
editmenu.add_command(label="Cerrar",command=salir)




helpmenu=Menu(barramenu)
helpmenu=Menu(barramenu, tearoff=0)
helpmenu.add_command(label="Acerca de", command=info)
helpmenu.add_separator()
helpmenu.add_command(label="Quienes somos")


barramenu.add_cascade(label="Archivo", menu=filemenu)
barramenu.add_cascade(label="Editar", menu=editmenu)
barramenu.add_cascade(label="Ayuda", menu=helpmenu)




raiz.mainloop()