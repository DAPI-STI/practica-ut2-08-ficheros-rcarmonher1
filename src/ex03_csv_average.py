"""
EX03 (CSV) · Calcular la media de una columna

Objetivo:
- Leer un CSV con cabecera (primera línea).
- Usar la librería estándar `csv` (recomendado: csv.DictReader).
- Convertir datos a float y calcular una media.

Ejemplo típico:
- Un CSV de calificaciones con columnas: name, average
"""

from __future__ import annotations

import csv
from pathlib import Path


def csv_average(path: str | Path, column: str) -> float:
    """
    Calcula y devuelve la media de la columna numérica `column` en el CSV `path`.

    Reglas:
    - El CSV tiene cabecera.
    - `column` debe existir en la cabecera. Si no, ValueError.
    - Todos los valores de esa columna deben poder convertirse a float. Si no, ValueError.
    - Si no hay filas de datos (CSV vacío tras la cabecera), ValueError.
    - Si el fichero no existe, FileNotFoundError.

    Ejemplo:
    name,average
    Ana,10
    Luis,6

    csv_average(..., "average") -> 8.0
    """
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        if reader.fieldnames is None or column not in reader.fieldnames:
            raise ValueError("La columna " + column + " no existe en el CSV.")
        
        total = 0.0
        n = 0
        
        for a in reader:
            valor = a[column]
            
            if valor.replace(".", "", 1).isdigit() == False:
                raise ValueError("El valor " + valor + " no se puede convertir a número.")
            
            valor_float = float(valor)
            total = total + valor_float
            n = n + 1
            
        if n == 0:
            raise ValueError("El CSV no tiene filas de datos.")
            
        return total / n
    
    raise NotImplementedError("Implementa csv_average(path, column)")
