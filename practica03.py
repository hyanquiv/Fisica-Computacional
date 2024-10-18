import tkinter as tk
from tkinter import ttk

# Función para calcular la fuerza F = m * a
def calcular_fuerza(event=None):
    masa = masa_slider.get()
    aceleracion = aceleracion_slider.get()
    fuerza = masa * aceleracion
    resultado_var.set(f"Fuerza (F) = {fuerza:.2f} N")  # Actualiza el resultado
    masa_valor_var.set(f"{masa:.2f} kg")  # Actualiza el valor de la masa
    aceleracion_valor_var.set(f"{aceleracion:.2f} m/s²")  # Actualiza el valor de la aceleración

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de la Segunda Ley de Newton")

# Etiqueta de título
titulo = tk.Label(ventana, text="F = m * a", font=("Arial", 16))
titulo.pack(pady=10)

# Slider para la masa (m)
masa_label = tk.Label(ventana, text="Masa (m) en kg:")
masa_label.pack()
masa_slider = ttk.Scale(ventana, from_=0.1, to=100, orient='horizontal', length=300)
masa_slider.pack(pady=5)
masa_slider.set(10)  # Valor inicial del slider

# Etiqueta para mostrar el valor actual de la masa
masa_valor_var = tk.StringVar()
masa_valor_label = tk.Label(ventana, textvariable=masa_valor_var)
masa_valor_label.pack()
masa_valor_var.set(f"{masa_slider.get():.2f} kg")  # Inicializar con el valor del slider

# Slider para la aceleración (a)
aceleracion_label = tk.Label(ventana, text="Aceleración (a) en m/s²:")
aceleracion_label.pack()
aceleracion_slider = ttk.Scale(ventana, from_=0.1, to=50, orient='horizontal', length=300)
aceleracion_slider.pack(pady=5)
aceleracion_slider.set(9.8)  # Valor inicial del slider (gravedad terrestre)

# Etiqueta para mostrar el valor actual de la aceleración
aceleracion_valor_var = tk.StringVar()
aceleracion_valor_label = tk.Label(ventana, textvariable=aceleracion_valor_var)
aceleracion_valor_label.pack()
aceleracion_valor_var.set(f"{aceleracion_slider.get():.2f} m/s²")  # Inicializar con el valor del slider

# Variable para mostrar el resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_var, font=("Arial", 14))
resultado_label.pack(pady=20)

# Actualizar el resultado cuando se muevan los sliders
masa_slider.bind("<Motion>", calcular_fuerza)
aceleracion_slider.bind("<Motion>", calcular_fuerza)

# Calcular la fuerza al inicio
calcular_fuerza()

# Iniciar el loop de la aplicación
ventana.mainloop()
