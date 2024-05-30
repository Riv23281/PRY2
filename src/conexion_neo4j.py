from neo4j import GraphDatabase

class ConexionNeo4j:
    def __init__(self, uri, usuario, contraseña):
        self.uri = uri
        self.usuario = usuario
        self.contraseña = contraseña
        self.driver = None

    def conectar(self):
        self.driver = GraphDatabase.driver(self.uri, auth=(self.usuario, self.contraseña))

    def cerrar(self):
        if self.driver:
            self.driver.close()

    def ejecutar_consulta(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            records = [record for record in result]
            print(f"Ejecutar consulta - Query: {query}, Parameters: {parameters}, Records: {records}")
            return records
