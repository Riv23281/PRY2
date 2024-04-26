import csv
import os

class ManejadorUsuarios:
    def __init__(self):
        self.archivo_usuarios = "InfoUsuarios.csv"
        self.usuarios = []


        if os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.usuarios.append(row)

    def crear_usuario(self, nombre, contraseña):

        for usuario in self.usuarios:
            if usuario["Nombre"] == nombre:
                print("El usuario ya existe")
                return False


        self.usuarios.append({"Nombre": nombre, "Contraseña": contraseña})
        self.guardar_usuarios()
        print("Usuario creado")
        return True

    def iniciar_sesion(self, nombre, contraseña):

        for usuario in self.usuarios:
            if usuario["Nombre"] == nombre and usuario["Contraseña"] == contraseña:
                print("Inicio de sesión exitoso")
                return True
        print("Nombre de usuario o contraseña incorrectos")
        return False

    def guardar_usuarios(self):

        with open(self.archivo_usuarios, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Nombre", "Contraseña"])
            writer.writeheader()
            for usuario in self.usuarios:
                writer.writerow(usuario)

if __name__ == "__main__":
    manejador_usuarios = ManejadorUsuarios()

    manejador_usuarios.crear_usuario("usuario1", "contraseña1")
    manejador_usuarios.iniciar_sesion("usuario1", "contraseña1")
