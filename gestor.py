from calendar import day_abbr
from distutils.log import fatal
import tkinter as tk
import pandas as pd
import numpy as np


df = pd.DataFrame({'DNI': [""], 'nombre': [""]})

def saveData():
    global df
    Sdni = cajaDni.get() #Tomo el valor de la caja y lo asigno a dni
    Snombre = cajanombre.get() #Tomo el valor de la caja y lo asigno a nombre   
    addDf = pd.DataFrame({'DNI':[Sdni], 'nombre': [Snombre]})
    df = pd.concat([df, addDf], axis="index", ignore_index= True)
    df.to_csv("./surveys.csv")


window = tk.Tk()
window.title("Gestor")
#tamaño original de la ventana en px
window.config(width=400, height=300)





#Esto es un label nombre
etiqueta = tk.Label(window, text="nombre", bg= "blue")
etiqueta.place(x= 40, y= 50)

cajanombre = tk.Entry(window)
cajanombre.place(x= 90, y=50)

#Esto es un label DNI
etiqueta = tk.Label(window, text="DNI", bg= "blue")
etiqueta.place(x= 40, y= 20)

cajaDni = tk.Entry(window)
cajaDni.place(x= 90, y=20)





#creacion de un boton Grabar
boton = tk.Button(text="Grabar Datos", command= saveData)
boton.place(x= 300, y= 20)

window.mainloop()
