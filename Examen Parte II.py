# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:21:50 2022

@author: Dell
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
from tkinter.messagebox import showinfo

#Establecer ventana
vent = tk.Tk()
vent.geometry('1400x700')

vent.title('Calculo de Zonas Inundadas')    #Titulo
vent.config(bg= 'turquoise1')

# Caja 1 #


etiq1 = tk.Label(vent, text='1. Seleciona la imagen a utilizar.', bg='gray85',  fg='black', font = 'Arial 12')
etiq1.grid(row = 0, column = 1, pady = (3))


textResult1 = tk.Text(vent, height = 1, font = 'Arial 10', bg = 'white', fg = 'black', highlightthickness = 3)                                
textResult1.grid(row = 2, column = 1, padx = (50,50))
#funcion para abrir imagen
def abrir_imagen():
    imagen_abierta=filedialog.askopenfilename(initialdir = "/", title = "Seleccione la imagen.",filetypes = (("zip files","*.zip"),("all files","*.*")))
    print (imagen_abierta)
    textResult1.insert(tk.END, imagen_abierta)
    

boton1 = tk.Button(text="Seleccionar imagen", font = 'Arial 10',  bg="white",command=abrir_imagen)
boton1.grid(row = 1, column = 1, padx = (10,10))

# Caja 2 #


etiq2 = tk.Label(vent, text='2. Seleciona el Shapefile de la zona de estudio.', font = 'Arial 10', bg='gray85', fg='black')
etiq2.grid(row = 3, column = 1)


textResult2 = tk.Text(vent, height = 1, font = 'Arial 10', bg = 'white', fg = 'black', highlightthickness = 3)                                     
textResult2.grid(row = 5, column = 1, padx = (100,100))


def abrir_shape():
    shape_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione shapefile",filetypes = (("shapefile files","*.shp"),
                ("all files","*.*")))
    print (shape_abierto)
    textResult2.insert(tk.END, shape_abierto)
    

boton2 = tk.Button(text="Seleccione el shapefile ", font = 'Arial 10', bg="white", command = abrir_shape)
boton2.grid(row = 4, column = 1)
# caja 3 #


etiq3 = tk.Label(vent, text='3. Proceda a pre-procesar la imagen.', font = 'Arial 10', bg='gray85',  fg='black')
etiq3.grid(row = 6, column = 1)



boton3 = tk.Button(text="Preprocesar la imagen", font = 'Arial 10', bg="white")
boton3.grid(row = 7, column = 1)

# Caja 4 #


etiq4 = tk.Label(vent, text='4. Defina el umbral de la mascara de agua.', font = 'Arial 10', bg='gray85',  fg='black')
etiq4.grid(row = 9, column = 1)


umbral = tk.Entry(vent, font= 'Arial 10', justify = 'center', highlightthickness = 3)
umbral.grid(row = 10, column = 1, pady = (3))

boton4 = tk.Button(text="Aplicar la mascara", font = 'Arial 10', bg="white")
boton4.grid(row = 11, column = 1, pady =(3))