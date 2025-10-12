LINES = 7
STARS = 7

for line in range(LINES):
    for _ in range(STARS - line, 0, -1):
        print('*', end='')
    print()
