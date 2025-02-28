n_input = int(input())
O = 0
output = []
while n_input != O :
    O += 1

    m, n = list(map(int, input().split()))
    
    
    
    # create matrix
    # every object of this list is a raw in matrix
    
    matrix = [input() for _ in range(m)]
    y = 0
    z = 0
    for i in matrix :
        for j in i :
            if j == '/' or j == '\\' or j == '_' :
                x = m - matrix.index(i) -1
                y += x
    
            if j == '/' or j == '\\' :
                y += .5
    output.append(y)

for i in output :
    print(i)
