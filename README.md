# Práctica de Git, GitHub y pytest

Proyecto de ejemplo para practicar:
- funciones Python y excepciones;
- pruebas automatizadas con pytest;
- ramas, commits y Pull Requests;
- integración continua con GitHub Actions;
- revert, reset y resolución de conflictos.

## Preparar el entorno en Windows

Abre esta carpeta en VS Code y ejecuta en el terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
pytest
```

Si PowerShell no permite activar el entorno, no cambies la política de seguridad todavía: avisa y buscamos una alternativa adecuada.

## Ejecutar la aplicación

```powershell
python app.py
```

## Importante para la práctica

Haz los ejercicios de `git revert`, `git reset --hard` y conflictos solo en este repositorio de práctica. No los pruebes en un proyecto real con trabajo que quieras conservar.
