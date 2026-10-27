"""Backend mínimo (FastAPI) para practicar CI, SonarCloud y Dependabot."""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Catálogo de streaming", version="1.0.0")

PELICULAS = {
    1: {"id": 1, "titulo": "El viaje", "genero": "aventura"},
    2: {"id": 2, "titulo": "Noche larga", "genero": "suspenso"},
    3: {"id": 3, "titulo": "Risas", "genero": "comedia"},
}

PRECIO_MENSUAL = {"basico": 5000, "estandar": 8000, "premium": 12000}
MESES_PARA_DESCUENTO = 12
PORCENTAJE_CON_DESCUENTO = 90


def calcular_precio(plan: str, meses: int) -> int:
    """Devuelve el total a pagar. Contratando 12 meses o más hay 10% de descuento."""
    if plan not in PRECIO_MENSUAL:
        raise ValueError(f"Plan desconocido: {plan}")
    if meses < 1:
        raise ValueError("La cantidad de meses debe ser al menos 1")
    total = PRECIO_MENSUAL[plan] * meses
    if meses >= MESES_PARA_DESCUENTO:
        total = total * PORCENTAJE_CON_DESCUENTO // 100
    return total


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/peliculas")
def listar_peliculas() -> list[dict]:
    return list(PELICULAS.values())


@app.get("/peliculas/{pelicula_id}", responses={404: {"description": "No existe"}})
def obtener_pelicula(pelicula_id: int) -> dict:
    pelicula = PELICULAS.get(pelicula_id)
    if pelicula is None:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    return pelicula


@app.get("/precio", responses={400: {"description": "Plan o meses inválidos"}})
def precio(plan: str, meses: int) -> dict:
    try:
        total = calcular_precio(plan, meses)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    return {"plan": plan, "meses": meses, "total": total}
