import tkinter as tk
from PIL import Image, ImageTk

def cambiar_imagen(btn_id, nueva_imagen):
    canvas.itemconfig(btn_id, image=nueva_imagen)

root = tk.Tk()
root.geometry("900x600")
root.title("Interfaz personalizada")

# ===================== Canvas principal =====================
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ========== Imagen de fondo ==========
img_fondo_original = Image.open("fonfo.png")
img_fondo = ImageTk.PhotoImage(img_fondo_original)
fondo_id = canvas.create_image(0, 0, anchor="nw", image=img_fondo)

# ========== Imagen de título ==========
img_titulo = ImageTk.PhotoImage(Image.open("titulo_1.png"))
titulo_id = canvas.create_image(450, 80, image=img_titulo)

# ========== Botones personalizados ==========
img_btn1 = ImageTk.PhotoImage(Image.open("boton_1.png"))
img_btn1_hover = ImageTk.PhotoImage(Image.open("boton_1.png"))

img_btn2 = ImageTk.PhotoImage(Image.open("boton_2.png"))
img_btn2_hover = ImageTk.PhotoImage(Image.open("boton_2.png"))

# Crear botones como Labels (pueden simular clics)
btn1 = tk.Label(root, image=img_btn1, bd=0, cursor="hand2")
btn2 = tk.Label(root, image=img_btn2, bd=0, cursor="hand2")

# Posicionar sobre canvas
btn1_id = canvas.create_window(300, 300, window=btn1)
btn2_id = canvas.create_window(550, 300, window=btn2)

# Eventos para cambiar imágenes al pasar el mouse
btn1.bind("<Enter>", lambda e: cambiar_imagen(btn1_id, img_btn1_hover))
btn1.bind("<Leave>", lambda e: cambiar_imagen(btn1_id, img_btn1))
btn2.bind("<Enter>", lambda e: cambiar_imagen(btn2_id, img_btn2_hover))
btn2.bind("<Leave>", lambda e: cambiar_imagen(btn2_id, img_btn2))

# ========== Frame opcional con Grid (zona inferior) ==========
frame_grid = tk.Frame(canvas, bg="#ffffff")
canvas.create_window(450, 500, window=frame_grid)

tk.Label(frame_grid, text="Zona informativa", bg="#ffffff").grid(row=0, column=0, padx=10)
tk.Button(frame_grid, text="Salir", command=root.quit).grid(row=0, column=1, padx=10)

# ========== Redimensionamiento ==========
def ajustar_fondo(event):
    nueva = img_fondo_original.resize((event.width, event.height))
    img_fondo_redim = ImageTk.PhotoImage(nueva)
    canvas.itemconfig(fondo_id, image=img_fondo_redim)
    canvas.image = img_fondo_redim  # Evitar GC

canvas.bind("<Configure>", ajustar_fondo)

root.mainloop()
