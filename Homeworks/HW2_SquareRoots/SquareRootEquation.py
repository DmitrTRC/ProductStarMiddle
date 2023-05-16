import math

"""
Solving Square Root Equation

"""


def get_discriminant(a: float, b: float, c: float) -> float:
    return b * b - 4 * a * c


def get_roots(a: float, b: float, c: float) -> list:
    discriminant = get_discriminant(a, b, c)
    if discriminant > 0:
        return [(-b + math.sqrt(discriminant)) / (2 * a), (-b - math.sqrt(discriminant)) / (2 * a)]
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        return []


if __name__ == '__main__':
    try:
        k_a, k_b, k_c = map(float, input().split())
    except ValueError:
        print('Incorrect input')
        exit(1)

    result = get_roots(k_a, k_b, k_c)

    if len(result) == 0:
        print('No roots')
    else:
        for index, root in enumerate(result):
            print(f'root {index + 1}: {root}')
