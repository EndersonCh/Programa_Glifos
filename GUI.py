from logica import Transformador
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pathlib import Path

class aplicacion:
    def __init__(self,ventana):
        
        self.ruta=None
        self.ventana=ventana # creación de ventana
        
        self.color_fondo="#ECE8DC" #Paleta de colores
        self.color_azul="#3FA3DC"
        self.color_rojo="#E41F1A"
        self.color_negro="#272726"
        
        self.ima_cabecera=None # Recursos Visuales
        self.ima_btn_salir=None
        self.ima_titulo=None
        self.ima_btn_1=None
        self.ima_btn_2=None
        self.ima_btn_3=None
        self.ima_btn_4=None
        self.ima_btn_5=None
        self.ima_base=None
        self.ima_procesar=None
        self.ima_exportar=None
        self.ima_limpiar=None
        self.ima_cajauser=None
        
        self.boton_1=None   #botones
        self.boton_2=None
        self.boton_3=None
        self.boton_4=None
        self.boton_5=None
        
        self.caja_1=None # Entradas y salidas de texto
        self.entrada=None
        
        self.ventana.title("Segunda practica") #configuracion de ventana
        self.ventana.geometry("800x600")
        self.ventana.configure(bg=self.color_fondo)

        
        self.trans=Transformador()
        self.crear_entorno()
        
    def cargar_imagen(self,nom_archivo): #Función para obtener ruta de la ubicacion de imagenes
        dir_actual=os.path.dirname(os.path.abspath(__file__))
        imagen_path=os.path.join(dir_actual,"assets",nom_archivo)
        
        if not os.path.exists(imagen_path):
            raise FileNotFoundError(f"No se pudo abrir la imagen {imagen_path}")
        
        return tk.PhotoImage(file=imagen_path)  
      
    def seleccionar_archivo(self): #Función para cargar archivo 
        
        
        ruta=filedialog.askopenfilename(
            title="Seleccionar archivo .txt",
            filetypes=[("Archivos de texto", "*txt"), ("Todos los archivos","*.*")] 
        )
        
        if ruta:
            self.ruta = Path(ruta)
            print(f"Ruta Almacenada: {self.ruta}")
            self.boton_1.config(state="disabled")
            self.boton_2.config(state="active")
            self.boton_4.config(state="active")
            
            self.trans.cargar_datos(self.ruta)
            self.caja_1.config(state='normal')
            self.caja_1.delete("1.0",tk.END)
            self.caja_1.insert(1.0,"Numeros:\n")
            for linea in self.trans.numeros:
                self.caja_1.insert('end',f"{linea}\n")    
            
            self.caja_1.config(state='disabled')
            self.boton_5.config(state="disabled")            
        else:
            print(f"No se seleciono ningun archivo")  
            
    def accion_procesar(self): #Función para procesar numeros leidos
    
        self.caja_1.config(state="normal")
        self.caja_1.delete("1.0",tk.END)
        self.caja_1.insert(1.0,"Numeros y Glifos\n")
        for linea,numero in zip(self.trans.glifos, self.trans.numeros):
            linea="".join(linea)
            self.caja_1.insert("end",f"--> {numero}: {linea} \n")    
        
        self.caja_1.config(state='disabled')
        self.boton_2.config(state="disabled")
        self.boton_3.config(state="active")
        self.boton_5.config(state="active")
        
    def accion_limpiar(self): #función que limpia listas y pantalla para procesar datos nuevos
        
        self.caja_1.config(state="normal")
        self.caja_1.delete("1.0",tk.END)
        self.trans.numeros.clear()
        self.trans.glifos.clear()
        self.boton_1.config(state="active")
        self.boton_4.config(state="disabled")
        self.boton_3.config(state="disabled")
        
    def accion_exportar(self): #función que invoca al exportar para crear archivo de salida
        
        if self.trans.exportar():
            messagebox.showinfo("Exportar","El archivo .txt se ha creado de manera exictosa") 
        else:  
            messagebox.showwarning("Exportar","Ocurrio un error al crear el archivo") 
        self.boton_3.config(state="disabled")
    
    def accion_individual(self): #Función para procesar un solo numero desde pantalla
        nume= self.entrada.get()
        self.entrada.delete(0,tk.END)
        if nume.isdigit():
            nume=int(nume)
            if nume>0 and nume<4000:
                self.trans.individual(nume)
                self.caja_1.config(state="normal")
                glif="".join(self.trans.glifo)
                self.caja_1.insert("end",f"--> {nume}: {glif}\n")
                self.boton_1.config(state="disabled")
                self.boton_4.config(state="active",relief=tk.FLAT)
                self.boton_3.config(state="active",relief=tk.FLAT)
            else:
                messagebox.showinfo("Error","Ingresa un numero entre 1-4000")
        else:
            messagebox.showinfo("Error","Ingresa un numero entre 1-4000")
            
    def al_entrar(self,event): #control de entrada por interfaz
        if self.entrada.get() == "Escribe un numero!":
            self.entrada.delete(0, tk.END)
            self.entrada.config(fg=self.color_azul,relief=tk.FLAT)

    def al_salir(self,event): #control de entrada por interfaz
        if self.entrada.get() == "":
            self.entrada.insert(0, "Escribe un numero!")
            self.entrada.config(fg=self.color_negro,relief=tk.FLAT)    
                 
    def crear_entorno(self): # creacion de parte grafica(Botones, textos, imagenes)
        canvas=tk.Canvas(self.ventana,
            bg=self.color_fondo,
            height=100,  # Altura fija
            highlightthickness=0
            
        )
        canvas.pack(fill="both",expand=True)
        
        canvas_cabecera=tk.Canvas(canvas,
            height=70,  # Altura fija
            highlightthickness=0,
            bg=self.color_fondo
                                )
        canvas_cabecera.pack(side="top", fill="x")
        ancho =canvas_cabecera.winfo_width()
        alto = canvas_cabecera.winfo_height()
        
        self.ima_cabecera=self.cargar_imagen("cabecera.png")
        
        cabecera=canvas_cabecera.create_image( 
            400.6,38.3,                         
            image=self.ima_cabecera,  
            anchor="center"
            )
        
        self.ima_btn_salir=self.cargar_imagen("boton_salir.png")
        boton_salir=tk.Button(
            canvas_cabecera,
            image=self.ima_btn_salir,
            borderwidth=0,
            highlightthickness=0,
            command=ventana.destroy,
            relief="flat",
            bg=self.color_fondo
                )
        boton_salir.place(
            x=637.3,
            y=37.8,
            width=216,
            height=26,
            anchor="center")

        self.ima_titulo=self.cargar_imagen("titulo.png")
        titulo=canvas.create_image(
            400.06,188.27,
            image=self.ima_titulo,
            ancho="center"     
        )

        descripcion=tk.Label(ventana, 
            text="Es programa transforma números enteros positivos en su representación glifica de Aethelgard", 
            font=("Helvetica", 12), 
            bg=self.color_fondo,
            fg=self.color_negro
        )

        descripcion.place(
            x=400,
            y=322,
            width=711,
            height=20,
            anchor="center"  
        )
        
        self.ima_base=self.cargar_imagen("base.png")
        
        base=canvas.create_image(
            378.2,460.2,
            image=self.ima_base,
            anchor="center"
        )
        
        self.ima_procesar=self.cargar_imagen("procesar.png")
        procesar=canvas.create_image(
            158,423.5,
            image=self.ima_procesar,
            anchor="center"
        )
        self.ima_exportar=self.cargar_imagen("exportar.png")
        exportar=canvas.create_image(
            158,488.93,
            image=self.ima_exportar,
            anchor="center"
        ) 
        self.ima_limpiar=self.cargar_imagen("limpiar.png")
        limpiar=canvas.create_image(
            158,551.39,
            image=self.ima_limpiar,
            anchor="center"
        ) 
        self.ima_btn_1=self.cargar_imagen("boton_1.png")
        self.boton_1=tk.Button(
            
            image=self.ima_btn_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.seleccionar_archivo,
            relief=tk.FLAT,
            bg=self.color_azul,
            activebackground=self.color_azul
                )
        self.boton_1.place(
            x=699,
            y=263.20,
            width=88,
            height=40,
            anchor="center"
        )       
        self.ima_btn_2=self.cargar_imagen("boton_4.png")
        self.boton_2=tk.Button(
            
            image=self.ima_btn_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.accion_procesar,
            relief=tk.FLAT,
            bg=self.color_fondo,
            activebackground=self.color_fondo
                )
        self.boton_2.place(
            x=331.8,
            y=419.6,
            width=84,
            height=40,
            anchor="center"
        )  
        self.boton_2.config(state="disabled")     
        self.ima_btn_3=self.cargar_imagen("boton_3.png")
        self.boton_3=tk.Button(
            
            image=self.ima_btn_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.accion_exportar,
            relief=tk.FLAT,
            bg=self.color_fondo,
            activebackground=self.color_fondo
                )
        self.boton_3.place(
            x=331.8,
            y=487.8,
            width=84,
            height=40,
            anchor="center"
        )  
        self.boton_3.config(state="disabled")     
        self.ima_btn_4=self.cargar_imagen("boton_2.png")
        self.boton_4=tk.Button(
            
            image=self.ima_btn_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.accion_limpiar,
            relief=tk.FLAT,
            bg=self.color_fondo,
            activebackground=self.color_fondo
                )
        self.boton_4.place(
            x=331.8,
            y=550.3,
            width=84,
            height=40,
            anchor="center"
        )   
        self.boton_4.config(state="disabled") 
        self.ima_btn_5=self.cargar_imagen("boton_5.png")
        self.boton_5=tk.Button(
            
            image=self.ima_btn_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.accion_individual,
            relief=tk.FLAT,
            bg=self.color_fondo,
            activebackground=self.color_fondo
                )
        self.boton_5.place(
            x=710.0,
            y=369.0,
            width=48,
            height=36,
            anchor="center"
        )   
        self.caja_1=tk.Text(
            canvas,
            width=50,
            height=20,
              # Opciones: NONE, CHAR, WORD
            font=('Helvetica', 14),
            highlightthickness=0,
            padx=10,
            pady=10,
            bd=0,                  
            state='disabled',      
            bg="#FAFAFA",   
            fg=self.color_negro 
            
        )
        self.caja_1.place(
            x=571,
            y=480,
            width=364,
            height=160,
            
            anchor="center"
            )
        
        self.ima_cajauser=self.cargar_imagen("entrada.png")
        caja_user=canvas.create_image(
            571,370,
            image=self.ima_cajauser,
            anchor="center"
        )
        
        self.entrada=tk.Entry(
            fg=self.color_negro,
            bg="#FAFAFA",
            font=('Helvetica', 14),
            bd=0,
            relief="flat",
            
            
            )
        self.entrada.insert(0, "Escribe un numero!")
        self.entrada.bind("<FocusIn>", self.al_entrar)
        self.entrada.bind("<FocusOut>", self.al_salir)
        self.entrada.place(
            x=547,y=371,
            width=254.18,
            height=19.3,
            anchor="center"
        )
        
            
      
        
        
        
if __name__==("__main__"):
    ventana=tk.Tk()
   
    app=aplicacion(ventana)
    ventana.resizable(False,False)
    
    ventana.mainloop()
    