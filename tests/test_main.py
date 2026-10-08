import pytest
from fastapi.testclient import TestClient

from app.main import app, calcular_precio

client = TestClient(app)


def test_health():
    respuesta = client.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "ok"}


def test_listar_peliculas():
    respuesta = client.get("/peliculas")
    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 3


def test_obtener_pelicula_existente():
    respuesta = client.get("/peliculas/1")
    assert respuesta.status_code == 200
    assert respuesta.json()["titulo"] == "El viaje"


def test_obtener_pelicula_inexistente():
    respuesta = client.get("/peliculas/999")
    assert respuesta.status_code == 404


def test_precio_sin_descuento():
    assert calcular_precio("basico", 2) == 10000


def test_precio_con_descuento_anual():
    assert calcular_precio("premium", 12) == 129600


def test_precio_plan_desconocido():
    with pytest.raises(ValueError):
        calcular_precio("gratis", 1)


def test_precio_meses_invalidos():
    with pytest.raises(ValueError):
        calcular_precio("basico", 0)


def test_endpoint_precio_ok():
    respuesta = client.get("/precio", params={"plan": "estandar", "meses": 3})
    assert respuesta.status_code == 200
    assert respuesta.json() == {"plan": "estandar", "meses": 3, "total": 24000}


def test_endpoint_precio_plan_invalido():
    respuesta = client.get("/precio", params={"plan": "gratis", "meses": 3})
    assert respuesta.status_code == 400
