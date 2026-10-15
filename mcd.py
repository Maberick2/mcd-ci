def mcd(a, b):
    """Calcula el máximo común divisor de dos números enteros.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.

    Returns:
        int: Máximo común divisor, siempre positivo.

    Raises:
        TypeError: Si alguna entrada no es un entero.
        ValueError: Si ambos números son cero.
    """
    if type(a) is not int or type(b) is not int:
        raise TypeError("Ambos valores deben ser números enteros.")

    if a == 0 and b == 0:
        raise ValueError("El MCD de cero y cero no está definido.")

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a