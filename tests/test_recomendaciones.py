from app.recomendaciones import generos_disponibles, recomendar, resumen_por_genero

PELICULAS = [
    {"titulo": "Zeta", "genero": "aventura"},
    {"titulo": "Alfa", "genero": "aventura"},
    {"titulo": "Beta", "genero": "aventura"},
    {"titulo": "Gama", "genero": "aventura"},
    {"titulo": "Risas", "genero": "comedia"},
]


def test_recomendar_filtra_por_genero():
    assert recomendar(PELICULAS, "comedia") == ["Risas"]


def test_recomendar_respeta_el_limite_y_ordena():
    assert recomendar(PELICULAS, "aventura", limite=3) == ["Alfa", "Beta", "Gama"]


def test_recomendar_sin_coincidencias():
    assert recomendar(PELICULAS, "terror") == []


def test_resumen_por_genero():
    assert resumen_por_genero(PELICULAS) == {"aventura": 4, "comedia": 1}


def test_generos_disponibles():
    assert generos_disponibles(PELICULAS) == ["aventura", "comedia"]
