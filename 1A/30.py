from functools import lru_cache


def moves(x, y):
    possible_moves = []

    if x != 0:
        possible_moves.append((x - 1, y))
        if x != 1:
            possible_moves.append((x // 2, y))

    if y != 0:
        possible_moves.append((x, y - 1))
        if y != 1:
            possible_moves.append((x, y // 2))

    return possible_moves


@lru_cache(None)
def game(x, y):
    if x + y <= 20:
        return "W"
    elif any(game(*move) == "W" for move in moves(x, y)):
        return "P1"
    elif all(game(*move) == "P1" for move in moves(x, y)):
        return "V1"
    elif any(game(*move) == "V1" for move in moves(x, y)):
        return "P2"
    elif all(game(*move) in ("P1", "P2") for move in moves(x, y)):
        return "V12"


for i in range(10, 100):
    print(i, game(10, i))

print()
for i in range(10, 100):
    if game(10, i) == "V12":
        print(i, game(10, i))
