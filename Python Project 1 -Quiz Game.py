print ("Welcome to my computer Quiz!")

playing =  input("Do you want to play?")

if playing.lower() != "yes": 
    quit()

print("Okay! Let's play:") 
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")

answer = input("What does HTTP stand for? ")
if answer.lower() == "hypertext transfer protocol": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")

answer = input("What does API stand for? ")
if answer.lower() == "application programming interface": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")   

answer = input("What does ORM stand for? ")
if answer.lower() == "object relational mapping": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")   

answer = input("What does IDE stand for? ")
if answer.lower() == "integrated development environment": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")

answer = input("What does GUI stand for? ")
if answer.lower() == "graphical user interface": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")

answer = input("What does CRUD stand for? ")
if answer.lower() == "create, read, update and delete": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")

answer = input("What does PEP stand for? ")
if answer.lower() == "python enhancement proposal": 
    print('Correct!')
    score += 1
else: 
    print ("Incorrect!")

print ("You got " + str(score)+ " questions correct")
print ("You got " + str((score/10)* 100) + "%.")


