

def obtener_recetas(opcion):
   
    recetas = {
        "Vegano": ["Ensalada de quinoa", "Tacos de coliflor asada", "Curry de lentejas"],
        "Con carne": ["Pollo al horno", "Lasaña de carne", "Hamburguesas caseras"]
    }
    

    if opcion in recetas:
        print("Recetas para la opción", opcion + ":")
        for receta in recetas[opcion]:
            print("-", receta)
    else:
        print("Opción no válida. Por favor, seleccione 'Vegano' o 'Con carne'.")


def main():
    print("Bienvenido a la aplicación de recetas de cocina.")
    print("Opciones:")
    print("1. Vegano")
    print("2. Con carne")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        obtener_recetas("Vegano")
    elif opcion == "2":
        obtener_recetas("Con carne")
    else:
        print("Opción no válida. Por favor, seleccione '1' o '2'.")

if __name__ == "__main__":
    main()
