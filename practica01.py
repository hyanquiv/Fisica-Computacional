import tkinter as tk
from tkinter import messagebox

# Función para calcular las ecuaciones
def calcular_ecuacion():
    try:
        v = float(velocidad.get())  # Velocidad en m/s
        vi = float(velocidad_inicial.get())  # Velocidad inicial en m/s
        a = float(aceleracion.get())  # Aceleración en m/s^2
        t = float(tiempo.get())  # Tiempo en segundos

        # Cálculo de las tres ecuaciones
        delta_x_a = v * t  # Ecuación a: distancia en metros
        delta_x_b = vi * t + (0.5 * a * t**2)  # Ecuación b: distancia en metros
        vf = vi + a * t  # Ecuación c: velocidad final en m/s

        # Mostrar resultados con unidades
        resultado_a.set(f"Δx (a) = {delta_x_a:.2f} m")
        resultado_b.set(f"Δx (b) = {delta_x_b:.2f} m")
        resultado_c.set(f"Vf (c) = {vf:.2f} m/s")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese todos los valores correctamente.")

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Calculadora Cinemática")

# Variables de entrada
velocidad = tk.StringVar()
velocidad_inicial = tk.StringVar()
aceleracion = tk.StringVar()
tiempo = tk.StringVar()

# Variables de salida
resultado_a = tk.StringVar()
resultado_b = tk.StringVar()
resultado_c = tk.StringVar()

# Leyendas explicativas
leyenda1 = "Ecuación (a): Δx = v × Δt\nCalcula la distancia recorrida (Δx) en metros (m), con velocidad constante (v) en m/s, durante el tiempo (Δt) en segundos (s)."
leyenda2 = "Ecuación (b): Δx = Vi × Δt + 0.5 × α × Δt²\nCalcula la posición final (Δx) en metros (m) de un objeto con velocidad inicial (Vi) en m/s y aceleración (α) en m/s²."
leyenda3 = "Ecuación (c): Vf = Vi + α × Δt\nCalcula la velocidad final (Vf) en m/s, usando la velocidad inicial (Vi) en m/s, la aceleración (α) en m/s² y el tiempo (Δt) en segundos (s)."

# Etiquetas y campos de entrada
tk.Label(ventana, text="Velocidad (v) [m/s]:").grid(row=0, column=0)
tk.Entry(ventana, textvariable=velocidad).grid(row=0, column=1)

tk.Label(ventana, text="Velocidad inicial (Vi) [m/s]:").grid(row=1, column=0)
tk.Entry(ventana, textvariable=velocidad_inicial).grid(row=1, column=1)

tk.Label(ventana, text="Aceleración (α) [m/s²]:").grid(row=2, column=0)
tk.Entry(ventana, textvariable=aceleracion).grid(row=2, column=1)

tk.Label(ventana, text="Tiempo (Δt) [s]:").grid(row=3, column=0)
tk.Entry(ventana, textvariable=tiempo).grid(row=3, column=1)

# Leyendas explicativas de cada ecuación
tk.Label(ventana, text=leyenda1, justify="left").grid(row=4, column=0, columnspan=2, pady=(10, 0))
tk.Label(ventana, text=leyenda2, justify="left").grid(row=5, column=0, columnspan=2, pady=(10, 0))
tk.Label(ventana, text=leyenda3, justify="left").grid(row=6, column=0, columnspan=2, pady=(10, 0))

# Botón para calcular
tk.Button(ventana, text="Calcular", command=calcular_ecuacion).grid(row=7, column=0, columnspan=2, pady=10)

# Resultados
tk.Label(ventana, textvariable=resultado_a).grid(row=8, column=0, columnspan=2)
tk.Label(ventana, textvariable=resultado_b).grid(row=9, column=0, columnspan=2)
tk.Label(ventana, textvariable=resultado_c).grid(row=10, column=0, columnspan=2)

ventana.mainloop()
