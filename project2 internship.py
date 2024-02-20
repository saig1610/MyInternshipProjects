print("PYTHON PROGRAMMING PROJECT - 2\n")

#title of the project
print("PROJECT TITLE : WORD COUNTER\n") 
print("THIS COUNTS THE NUMBER OF WORDS IN YOUR INPUT\n")


#getting the input from the user 
x=str(input("Enter your text here:\n"))


#error correction(cancelling invalid enteries)
if not x:
    print("!!!!!!!!!!!INVALID INPUT!!!!!!!!\n INPUT CANNOT BE EMPTY")


#word counting logic (function creation)   
if x==x:
    word_counter=len(x.split())

#DISPLAYING THE OUTPUT
    print("\nThe number of words in the given sentence is:",word_counter)
print("\nTHANK YOU FOR USING WORD COUNTER!!!")