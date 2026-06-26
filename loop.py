#syntax
for i in [1,2,3,4,5,6]:
    print(i)

for z in "broadway":
    print(z)

a={
    "name":"Rajat",
    "address":"Baneshwor"
}

for i in a.values():
    print(i)

for i in a:
    print(i,a[i])

#range(initial value, limit, increment)
#initial value is 0 if not given
#increment value is 1 if not given
for i in range(1,11,1):
    print(f' 7 X {i} ={7*i}')

#break and continue
for i in range(1,11,1):
    if i==6:
        break
    print(i)

for i in range(1,11,1):
    if i==6:
        continue
    print(i)

for i in range(1,11,1):
    if i==6 or i==8:
        continue
    print(i)


#nested for loop

n=[10,20,20,10]

for i in set(n):
    for j in range(1,11,1):
        print(f' {i} X {j} = {i*j}')
    print('\n')

result = []
for i in range(1,5):
    data = int(input(f"Enter the {i}nd number"))
    result.append(data)

for i in set(result):
    for j in range(1,11,1):
        print(f' {i} X {j} = {i*j}')
    print('\n')

#a=[]//empty list
#a={}//empty dictionary
#a=()//empty tuple
#data=set()//empty set

#While loop
 
i=1
while(i<=10):
    print(i)
    i=i+1