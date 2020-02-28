def get_index_of(s, m):
    si = 0
    mi = 0
    next_arr = get_next_arr(m)

    while si < len(s) and mi < len(m):
        if s[si] == m[mi]:
            si += 1
            mi += 1
        elif next_arr[mi] == -1:
            si += 1
            mi = 0
        else:
            mi = next_arr[mi]

    return si - mi if mi == len(m) else -1

def get_next_arr(m):
    if len(m) == 1:
        return [-1]

    next_arr = [-1] * len(m)
    next_arr[0] = -1
    next_arr[1] = 0
    pos = 2
    cn = 0

    while pos < len(next_arr):
        if m[pos - 1] == m[cn]:
            next_arr[pos] = cn + 1
            pos += 1
            cn += 1
        elif cn > 0:
            cn = next_arr[cn]
        else:
            next_arr[pos] = 0
            pos += 1

    return next_arr