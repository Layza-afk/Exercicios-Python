# Multiplos

def multiplos():
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            print(f'3 * {i/3} ou 5 * {i/5}')
        elif i % 3 == 0:
            print(f'3 * {i/3}')
        elif i % 5 == 0:
            print(f'5 * {i/5}')
        else:
            print(i)

print(multiplos())