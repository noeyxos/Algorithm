N, M = map(int, input().split())
lst = [0]*N

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        lst[x-1] = k
print(" ".join(map(str, lst)))