n = int(input())

flag1 = False
for i in range(2, n) :
    if ((n % i) != 0) :
            flag1 = True

    elif n == 1 :
        print('zoj')

    else :
         flag1 = False
         break
    
if flag1 == True :
    if ((n % 2) == 1 ) :
        print('zoj')

else :
    print('fard')
    