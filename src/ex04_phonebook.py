"""
EX04 (Texto) · Listín telefónico en fichero

Vas a implementar un pequeño "CRUD" (Crear/Leer/Actualizar/Borrar) de contactos,
guardados en un fichero de texto.

Formato del fichero (una línea por contacto):
nombre,telefono

Ejemplo:
Ana,600123123
Luis,600000000

Para que el ejercicio sea más limpio, se proponen dos funciones "privadas":
- _load_phonebook(): lee el fichero y lo convierte en dict
- _save_phonebook(): guarda el dict en el fichero

Luego, las funciones públicas usan esas helpers:
- add_contact(): alta/actualización
- get_phone(): consulta
- remove_contact(): baja
"""

from __future__ import annotations

from pathlib import Path


def _load_phonebook(path: str | Path) -> dict[str, str]:
    """
    Carga el listín desde `path` y devuelve un diccionario {name: phone}.

    Reglas:
    - Si el fichero no existe, devuelve {} (NO es error).
    - Ignora líneas vacías.
    - Cada línea debe tener exactamente 2 partes separadas por coma:
      "nombre,telefono"
      Si alguna línea está mal formada, lanza ValueError.
    - Recorta espacios alrededor de nombre y teléfono con .strip().

    Consejo:
    - Usa `with open(..., encoding="utf-8") as f:`
    - Recorre línea a línea con `for line in f:`
    """
    agenda = {}
    ruta = Path(path)
    
    if ruta.exists() == False:
        return agenda

    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            
            if linea == "":
                continue
            
            partes = linea.split(",")
            
            if len(partes) != 2:
                raise ValueError("Línea mal formada: " + linea)
            
            nombre = partes[0].strip()
            telefono = partes[1].strip()
            agenda[nombre] = telefono
            
    return agenda
    

def _save_phonebook(path: str | Path, phonebook: dict[str, str]) -> None:
    """
    Guarda el diccionario en `path` en formato "nombre,telefono", una línea por contacto.

    Reglas:
    - Sobrescribe el fichero (modo 'w').
    - Puedes guardar en cualquier orden.
    - Usa encoding="utf-8".
    """
    with open(path, "w", encoding="utf-8") as archivo:
        for nombre in phonebook:
            telefono = phonebook[nombre]
            linea = nombre + "," + telefono + "\n"
            archivo.write(linea)
    


def add_contact(path: str | Path, name: str, phone: str) -> None:
    """
    Añade o actualiza un contacto (name -> phone) en el fichero.

    Reglas:
    - name y phone no pueden estar vacíos (tras strip). Si lo están, ValueError.
    - Si el contacto ya existe, se actualiza su teléfono.
    - Si no existe, se añade.

    Pista:
    - load -> modificar dict -> save
    """
    nombre = name.strip()
    telefono = phone.strip()
    
    if nombre == "":
        raise ValueError("El nombre no puede estar vacío")
    
    if telefono == "":
        raise ValueError("El teléfono no puede estar vacío")
    
    agenda = _load_phonebook(path)
    agenda[nombre] = telefono
    _save_phonebook(path, agenda)
    


def get_phone(path: str | Path, name: str) -> str | None:
    """
    Devuelve el teléfono del contacto `name` o None si no existe.

    Reglas:
    - Si el fichero no existe, devuelve None (porque no hay contactos).
    - `name` se compara tras strip().
    """
    agenda = _load_phonebook(path)
    nombre = name.strip()
    
    if nombre in agenda:
        return agenda[nombre]
        
    return None
    


def remove_contact(path: str | Path, name: str) -> bool:
    """
    Elimina el contacto `name` si existe.

    Devuelve:
    - True si se eliminó
    - False si no existía

    Reglas:
    - Si el fichero no existe, devuelve False.
    - `name` se compara tras strip().

    Pista:
    - load -> borrar si existe -> save si cambió
    """
    agenda = _load_phonebook(path)
    nombre = name.strip()
    
    if nombre in agenda:
        del agenda[nombre]
        _save_phonebook(path, agenda)
        return True
        
    return False
    
