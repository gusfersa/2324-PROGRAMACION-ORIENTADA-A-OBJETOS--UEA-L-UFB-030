# Creación de un diccionario con información de un libro
libro = {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "publicado": 1967
}

# Acceso a un valor
print(libro["titulo"])  # Salida: Cien años de soledad

# Modificación de un valor
libro["publicado"] = 1968

# Agregar un nuevo par clave-valor
libro["genero"] = "Realismo mágico"

# Eliminación de un par clave-valor
del libro["genero"]

# Uso de .items() para iterar sobre el diccionario
for clave, valor in libro.items():
    print(f"{clave}: {valor}")
