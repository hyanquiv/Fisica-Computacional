import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import tkinter as tk
from tkinter import ttk, messagebox

# Función de fuerza variable
def fuerza_variable(x):
    # return 2 * x  # Opción: Fuerza F(x) = 2x
    return np.sin(x)  # Opción: Fuerza F(x) = sin(x)

# Función para calcular el trabajo mediante integración numérica
def calcular_trabajo(F, a, b):
    W, _ = quad(F, a, b)  # Realiza la integración numérica entre los límites a y b
    return W

# Función para graficar la fuerza y el área bajo la curva (trabajo)
def graficar_fuerza(F, a, b):
    x = np.linspace(a, b, 100)  # Genera 100 puntos entre los límites de integración
    y = F(x)  # Evalúa la función de fuerza en esos puntos

    # Crear el gráfico
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label='Fuerza F(x)', color='blue')  # Grafica la fuerza
    plt.fill_between(x, 0, y, color='lightblue', alpha=0.5, label='Área = Trabajo')  # Resalta el área bajo la curva
    plt.title('Fuerza Variable F(x) = sin(x) vs Posición x')
    plt.xlabel('Posición (m)')
    plt.ylabel('Fuerza (N)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Función que se ejecuta cuando se presiona el botón "Calcular"
def on_calcular():
    try:
        a = float(slider_a.get())  # Obtener el valor del límite inferior
        b = float(slider_b.get())  # Obtener el valor del límite superior
        
        if a >= b:
            messagebox.showerror("Error", "El límite inferior debe ser menor que el límite superior.")
            return

        # Calcular el trabajo
        W = calcular_trabajo(fuerza_variable, a, b)
        label_resultado.config(text=f"El trabajo es: {W:.2f} J")

        # Graficar la fuerza
        graficar_fuerza(fuerza_variable, a, b)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Trabajo con Fuerza Variable")
root.geometry("400x300")

# Etiquetas y sliders para los límites de integración
label_a = ttk.Label(root, text="Límite a:")
label_a.pack(pady=5)
slider_a = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, resolution=0.1)
slider_a.pack(pady=5)

label_b = ttk.Label(root, text="Límite b:")
label_b.pack(pady=5)
slider_b = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, resolution=0.1)
slider_b.set(5)  # Valor inicial en 5
slider_b.pack(pady=5)

# Botón para calcular el trabajo
boton_calcular = ttk.Button(root, text="Calcular Trabajo", command=on_calcular)
boton_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = ttk.Label(root, text="El trabajo es: -- J")
label_resultado.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
