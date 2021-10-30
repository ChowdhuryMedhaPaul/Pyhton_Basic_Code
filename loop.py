""" i=1
while i<=5:
    print('i'*i)
    i+=1
print("done")

num=9
i=0
while  i<3:
    guess= int(input('Guess: '))
    i+=1;
    if guess == 9:

       print('win')
       break
else:
    print("falied")



i=1;
while  i==1:
    st=input("string ")
    if st.lower() =="stop" :
        print("car stoped")
    elif st.lower() == "start":
        print("car started")

    elif st.lower() =='asd':
        print("none")
    else:
        break 


command=""
 while command.lower() != "quit":

command=""
sp=1;
st=1
while True:
    command= input("> ")
    if command.lower() == 'stop':
        if sp==1:


            print("car stoped")
            sp+=1
        else:
            print("car already stoped")
    
    elif  command.lower()== 'start':

        if st==1:
            print("car started")
            st+=1
        else:
            print("car already started")
    
    elif command.lower()=='any':

        print (
         hello,
         mr jhon
        your car is nice)
       
    elif command.lower()=="quit":
        break;
    else:
        print("donot")

"""

command=""
sp=1;
started = False
while True:
    command= input("> ").lower()
    if  command== 'start':
        if started:
            print("car is already started")
          
        else:
            started= True
            print("car just started")
           
    
    elif command == 'stop':
        if  not started:
            print("car already stoped")

        else:
            started=False
            print("car just stoped")
          
    
    elif command.lower()=='any':

        print ("""
hello,
mr jhon
your car is nice
        """)
    elif command.lower()=="quit":
        break;
    else:
        print("donot")
