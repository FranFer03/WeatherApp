import tkinter as tk
from PIL import ImageTk, Image

class WeatherApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.frame1 = None
        self.frame2 = None
        self.frame3 = None
        self.master = master
        self.master.title("Weather APP")
        ancho_pantalla = self.master.winfo_screenwidth()
        alto_pantalla = self.master.winfo_screenheight()
        ancho_ventana = 300
        alto_ventana = 300
        posicion_x = (ancho_pantalla - ancho_ventana) // 2
        posicion_y = (alto_pantalla - alto_ventana) // 2

        self.master.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.master.after(100, self.load_image)  # Programar la carga de la imagen

    def change_text(self):
        self.label.config(text="¡Texto cambiado!")

    def imprimir_boton(self):
        print("Boton apretado")

    def create_widgets(self):
        self.frame1 = tk.Frame(self, relief=tk.RAISED, bd=2, bg="blue")
        self.frame1.place(relx=0, rely=0, relwidth=0.25, relheight=0.3)

        self.frame2 = tk.Frame(self, relief=tk.RAISED, bd=2, bg="red")
        self.frame2.place(relx=0.25, rely=0, relwidth=0.75, relheight=0.3)
        self.label = tk.Label(self.frame2, text="¡Hola, mundo!", bg="red", fg="blue", font=("Arial", 16), width=20, height=2, anchor="center")
        self.label.pack()
        self.button = tk.Button(self.frame2, text="Cambiar", command=self.change_text)
        self.button.pack()

        self.frame3 = tk.Frame(self, relief=tk.RAISED, bd=2, bg="green")
        self.frame3.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

    def load_image(self):
        # Obtener las dimensiones de frame3
        frame1_width = self.frame1.winfo_width()
        frame1_height = self.frame1.winfo_height()

        # Abrir y redimensionar la imagen
        imagen = Image.open("imagenes/weather-forecast.png")
        imagen = imagen.resize((frame1_width, frame1_height), Image.Resampling.LANCZOS)
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        self.etiqueta = tk.Label(self.frame1, image=self.imagen_tk)
        self.etiqueta.pack(fill=tk.BOTH, expand=True)


