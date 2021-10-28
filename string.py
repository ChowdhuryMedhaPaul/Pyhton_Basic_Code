course = "Python's for beginners"

course1 = 'Python for "beginners"'
another= course1[:]
print(another)
print(course,course1)
print(course[0],course[9],course[-1],course[-9])
print(course1[0:3],course1[:5],course1[1:])

mul_string='''
 hello
 this is me
 hiw?
 oh great
'''
print(mul_string)

name='Janiffer'
print(name[1:-1])

first='Jhon'
last='Smith'
print(len(first))
message= first + '[' + last + '] is a coder'
print(message)
msg= f'{first} [{last}] is a coder'
print(msg)


course= 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('P'))
print(course.find('o'))
print(course.find('O'))
print(course.find('Beginners'))
print(course.replace('P','J'))
print(course.replace('p','J'))
print(course.replace('p','Jj'))
print(course.replace('Beginners','Absolute Beginners'))
print('Python' in course)
print('python' in course)