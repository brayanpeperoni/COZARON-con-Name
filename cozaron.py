import tkinter as tk
from tkinter import simpledialog, messagebox
import math

def crear_corazon(nombre):
    ventana = tk.Tk()
    ventana.title("Corazón con nombre")
    ventana.geometry("900x750")
    ventana.configure(bg="#0d0d0d")

    titulo = tk.Label(
        ventana,
        text=f"Nombre de tu persona especial: {nombre}",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#0d0d0d"
    )
    titulo.pack(pady=20)

    canvas = tk.Canvas(
        ventana,
        width=850,
        height=620,
        bg="#0d0d0d",
        highlightthickness=0
    )
    canvas.pack()

    texto = nombre
    color = "#ff4d6d"

    # Crear forma de corazón usando fórmula matemática
    puntos = []
    for i in range(0, 360, 5):
        t = math.radians(i)
        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        x = x * 18 + 425
        y = -y * 18 + 320
        puntos.append((x, y))

    # Rellenar corazón con el nombre
    for y in range(140, 560, 24):
        for x in range(170, 680, 70):
            dentro = False
            cruces = 0

            for i in range(len(puntos)):
                x1, y1 = puntos[i]
                x2, y2 = puntos[(i + 1) % len(puntos)]

                if ((y1 > y) != (y2 > y)):
                    x_interseccion = (x2 - x1) * (y - y1) / (y2 - y1) + x1
                    if x < x_interseccion:
                        cruces += 1

            if cruces % 2 == 1:
                canvas.create_text(
                    x,
                    y,
                    text=texto,
                    fill=color,
                    font=("Consolas", 13, "bold")
                )

    # Borde del corazón
    canvas.create_line(
        puntos,
        fill="#ff1e56",
        width=3,
        smooth=True
    )

    # Mensaje inferior
    canvas.create_text(
        425,
        590,
        text="❤️ Formando corazón... ❤️",
        fill="white",
        font=("Arial", 16, "bold")
    )

    ventana.mainloop()

# Ventana para pedir nombre
root = tk.Tk()
root.withdraw()

nombre = simpledialog.askstring("Nombre", "Escribe el nombre:")

if nombre:
    crear_corazon(nombre)
else:
    messagebox.showwarning("Aviso", "No escribiste ningún nombre.")