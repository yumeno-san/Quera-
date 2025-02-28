n ,a1, a2, a3, a4 = map(int, input().split())

a = 1
for i in range(1, n+1):
    if (i % a1 == 0) or (i % a2 == 0) or (i % a3 == 0) or (i % a4 == 0):
        a += 1
print(a-1)