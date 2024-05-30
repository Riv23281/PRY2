import csv
import os

class ManejadorUsuarios:
    def __init__(self):
        self.archivo_usuarios = "InfoUsuarios.csv"
        self.usuarios = []

        # Comprobar si el archivo de usuarios ya existe
        if os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.usuarios.append(row)

    def crear_usuario(self, nombre, contraseña):
        # Verificar si el usuario ya existe
        for usuario in self.usuarios:
            if usuario["Nombre"] == nombre:
                print("¡El usuario ya existe!")
                return False

        # Agregar el nuevo usuario
        self.usuarios.append({"Nombre": nombre, "Contraseña": contraseña})
        self.guardar_usuarios()
        print("¡Usuario creado con éxito!")
        return True

    def iniciar_sesion(self, nombre, contraseña):
        # Verificar si el usuario existe y la contraseña es correcta
        for usuario in self.usuarios:
            if usuario["Nombre"] == nombre and usuario["Contraseña"] == contraseña:
                print("¡Inicio de sesión exitoso!")
                return True
        print("¡Nombre de usuario o contraseña incorrectos!")
        return False

    def guardar_usuarios(self):
        # Guardar la lista de usuarios en el archivo CSV
        with open(self.archivo_usuarios, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Nombre", "Contraseña"])
            writer.writeheader()
            for usuario in self.usuarios:
                writer.writerow(usuario)
