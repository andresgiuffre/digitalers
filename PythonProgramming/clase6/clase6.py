import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox

def funcion_boton(nombre):
    print(nombre, "apretó el botón")
    boton.config(text="Botón Apretado") # Cambia el texto del botón al ser apretado


def imprime_texto():
    print(caja.get())


def agregar_texto():
    # Agregar un texto a la caja de texto
    caja.insert(0, "Agregado")


def elimina_chars():
    # Elimina los primeros 5 caracteres
    caja.delete(0, 5) # Elimina los índices de los caracteres de 0 a 4 inclusive


def elimina_texto():
    # Elimina todo el texto
    caja.delete(0, tk.END)


def imprime_seleccion():
    print(lista.curselection()) # Devuelve el índice del elemento seleccionado
    print(lista.get(2)) # Devuelve el valor del índice 2


def imprime_estado():
    print(estado_caja.get()) # Obtiene el valor del checkbox
    # estado_caja.set(True) --> al pulsar el botón cambia el estado a True
    

def nuevo():
    print("Nuevo archivo")


def eliminar():
    print("Archivo eliminado")


def acerca_de():
    print("Acerca de ...")


ventana = tk.Tk()

ventana.title("Mi Aplicación")

# Barra de Menú
menu = tk.Menu()
menu_archivo = tk.Menu(menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo)
menu_archivo.add_command(label="Eliminar", command=eliminar)
menu_ayuda = tk.Menu(menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)
menu.add_cascade(label="Archivo", menu=menu_archivo)
menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(width=600, height=600, menu=menu)

# Botones
boton = ttk.Button(text="Soy un botón", command=lambda:funcion_boton("José"))
#boton.place(x=50, y=10)
boton.grid(row=0, column=0)

# Cajas de Texto
caja = ttk.Entry()
caja.grid(row=1, column=0)
#caja.place(x=10, y=50)
boton2 = tk.Button(text="Obtener Texto", command=imprime_texto)
boton2.grid(row=1, column=1)
#boton2.place(x=150, y=45)
agrega = tk.Button(text="Agregado", command=agregar_texto)
agrega.grid(row=3, column=0)
#agrega.place(x=10, y=80)
elimina_5 = tk.Button(text="Elimina 5", command=elimina_chars)
elimina_5.grid(row=3, column=1)
#elimina_5.place(x=80, y=80)
elimina_todo = tk.Button(text="Eliminar Texto", command=elimina_texto)
elimina_todo.grid(row=3, column=2)
#elimina_todo.place(x=145, y=80)

# Etiqueta
# Importar módulo PhotoImage
imagen = PhotoImage(file="C:\Temp\drive.png") # Solo PNG y GIF no animados
label = tk.Label(ventana, image=imagen)
label.grid(row=4, column=2)
#label.place(x=90, y=120)

# Listbox
lista = tk.Listbox()
lista.insert(0, "Python", "C++", "C#", "Java")
lista.grid(row=4, column=0)
#lista.place(x=10, y=120)
boton3 = tk.Button(text="Lista", command=imprime_seleccion)
boton3.grid(row=4, column=1)
#boton3.place(x=50, y=180)

# Combobox
lista_desplegable = ttk.Combobox(
    values=[
        "VSCode",
        "VS Community",
        "Notepad++",
        "PyCharm"
    ]
)
lista_desplegable.grid(row=5, column=0, columnspan=2)
#lista_desplegable.place(x=140, y=200)

# Checkbox
#estado_caja = tk.BooleanVar() # Se utiliza para que devuelva valores booleanos
estado_caja = tk.StringVar(value="Sin") # Se utiliza para que devuelva valores personalizados
checkbutton = ttk.Checkbutton(text="Con/Sin Airbag", variable=estado_caja, onvalue="Con", offvalue="Sin")
checkbutton.grid(row=5, column=2)
#checkbutton.place(x=140, y=230)
boton4 = tk.Button(text="Estado", command=imprime_estado)
boton4.grid(row=6, column=2)
#boton4.place(x=150, y=260)

# Cuadros de Diálogo
# Importar módulo messagebox

# Showinfo - Mensaje informativo
# messagebox.showinfo("Información", "Este es un mensaje informativo")

# Showwarning - Mensaje de Advertencia
# messagebox.showwarning("Advertencia", "Esto es una advertencia!!")

# Showerror - Mensaje de Error
# messagebox.showerror("Error", "Algo salió mal")

# Askokcancel - Hace una pregunta, si pulsamos OK es True, si pulsamos Cancel es False
# respuesta = messagebox.askokcancel("Confirmación", "Desea cerrar el programa?")
# if respuesta:
#     ventana.destroy()

# Askretrycancel - Como el showwarning pero nos permite una opcion True y una False
# respuesta = messagebox.askretrycancel("Error", "No se pudo conectar a la BBDD. Desea intentar nuevamente?")

ventana.mainloop()


# Para convertir este programa en un .exe primero instalamos PyInstaller

# pip install pyinstaller

# Desde un Command Prompt ejecutar en la carpeta donde está el programa .py:
# pyinstaller archivo.py

# Opciones posibles: 
# --oneline
# --noconsole
# Ambas requieren exclusiones del antivirus, sino son detectadas como troyanos.


# ENTORNOS VIRTUALES
# ------------------

# pip install virtualenv

# Para crear un entorno virtual nos posicionamos en el directorio donde vamos a trabajar y ejecutamos:

# virtualenv <nombre_del_entorno>

# venv\Scripts\activate (Windows)
# source venv/Scripts/activate (Linux)




