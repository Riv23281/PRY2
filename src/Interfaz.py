import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from recomendacion import Recomendacion
from conexion_neo4j import ConexionNeo4j
from manejador_usuarios import ManejadorUsuarios

class Interfaz:
    def __init__(self, master):
        self.master = master
        self.master.title("App de Recomendaciones de Recetas")
        self.conexion = ConexionNeo4j(uri="bolt://localhost:7687", usuario="neo4j", contraseña="Hola12345")
        self.conexion.conectar()
        self.recomendacion = Recomendacion(self.conexion)
        self.manejador_usuarios = ManejadorUsuarios()
        
        self.frame_inicio = tk.Frame(master)
        self.frame_inicio.pack()
        
        self.label_bienvenida = tk.Label(self.frame_inicio, text="Bienvenido a la App de Recomendaciones de Recetas")
        self.label_bienvenida.pack()

        self.label_usuario = tk.Label(self.frame_inicio, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(self.frame_inicio)
        self.entry_usuario.pack()
        
        self.label_contraseña = tk.Label(self.frame_inicio, text="Contraseña:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(self.frame_inicio, show='*')
        self.entry_contraseña.pack()

        self.boton_registro = tk.Button(self.frame_inicio, text="Registrarse", command=self.registrar_usuario)
        self.boton_registro.pack()
        
        self.boton_login = tk.Button(self.frame_inicio, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_login.pack()

    def registrar_usuario(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        if self.manejador_usuarios.crear_usuario(usuario, contraseña):
            messagebox.showinfo("Registro", "Usuario registrado exitosamente.")
        else:
            messagebox.showerror("Registro", "El usuario ya existe.")

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        if self.manejador_usuarios.iniciar_sesion(usuario, contraseña):
            self.frame_inicio.pack_forget()
            self.frame_menu_principal = tk.Frame(self.master)
            self.frame_menu_principal.pack()
            
            self.label_menu_principal = tk.Label(self.frame_menu_principal, text="Menú Principal")
            self.label_menu_principal.pack()
            
            self.boton_buscar = tk.Button(self.frame_menu_principal, text="Buscar Recetas", command=self.buscar_recetas)
            self.boton_buscar.pack()
            
            self.boton_ver_todas = tk.Button(self.frame_menu_principal, text="Ver Todas las Recetas", command=self.ver_todas_recetas)
            self.boton_ver_todas.pack()
            
            self.boton_recomendar = tk.Button(self.frame_menu_principal, text="Dar Recomendación", command=self.dar_recomendacion)
            self.boton_recomendar.pack()
            
            self.boton_agregar = tk.Button(self.frame_menu_principal, text="Agregar Receta", command=self.agregar_receta)
            self.boton_agregar.pack()
            
            self.boton_eliminar = tk.Button(self.frame_menu_principal, text="Eliminar Receta", command=self.eliminar_receta)
            self.boton_eliminar.pack()
            
            self.boton_editar = tk.Button(self.frame_menu_principal, text="Editar Receta", command=self.editar_receta)
            self.boton_editar.pack()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def buscar_recetas(self):
        etiqueta = askstring("Buscar Recetas", "Ingrese la etiqueta:")
        if etiqueta:
            recetas = self.recomendacion.recomendar_recetas([etiqueta.lower().strip()])
            if recetas:
                detalles_recetas = [f"Nombre: {receta['nombre']}\nEtiquetas: {', '.join(receta['etiquetas'])}\nIngredientes: {', '.join(receta['ingredientes'])}\nInstrucciones: {receta['instrucciones']}" for receta in recetas]
                messagebox.showinfo("Resultados de Búsqueda", "\n\n".join(detalles_recetas))
            else:
                messagebox.showinfo("Resultados de Búsqueda", "No se encontraron recetas con esa etiqueta.")

    def ver_todas_recetas(self):
        recetas = self.recomendacion.obtener_todas_recetas()
        if recetas:
            detalles_recetas = [f"Nombre: {receta['nombre']}\nEtiquetas: {', '.join(receta['etiquetas'])}\nIngredientes: {', '.join(receta['ingredientes'])}\nInstrucciones: {receta['instrucciones']}" for receta in recetas]
            messagebox.showinfo("Todas las Recetas", "\n\n".join(detalles_recetas))
        else:
            messagebox.showinfo("Todas las Recetas", "No hay recetas en la base de datos.")

    def dar_recomendacion(self):
        receta = self.recomendacion.recomendar_aleatoria()
        if receta:
            messagebox.showinfo("Recomendación", f"Te recomendamos probar: {receta['nombre']}")
        else:
            messagebox.showinfo("Recomendación", "No hay recetas para recomendar.")

    def agregar_receta(self):
        self.ventana_agregar = tk.Toplevel(self.master)
        self.ventana_agregar.title("Agregar Receta")
        
        self.label_nombre = tk.Label(self.ventana_agregar, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.ventana_agregar)
        self.entry_nombre.pack()
        
        self.label_etiquetas = tk.Label(self.ventana_agregar, text="Etiquetas (separadas por comas):")
        self.label_etiquetas.pack()
        self.entry_etiquetas = tk.Entry(self.ventana_agregar)
        self.entry_etiquetas.pack()
        
        self.label_ingredientes = tk.Label(self.ventana_agregar, text="Ingredientes (separados por comas):")
        self.label_ingredientes.pack()
        self.entry_ingredientes = tk.Entry(self.ventana_agregar)
        self.entry_ingredientes.pack()
        
        self.label_instrucciones = tk.Label(self.ventana_agregar, text="Instrucciones:")
        self.label_instrucciones.pack()
        self.entry_instrucciones = tk.Entry(self.ventana_agregar)
        self.entry_instrucciones.pack()
        
        self.boton_guardar = tk.Button(self.ventana_agregar, text="Guardar", command=self.guardar_receta)
        self.boton_guardar.pack()

    def guardar_receta(self):
        nombre = self.entry_nombre.get().strip()
        etiquetas = [et.strip().lower() for et in self.entry_etiquetas.get().split(',')]
        ingredientes = [ing.strip() for ing in self.entry_ingredientes.get().split(',')]
        instrucciones = self.entry_instrucciones.get().strip()
        
        if nombre and etiquetas and ingredientes:
            self.recomendacion.agregar_receta(nombre, etiquetas, ingredientes, instrucciones)
            messagebox.showinfo("Agregar Receta", "Receta agregada exitosamente.")
            self.ventana_agregar.destroy()
        else:
            messagebox.showwarning("Agregar Receta", "Todos los campos son obligatorios.")

    def eliminar_receta(self):
        nombre = askstring("Eliminar Receta", "Ingrese el nombre de la receta a eliminar:")
        if nombre:
            self.recomendacion.eliminar_receta(nombre.lower().strip())
            messagebox.showinfo("Eliminar Receta", "Receta eliminada exitosamente.")
        else:
            messagebox.showwarning("Eliminar Receta", "Debe ingresar el nombre de la receta a eliminar.")

    def editar_receta(self):
        nombre = askstring("Editar Receta", "Ingrese el nombre de la receta a editar:")
        receta = self.recomendacion.obtener_receta(nombre.lower().strip())
        if receta:
            self.ventana_editar = tk.Toplevel(self.master)
            self.ventana_editar.title("Editar Receta")

            self.label_nombre = tk.Label(self.ventana_editar, text="Nombre:")
            self.label_nombre.pack()
            self.entry_nombre = tk.Entry(self.ventana_editar)
            self.entry_nombre.insert(0, receta['nombre'])
            self.entry_nombre.pack()
            
            self.label_etiquetas = tk.Label(self.ventana_editar, text="Etiquetas (separadas por comas):")
            self.label_etiquetas.pack()
            self.entry_etiquetas = tk.Entry(self.ventana_editar)
            self.entry_etiquetas.insert(0, ','.join(receta['etiquetas']))
            self.entry_etiquetas.pack()
            
            self.label_ingredientes = tk.Label(self.ventana_editar, text="Ingredientes (separados por comas):")
            self.label_ingredientes.pack()
            self.entry_ingredientes = tk.Entry(self.ventana_editar)
            self.entry_ingredientes.insert(0, ','.join(receta['ingredientes']))
            self.entry_ingredientes.pack()
            
            self.label_instrucciones = tk.Label(self.ventana_editar, text="Instrucciones:")
            self.label_instrucciones.pack()
            self.entry_instrucciones = tk.Entry(self.ventana_editar)
            self.entry_instrucciones.insert(0, receta['instrucciones'])
            self.entry_instrucciones.pack()
            
            self.boton_guardar = tk.Button(self.ventana_editar, text="Guardar", command=self.actualizar_receta)
            self.boton_guardar.pack()
        else:
            messagebox.showwarning("Editar Receta", "Receta no encontrada.")

    def actualizar_receta(self):
        nombre = self.entry_nombre.get().strip()
        etiquetas = [et.strip().lower() for et in self.entry_etiquetas.get().split(',')]
        ingredientes = [ing.strip() for ing in self.entry_ingredientes.get().split(',')]
        instrucciones = self.entry_instrucciones.get().strip()

        if nombre and etiquetas and ingredientes:
            self.recomendacion.editar_receta(nombre, etiquetas, ingredientes, instrucciones)
            messagebox.showinfo("Editar Receta", "Receta editada exitosamente.")
            self.ventana_editar.destroy()
        else:
            messagebox.showwarning("Editar Receta", "Todos los campos son obligatorios.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
