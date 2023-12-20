from functools import lru_cache
def moves(h):
    return h+1, h*2

@lru_cache(None)
def game(h):
    if h>=129:
        return "W"
    if any(game(m) == "W" for m in moves(h)):
        return "П1"
    if all(game(m) =="П1" for m in moves(h)):
        return "В1"
    if any(game(m) =="В1" for m in moves(h)):
        return "П2"
    if all(game(m) =="П1" or game(m) =="П2" for m in moves(h)):
        return "В2"
for s in range(1,128):
    if game(s)=="В2":
        print(s, game(s))
