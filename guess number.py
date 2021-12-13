import random
response= random.randint(1,99)
name =input("what is your name?")
guess =int (input("what is your guess?"))

while guess !=response:
    if guess> response:
        print ('mine is smaller')
    else:
        print('mine is larger')   
    guess =int (input("what is yOur guess?"))

print("woOoOoOwww " , name,"well done!")  
