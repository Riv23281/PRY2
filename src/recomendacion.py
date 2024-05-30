class Recomendacion:
    def __init__(self, conexion):
        self.conexion = conexion

    def recomendar_recetas(self, etiquetas):
        etiquetas_str = ', '.join([f"'{etiqueta}'" for etiqueta in etiquetas])
        query = f"MATCH (r:Receta) WHERE any(etiqueta IN r.etiquetas WHERE etiqueta IN [{etiquetas_str}]) RETURN r"
        resultados = self.conexion.ejecutar_consulta(query)
        return [record['r'] for record in resultados]

    def obtener_todas_recetas(self):
        query = "MATCH (r:Receta) RETURN r"
        resultados = self.conexion.ejecutar_consulta(query)
        return [record['r'] for record in resultados]

    def recomendar_aleatoria(self):
        query = "MATCH (r:Receta) RETURN r ORDER BY rand() LIMIT 1"
        resultados = self.conexion.ejecutar_consulta(query)
        if resultados:
            return resultados[0]['r']
        return None

    def agregar_receta(self, nombre, etiquetas, ingredientes, instrucciones):
        query = (
            "CREATE (r:Receta {nombre: $nombre, etiquetas: $etiquetas, ingredientes: $ingredientes, instrucciones: $instrucciones})"
        )
        self.conexion.ejecutar_consulta(query, {"nombre": nombre, "etiquetas": etiquetas, "ingredientes": ingredientes, "instrucciones": instrucciones})

    def eliminar_receta(self, nombre):
        query = "MATCH (r:Receta {nombre: $nombre}) DETACH DELETE r"
        self.conexion.ejecutar_consulta(query, {"nombre": nombre})

    def obtener_receta(self, nombre):
        query = "MATCH (r:Receta {nombre: $nombre}) RETURN r"
        resultados = self.conexion.ejecutar_consulta(query, {"nombre": nombre})
        if resultados:
            return resultados[0]['r']
        return None

    def editar_receta(self, nombre, etiquetas, ingredientes, instrucciones):
        query = (
            "MATCH (r:Receta {nombre: $nombre}) "
            "SET r.etiquetas = $etiquetas, r.ingredientes = $ingredientes, r.instrucciones = $instrucciones"
        )
        self.conexion.ejecutar_consulta(query, {"nombre": nombre, "etiquetas": etiquetas, "ingredientes": ingredientes, "instrucciones": instrucciones})
