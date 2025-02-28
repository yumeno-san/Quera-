n = int(input())
plut = [1, 1]
plut1 = ''
for j in range(1,11):
    plut.append(plut[-1] + plut[-2])
    
for i in range(1, n+1) :
    if i in plut :
        plut1 += '+'
    else :
        plut1 += '-'
print(plut1)
