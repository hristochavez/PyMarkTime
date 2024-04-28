# PyMarkTime-Console

_Sistema de marcaciones de consola escrita en Python._

## Para usarlo debes tener:
- MySQL 8.0.36 o superior.
- Python 3.11.2

## Crea la BBDD:
- Ejecuta el archivo `sql-scripts/execute_as_root.sql` para crear al usuario de la BBDD.
- Crea el modelo usando el archivo `sql-scripts/schema.sql`
- Crea los procedimientos almacenados usando el archivo `sql-scripts/procedures.sql`

## Instala las dependencias del proyecto:
```sh
pip install -r requirements.txt
```

## Ejecuta el proyecto:

```sh
python main.py
```

