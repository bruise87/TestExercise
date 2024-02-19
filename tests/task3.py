def str_to_int(s):
    result = 0
    sig = 1
    for i in s:
        if i == "-":
            sig = -1
            continue
        curr = ord(i) - ord("0")
        result = result * 10 + curr
    return result * sig


assert str_to_int("275295") == 275295
assert str_to_int("-275295") == -275295


