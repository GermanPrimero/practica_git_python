import pytest

from app import calcular_iva, validar_nombre, es_cadena_valida


def test_validar_nombre_quita_espacios_exteriores():
    assert validar_nombre("  Ana  ") == "Ana"


def test_validar_nombre_rechaza_cadena_vacia():
    with pytest.raises(ValueError, match="no puede estar vacío"):
        validar_nombre("   ")


def test_validar_nombre_rechaza_tipo_incorrecto():
    with pytest.raises(TypeError, match="cadena de texto"):
        validar_nombre(123)


def test_calcular_iva_con_porcentaje_por_defecto():
    assert calcular_iva(10) == 12.1


def test_calcular_iva_con_porcentaje_personalizado():
    assert calcular_iva(100, 10) == 110


def test_calcular_iva_rechaza_precio_negativo():
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        calcular_iva(-1)

'''Nuevas funciones añadidas'''
def test_es_cadena_valida():
    assert es_cadena_valida("Hola") is True


def test_es_cadena_valida_con_espacios():
    assert es_cadena_valida("  Hola  ") is True


def test_es_cadena_vacia():
    assert es_cadena_valida("   ") is False


def test_es_cadena_valida_rechaza_tipo_incorrecto():
    with pytest.raises(TypeError):
        es_cadena_valida(123)
