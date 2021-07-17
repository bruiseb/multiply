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


assert slide_multiply(1038, 82) == (1038 * 82)
assert slide_multiply(3012, 1021) == (3012 * 1021)
assert slide_multiply(58, 38) == (58 * 38)
