"""Funciones sencillas para practicar Python, pytest y Git."""


def validar_nombre(nombre: str) -> str:
    """Devuelve el nombre si contiene texto; si no, lanza ValueError."""
    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser una cadena de texto.")
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    return nombre


def calcular_iva(precio: float, porcentaje: float = 21) -> float:
    """Calcula el precio con IVA. Rechaza valores negativos."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if porcentaje < 0:
        raise ValueError("El porcentaje no puede ser negativo.")
    return round(precio * (1 + porcentaje / 100), 2)


def main() -> None:
    nombre = validar_nombre("  Ana  ")
    total = calcular_iva(10)
    print(f"Hola, {nombre}. El precio con IVA es {total} €.")


if __name__ == "__main__":
    main()
