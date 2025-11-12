def is_safe(b, r, c, n):
    for i in range(r):
        if b[i][c] == 'Q' or (c-i >= 0 and b[i][c-i] == 'Q') or (c+i < n and b[i][c+i] == 'Q'):
            return False
    return True

def solve(b, r, n):
    if r == n: return True
    for c in range(n):
        if b[r][c] == '.' and is_safe(b, r, c, n):
            b[r][c] = 'Q'
            if solve(b, r+1, n): return True
            b[r][c] = '.'
    return False

n = int(input("n: "))
r, c = int(input("Row: ")), int(input("Col: "))
b = [['.']*n for _ in range(n)]
b[r][c] = 'Q'
if solve(b, r+1, n): [print(*row) for row in b]
else: print("No solution")
