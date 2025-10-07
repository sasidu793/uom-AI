## x0="apple", y0="asfsppsdsdle" --> True if all characters of x0 are in y0 in oder , y0="bsdpple"---> false, y0="paple" --> false
def is_subsequence(x0, y0):
    x_len, y_len = len(x0), len(y0)
    x_idx, y_idx = 0, 0

    while x_idx < x_len and y_idx < y_len:
        if x0[x_idx] == y0[y_idx]:
            x_idx += 1
        y_idx += 1

    return x_idx == x_len
print(is_subsequence("apple", "asfsppsdsdle"))  # True
print(is_subsequence("apple", "bsdpple"))       # False
print(is_subsequence("apple", "paple"))         # False