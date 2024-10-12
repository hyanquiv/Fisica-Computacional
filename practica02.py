import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Limpiar el gráfico antes de dibujar uno nuevo
def limpiar_grafico():
    for widget in frame_grafico.winfo_children():
        widget.destroy()

# Función para calcular la velocidad orbital (MRU y Estática)
def calcular_velocidad_orbita():
    limpiar_grafico()  # Limpiar gráfico anterior
    G = 6.67430e-11  # Constante de gravitación universal (Nm^2/kg^2)
    masa_estrella = masa_slider.get()  # Masa de la estrella (kg)
    radio_orbita = radio_slider.get()  # Radio de la órbita (m)
    
    # Fórmula de la velocidad orbital: v = sqrt(G * M / r)
    velocidad_orbital = np.sqrt(G * masa_estrella / radio_orbita)
    
    # Mostrar la fórmula y el resultado
    resultado.set(f"Velocidad orbital: {velocidad_orbital:.2f} m/s\n"
                  f"Fórmula: v = √(G * M / r)\n"
                  f"G = {G:.2e} N·m²/kg², M = {masa_estrella:.2e} kg, r = {radio_orbita:.2e} m")
    
    # Graficar la velocidad orbital en función del radio
    fig, ax = plt.subplots(figsize=(7, 4))
    radios = np.linspace(1e6, radio_orbita, 100)  # Rango de radios
    velocidades = np.sqrt(G * masa_estrella / radios)  # Cálculo de velocidades
    ax.plot(radios, velocidades, label="Velocidad Orbital", color='blue')
    ax.set_xlabel("Radio de la Órbita (m)")
    ax.set_ylabel("Velocidad (m/s)")
    ax.legend()
    
    # Mostrar la gráfica en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Función para calcular la fuerza de un móvil
def calcular_fuerza_movil():
    limpiar_grafico()  # Limpiar gráfico anterior
    masa = masa_movil_slider.get()  # Masa del móvil (kg)
    vi = vi_slider.get()  # Velocidad inicial (m/s)
    vf = vf_slider.get()  # Velocidad final (m/s)
    distancia = distancia_slider.get()  # Distancia recorrida (m)
    tiempo = tiempo_slider.get()  # Tiempo (s)
    
    # Aceleración a = (vf - vi) / t
    aceleracion = (vf - vi) / tiempo
    
    # Segunda ley de Newton: F = m * a
    fuerza = masa * aceleracion
    
    # Mostrar la fórmula y el resultado
    resultado.set(f"Fuerza aplicada: {fuerza:.2f} N\n"
                  f"Fórmula: F = m * a = m * (vf - vi) / t\n"
                  f"m = {masa:.2f} kg, vi = {vi:.2f} m/s, vf = {vf:.2f} m/s, t = {tiempo:.2f} s")
    
    # Graficar el proceso
    fig, ax = plt.subplots(figsize=(7, 4))
    tiempos = np.linspace(0, tiempo, 100)
    velocidades = vi + (vf - vi) * (tiempos / tiempo)
    ax.plot(tiempos, velocidades, label="Velocidad", color='green')
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Velocidad (m/s)")
    ax.legend()
    
    # Mostrar la gráfica en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Función para cambiar entre las opciones
def cambiar_opcion():
    opcion = combo_opciones.get()
    if opcion == "Calcular velocidad orbital":
        frame_orbita.pack(side="left", fill="both")
        frame_fuerza.pack_forget()
    elif opcion == "Calcular fuerza de un móvil":
        frame_orbita.pack_forget()
        frame_fuerza.pack(side="left", fill="both")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculos de Física")
ventana.geometry("1200x600")

# Crear frames para organizar la interfaz
frame_controles = tk.Frame(ventana, width=400)
frame_grafico = tk.Frame(ventana, width=800)
frame_controles.pack(side="left", fill="y")
frame_grafico.pack(side="right", fill="both", expand=True)

# Resultado
resultado = tk.StringVar()

# Combobox para seleccionar la opción
combo_opciones = ttk.Combobox(frame_controles, values=["Calcular velocidad orbital", "Calcular fuerza de un móvil"])
combo_opciones.pack(pady=10)
combo_opciones.bind("<<ComboboxSelected>>", lambda e: cambiar_opcion())

# Frame para calcular la velocidad orbital
frame_orbita = tk.Frame(frame_controles)
tk.Label(frame_orbita, text="Masa de la estrella (kg):").pack(pady=5)
masa_slider = tk.Scale(frame_orbita, from_=1e24, to=1e30, orient="horizontal", resolution=1e24, length=300)
masa_slider.pack()

tk.Label(frame_orbita, text="Radio de la órbita (m):").pack(pady=5)
radio_slider = tk.Scale(frame_orbita, from_=1e6, to=1e12, orient="horizontal", resolution=1e6, length=300)
radio_slider.pack()

tk.Button(frame_orbita, text="Calcular Velocidad Orbital", command=calcular_velocidad_orbita).pack(pady=10)

# Frame para calcular la fuerza de un móvil
frame_fuerza = tk.Frame(frame_controles)
tk.Label(frame_fuerza, text="Masa del móvil (kg):").pack(pady=5)
masa_movil_slider = tk.Scale(frame_fuerza, from_=1, to=1000, orient="horizontal", length=300)
masa_movil_slider.pack()

tk.Label(frame_fuerza, text="Velocidad inicial (m/s):").pack(pady=5)
vi_slider = tk.Scale(frame_fuerza, from_=0, to=100, orient="horizontal", length=300)
vi_slider.pack()

tk.Label(frame_fuerza, text="Velocidad final (m/s):").pack(pady=5)
vf_slider = tk.Scale(frame_fuerza, from_=0, to=100, orient="horizontal", length=300)
vf_slider.pack()

tk.Label(frame_fuerza, text="Distancia recorrida (m):").pack(pady=5)
distancia_slider = tk.Scale(frame_fuerza, from_=0, to=1000, orient="horizontal", length=300)
distancia_slider.pack()

tk.Label(frame_fuerza, text="Tiempo (s):").pack(pady=5)
tiempo_slider = tk.Scale(frame_fuerza, from_=1, to=100, orient="horizontal", length=300)
tiempo_slider.pack()

tk.Button(frame_fuerza, text="Calcular Fuerza", command=calcular_fuerza_movil).pack(pady=10)

# Mostrar el resultado
tk.Label(frame_controles, textvariable=resultado).pack(pady=20)

# Iniciar con el frame de órbita
frame_orbita.pack(side="left", fill="both")

# Iniciar el bucle de la ventana
ventana.mainloop()
