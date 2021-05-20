from enum import Enum

class A(Enum):
    V = 0
    C = 1
    F = 2


def test(x):
    result = {
        'a': 1,
        'b': 2,
    }
    return result.get(x, 0)


print(test('c'))
