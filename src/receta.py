class Receta:
    def __init__(self, nombre, etiquetas, ingredientes, instrucciones):
        self.nombre = nombre
        self.etiquetas = etiquetas
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones

    def __str__(self):
        return f"Receta: {self.nombre}\nEtiquetas: {', '.join(self.etiquetas)}\nIngredientes: {', '.join(self.ingredientes)}\nInstrucciones: {self.instrucciones}"
