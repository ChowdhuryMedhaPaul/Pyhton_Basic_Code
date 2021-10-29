is_hot= True

if is_hot:
    print('hot day')
    print('drink water')
print("enjoy")


is_hot= False

if is_hot:
    print('hot day')
else:
    print('cold day')
print("enjoy")


is_hot= True
is_cold= False

if is_hot:
    print('hot day')
    print('drink water')
elif is_cold:
    print('cold day')
    print('drink tea')

else:
    print("enjoy")



is_credit=True
if is_credit:
    pay=1000000*0.1
else:
    pay=1000000*0.2
print(pay)
print(f"Payment: ${pay}")


income=True
credit= True

if income and credit:
    print("get loan")

income=True
credit= False

if income or credit:
    print("get loan")

    
not_crime=False
credit= True

if  credit and not not_crime:
    print("get loan")

name="J"
if len(name) < 3:
    print("Char")
elif len(name) > 50:
    print("not char")
else:
    print("good")

weight =int(input("weight: "))
unit= input("(L)lb or (K)kg :")

if unit.upper() == 'L':
     con=weight*0.45
     print(f"your weight {con} kilos.")
else:
    con=weight/0.45
    print(f"your weight {con} pounds.")



