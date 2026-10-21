"""Recomendaciones de películas."""


def recomendar(peliculas, genero, limite=3):
    """Devuelve hasta `limite` títulos del género pedido."""
    titulos = []
    for pelicula in peliculas:
        if pelicula["genero"] == genero:
            titulos.append(pelicula["titulo"])
    titulos.sort()
    if len(titulos) > limite:
        titulos = titulos[:limite]
    return titulos


def resumen_por_genero(peliculas):
    """Cuenta cuántas películas hay de cada género."""
    resumen = {}
    for pelicula in peliculas:
        genero = pelicula["genero"]
        if genero not in resumen:
            resumen[genero] = 0
        resumen[genero] = resumen[genero] + 1
    return resumen


def generos_disponibles(peliculas):
    """Lista ordenada de géneros, sin repetir."""
    generos = []
    for pelicula in peliculas:
        if pelicula["genero"] not in generos:
            generos.append(pelicula["genero"])
    generos.sort()
    return generos
