from app.estadisticas import duracion_promedio, la_mas_larga, por_decada

CATALOGO = [
    {"titulo": "Corta", "duracion": 80, "anio": 1994},
    {"titulo": "Media", "duracion": 100, "anio": 1999},
    {"titulo": "Larga", "duracion": 150, "anio": 2003},
]


def test_duracion_promedio():
    assert duracion_promedio(CATALOGO) == 110.0


def test_duracion_promedio_lista_vacia():
    assert duracion_promedio([]) == 0


def test_la_mas_larga():
    assert la_mas_larga(CATALOGO) == "Larga"


def test_la_mas_larga_lista_vacia():
    assert la_mas_larga([]) is None


def test_por_decada():
    assert por_decada(CATALOGO) == {1990: 2, 2000: 1}
