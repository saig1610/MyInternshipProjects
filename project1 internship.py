#PROJECT 1- BASIC MULTIPLE CHOICE QUIZ GAME USING PYHTON
#STARTING THE QUIZZ GAME
print("PROJECT 1")
print("Welcome to quiz time with python")
name=str(input("Enter your name to start:"))
print("NOTE: ONLY THE OPTION MUST BE GIVEN AS ANSWER")

# Defining Score variables 
x = 0
score = x


# Question One 

print("(Q1)WHO WON THE 2022 FOOTBALL WORLD CUP?") 
answer_1 = input("a)France\nb)Argentina\nc)Germany\nd)Portugal\n ENTER YOUR ANS:")
if answer_1.lower() == "b":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The correct answer is option (b)Argentina\n")


# Question Two
print("(Q2)Who is the 45th president of the United States?")
answer_2 = input("a)Barack Obama\nb)Hillary Clinton\nc)Donald Trump\nd)Tom Brady\n ENTER YOUR ANS:")
if answer_2.lower() == "c":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The correct answer is option (c)Donald Trump\n")



# Question Three
print("(Q3)WHO PAINTED THE MONA LISA?") 
answer_1 = input("a)Vincent Van Gogh\nb)Pablo Picasso\nc)Leonardo da Vinci\nd)Michealengelo\n ENTER YOUR ANS:")
if answer_1.lower() == "c":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The right answer is option (c)Leonardo da Vinci\n")


# Question Four
print("(Q4)What was the last year the Toronto Maple Leafs won the Stanley   Cup?")
answer_4 = input("a)1967\nb)1955\nc)1987\nd)1994\n ENTER YOUR ANS:")
if answer_4.lower() == "a":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The right answer is option (a)1967\n" )


# Question Five 
print("(Q5)WHO IS THE GREEK GOD OF THE SEA") 
answer_1 = input("a)Zeus\nb)Hades\nc)Apollo\nd)Posiedon\n ENTER YOUR ANS:")
if answer_1.lower() == "d":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The correct answer is (d)Posiedon\n")


# Counting Total Score and displaying it
score = float(x / 5) * 100
print("CONGURATULATIONS," ,name,"!!!")
print(x,"out of 5, that is",score, "%")#displying marks in percentage
print("Thank you for playing!!")
