from functools import lru_cache
def moves(h):
    a, b = h
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)

@lru_cache(None)
def game(h):
    a, b = h
    if (a+b)>=77:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "П1"
    if all(game(m) =="П1" for m in moves(h)):
        return "В1"
    if any(game(m) =="В1" for m in moves(h)):
        return "П2"
    if all(game(m) =="П1" or game(m) =="П2" for m in moves(h)):
        return "В2"
for s in range(1,100):
    h = 7, s
    if game(h)=="В2":
        print(s, game(h))
