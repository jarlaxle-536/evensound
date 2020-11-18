def insert_into_list(lst, el, pos):
    pos = len(lst) if pos is None else pos
    return lst[:pos] + [el] + lst[pos:]
