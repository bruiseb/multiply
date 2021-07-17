""" The Steps to Egyptian Method / Russian Peasant Multiplication

To multiply numbers X and Y, the steps are.

1. Divide X in half repeatedly, ignoring remainders, until you get to 1.

2. Correspondingly double Y repeatedly, writing each new value in a row next to the halved X values.

3. Cross out the rows where the halved X values have an even number.

4. Add up the remaining numbers in the Y column.
"""


def egyptian_multiply(x: int, y: int) -> int:
    x_steps = [x]
    while x > 1:
        x_steps.append(x // 2)
        x = x // 2

    y_steps = [y]
    for _ in range(len(x_steps) - 1):
        y_steps.append(y * 2)
        y = y * 2

    return sum(y for x, y in zip(x_steps, y_steps) if x % 2 != 0)


def slide_multiply(x: int, y: int) -> int:
    """ Multiply two positive integers using the method identified in
        https://youtu.be/iZG25uBwU7M """
    length_x = len(str(x))
    length_y = len(str(y))
    string_y = str(y)
    x = [int(a) for a in reversed(str(x))]
    x.extend([0] * length_y)
    y = [0] * length_x
    y.extend([int(b) for b in string_y])
    result = ""
    slides = length_x + length_y - 1
    carry = 0
    for _ in range(slides):
        tail_y = y.pop()
        y = [tail_y] + y
        calc = sum(x[i] * y[i] for i in range(slides)) + carry
        result = str(calc % 10) + result
        carry = calc // 10
    if carry:
        result = str(carry) + result
    return int(result)


print(egyptian_multiply(1038, 82))
print(1038 * 82)
print(egyptian_multiply(3012, 1021))
print(3012 * 1021)

print(slide_multiply(1038, 82))
print(1038 * 82)
print(slide_multiply(3012, 1021))
print(3012 * 1021)
print(slide_multiply(58, 38))
