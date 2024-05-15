from functools import lru_cache


def moves(x, y):
    return (x + 2, y), (x * 2, y), (x, y + 2), (x, y * 2)


@lru_cache(None)
def game(x, y):
    if x + y >= 74:
        return "W"  # типа победа
    elif any(game(*move) == "W" for move in moves(x, y)):
        return "P1"
    elif all(game(*move) == "P1" for move in moves(x, y)):
        return "V1"
    elif any(game(*move) == "V1" for move in moves(x, y)):
        return "P2"
    elif all(game(*move) == "P1" or game(*move) == "P2" for move in moves(x, y)):
        return "V12"


for i in range(1, 67):
    if game(7, i) == "V12":
        print(i, game(7, i))
