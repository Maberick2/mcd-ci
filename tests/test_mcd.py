import pytest

from mcd import mcd


def test_mcd_caso_correcto():
    assert mcd(12, 18) == 6


def test_mcd_numeros_coprimos():
    assert mcd(7, 13) == 1


def test_mcd_caso_limite():
    assert mcd(0, 8) == 8
    assert mcd(8, 0) == 8


def test_mcd_numeros_negativos():
    assert mcd(-12, 18) == 6


def test_mcd_ambos_cero():
    with pytest.raises(ValueError):
        mcd(0, 0)


@pytest.mark.parametrize(
    "a, b",
    [("12", 18), (12, 2.5), (True, 18), (None, 18)],
)
def test_mcd_entrada_incorrecta(a, b):
    with pytest.raises(TypeError):
        mcd(a, b)