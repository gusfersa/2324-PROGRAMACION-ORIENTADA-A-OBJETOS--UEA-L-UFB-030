import tkinter as tk

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

def limpiar():
    entrada.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")

# Crear un campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones de los números
numeros = "7894561230"
for i, num in enumerate(numeros):
    tk.Button(ventana, text=num, font=("Arial", 14), command=lambda num=num: agregar_caracter(num)).grid(row=(i//3)+1, column=(i%3), padx=5, pady=5)

# Botón para el punto decimal
tk.Button(ventana, text=".", font=("Arial", 14), command=lambda: agregar_caracter(".")).grid(row=4, column=1, padx=5, pady=5)

# Botón para el cálculo y limpieza
tk.Button(ventana, text="=", font=("Arial", 14), command=calcular).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
tk.Button(ventana, text="C", font=("Arial", 14), command=limpiar).grid(row=4, column=2, columnspan=2, padx=5, pady=5)

# Crear los botones de las operaciones
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    tk.Button(ventana, text=operador, font=("Arial", 14), command=lambda op=operador: agregar_caracter(op)).grid(row=i+1, column=3, padx=5, pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()
