move = input("Kérem a robot mozgását: ")

E = move.count('E')
print(f"E betűk száma: {E}")

D = move.count('D')
print(f"D betűk száma: {D}")

N = move.count('N')
print(f"N betűk száma: {N}")

K = move.count('K')
print(f"K betűk száma: {K}")


move_list = []
for i in move:
    move_list.append(i)

if E > D:
    for i in range(D):
        move_list.remove('E')
        move_list.remove('D')
else:
    for i in range(E):
        move_list.remove('E')
        move_list.remove('D')

if N > K:
    for i in range(N):
        move_list.remove('N')
        move_list.remove('K')
else:
    for i in range(K):
        move_list.remove('N')
        move_list.remove('K')

move_new = ''
for i in move_list:
    move_new+= i

print(f'Egy legrövidebb útvonal parancsa: {move_new}')