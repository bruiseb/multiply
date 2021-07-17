""" The Steps to Egyptian Method / Russian Peasant Multiplication

To multiply numbers X and Y, the steps are.

1. Divide X in half repeatedly, ignoring remainders, until you get to 1.
2. Correspondingly double Y repeatedly, writing each new value in a row next to the halved X values.
3. Cross out the rows where the halved X values have an even number.
4. Add up the remaining numbers in the Y column.
"""


def egyptian_multiply(x: int, y: int) -> int:
    """ Multiply two positive integers using the method identified in
        https://youtu.be/qHXsKyVSPOU """
    x_steps = [x]
    while x > 1:
        x_steps.append(x // 2)
        x = x // 2

    y_steps = [y]
    for _ in range(len(x_steps) - 1):
        y_steps.append(y * 2)
        y = y * 2

    return sum(y for x, y in zip(x_steps, y_steps) if x % 2 != 0)


assert egyptian_multiply(1038, 82) == (1038 * 82)
assert egyptian_multiply(3012, 1021) == (3012 * 1021)
