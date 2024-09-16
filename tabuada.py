"""Apresente a tabuada completa dos números de 1 a 10."""

for i in range(1, 11):
    print(f'Tabuada do {i}\n')
    for j in range(1, 11):
        print(f'{i:2} x {j:2} = {i * j:2}')
    print('------------')
