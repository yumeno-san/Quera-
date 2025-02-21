x = input().split()
x_int = list(map(int, x))
from itertools import combinations
non_zero = [m for m in x_int if m != 0]

subset = list(combinations(non_zero, 3))

for i, j, k in subset :

    if (i + j > k) :
        if (i + k > j) : 
            if (k + j > i) :


                print ('YES')
                exit()
    
print('NO')