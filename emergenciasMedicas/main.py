import tkinter as tk

from PIL import Image,ImageTk
from functions import display_logo
from SolicitarAtencion import ventanaAtencion


root = tk.Tk()
root.title("Emergencias Medicas")

root.geometry("1200x500")


#encabezado -> logo y btn
header = tk.Frame(root, width = 1200, height = 160, bg = "white")
header.grid(columnspan = 3, rowspan = 1, row = 0)

body = tk.Frame(root, width = 1200, height = 340, bg = "#0026fe")
body.grid(columnspan = 3, rowspan = 2, row = 1)

#agregar_btn = tk.Button(root, image=display_btn('./images/btn_agregar.png',1,0,20,60,"nw"),borderwidth=0,command="click")
agregar_btn = tk.Button(root, text="solicitar atencion", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=15, command=lambda: ventanaAtencion())
agregar_btn.grid(column=1, row=0, pady=50, padx=0,sticky="w" )

otro = tk.Button(root, text="otro", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=12,command=lambda:print("click"))
otro.grid(column=1, row=0, pady=50, padx=100, )

agregar_btn = tk.Button(root, text="lista de espera", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=12)
agregar_btn.grid(column=1, row=0, pady=50, padx=0, sticky = "e")

agregar_btn = tk.Button(root, text="situacion de pacientes", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=18)
agregar_btn.grid(column=2, row=0, pady=50, padx=50,sticky = "w")

agregar_btn = tk.Button(root, text="otro", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=12)
agregar_btn.grid(column=2, row=0, pady=50, padx=20,sticky = "e")

display_logo('./images/logoucen.png',0,0)





root.mainloop()
