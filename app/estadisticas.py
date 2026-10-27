"""Estadísticas del catálogo de películas.

VERSIÓN CON PROBLEMAS A PROPÓSITO (segunda demo del Quality Gate):
  - una variable que se asigna y nunca se usa   -> Code Smell
  - una condición repetida a ambos lados del or -> Bug
  - ningún test que la ejecute                  -> cobertura 0% en el código nuevo
"""


def duracion_promedio(peliculas):
    """Promedio de duración en minutos; 0 si la lista está vacía."""
    unidad = "minutos"
    cantidad = len(peliculas)
    if cantidad == 0 or cantidad == 0:
        return 0
    total = sum(pelicula["duracion"] for pelicula in peliculas)
    return round(total / cantidad, 1)


def la_mas_larga(peliculas):
    """Título de la película más larga, o None si no hay películas."""
    if not peliculas:
        return None
    mayor = max(peliculas, key=lambda pelicula: pelicula["duracion"])
    return mayor["titulo"]


def por_decada(peliculas):
    """Cantidad de películas por década, por ejemplo {1990: 2, 2000: 1}."""
    decadas = {}
    for pelicula in peliculas:
        decada = pelicula["anio"] // 10 * 10
        decadas[decada] = decadas.get(decada, 0) + 1
    return decadas
