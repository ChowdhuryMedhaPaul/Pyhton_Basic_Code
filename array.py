
"""
names=['Jhon','Aninda','Raihan','Rai']
print(names)
names[1]='Paul'
print(names)
print(names[3])
print(names[-1])
print(names[2:3])

numbers=[1,2,5,5,4]
cnt=0
for i in numbers:
    if(i>=cnt):
        cnt=i
print(cnt)



matrix=[

    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
matrix[0][1]=20
matrix[2][2]=100
print(matrix[0][1],matrix[2][2])
print(matrix)


for row in matrix:
    for item in row:
        print(item)


numbers=[5,2,1,10,2]
numbers.append(20)
print(numbers)
print(numbers.count(2))
it=numbers.index(2)
print(it)
#it=numbers.index(100)
# print(it)
print(100 in numbers)
numbers.insert(2,9)
print(numbers)
numbers.remove(1)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
cp=numbers.copy()
print(cp)
numbers.pop()
print(numbers)
numbers.clear()
print(numbers)

num=[5,2,2,2,1]
item=num[0]
for i in num:
    if(i==i+1):
        num.remove(i)
        break
print(num)

num=[5,2,2,4,6,5,1]
unique=[]
for i in num:
    if i not in unique:
        unique.append(i)
print(unique)
"""


number=(1,2,3) # tuple
#number[0]=10
print(number)
x,y,z=number
print(x,y,z)
number=[1,2,3]
x,y,z=number
print(x,y,z)


