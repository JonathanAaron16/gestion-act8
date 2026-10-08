# Catálogo de streaming — CI, calidad y seguridad

<!-- Reemplazar USUARIO, REPO y PROJECT_KEY por los valores reales -->
[![CI](https://github.com/JonathanAaron16/gestion-act8/actions/workflows/ci.yml/badge.svg)](https://github.com/USUARIO/REPO/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=f7d57eb8f38c647b56ed412de489604463e316ad&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=PROJECT_KEY)

Backend mínimo en FastAPI con tests (pytest), pipeline de GitHub Actions,
análisis estático en SonarCloud y Dependabot.

## Correr local

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest --cov=app
uvicorn app.main:app --reload    # http://localhost:8000/docs
```
