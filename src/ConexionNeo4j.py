from neo4j import GraphDatabase

class ConexionNeo4j:
    def __init__(self, uri, usuario, contraseña):
        self.uri = uri
        self.usuario = usuario
        self.contraseña = contraseña
        self.driver = None
        self.session = None

    def conectar(self):
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.usuario, self.contraseña))
            self.session = self.driver.session()
            print("Conexión establecida con éxito a la base de datos de Neo4j.")
        except Exception as e:
            print(f"No se pudo establecer la conexión: {e}")

    def cerrar_conexion(self):
        if self.session:
            self.session.close()
            print("Conexión cerrada correctamente.")
        if self.driver:
            self.driver.close()

    def ejecutar_consulta(self, consulta):
        try:
            return self.session.run(consulta)
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

if __name__ == "__main__":
   
    conexion = ConexionNeo4j("bolt://localhost:7687", "neo4j", "Hola12345")
    conexion.conectar()
    resultado = conexion.ejecutar_consulta("total nodos ")
    for registro in resultado:
        print(f"Total de nodos en la base de datos: {registro['total_nodos']}")
    conexion.cerrar_conexion()
