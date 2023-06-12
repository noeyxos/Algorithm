N,M = map(int, input().split())

list = []
for _ in range(M):
    i,j,k = map(int, input().split())
    for n in range(i, j+1):
        list[n] = k