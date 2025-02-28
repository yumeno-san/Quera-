n = int(input())
person_list = []
for i in range(1, n+1) :
    t = input().split()
    person_list.append(t)

sorted_list = sorted(person_list, key=lambda x : int(x[1]) , reverse=True)
for key, value in sorted_list :
    print(key)
    break
