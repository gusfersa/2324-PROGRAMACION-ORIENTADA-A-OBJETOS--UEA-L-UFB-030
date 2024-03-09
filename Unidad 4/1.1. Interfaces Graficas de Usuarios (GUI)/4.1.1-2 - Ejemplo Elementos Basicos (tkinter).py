import tkinter as tk
from tkinter import messagebox

def calcular_resultado():
    try:
        # Obtiene el valor del campo de entrada y realiza un cálculo
        numero = float(entrada.get())
        resultado = numero * 2
        # Muestra el resultado en el área de texto
        area_texto.insert(tk.END, f"El doble de {numero} es {resultado}\n")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de GUI con Tkinter")
ventana.geometry('400x400')

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="CALCULO  DOBLE")
etiqueta.pack(pady=0)
etiqueta = tk.Label(ventana, text="Introduce un número:")
etiqueta.pack(pady=10)

# Crear un campo de entrada
entrada = tk.Entry(ventana)
entrada.pack()

# Crear un botón para calcular el resultado
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_resultado)
boton_calcular.pack(pady=10)

# Crear un área de texto para mostrar el resultado
area_texto = tk.Text(ventana, height=5, width=30)
area_texto.pack()

# Ejecutar el bucle de eventos
ventana.mainloop()
