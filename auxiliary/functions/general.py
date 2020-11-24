def insert_into_list(lst, el, pos=None):
    pos = len(lst) if pos is None else pos
    return lst[:pos] + [el] + lst[pos:]

def remove_from_list(lst, pos):
    return lst[:pos] + lst[pos + 1:]
