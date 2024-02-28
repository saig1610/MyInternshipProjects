print("PYTHON PROGRAMMING PROJECT - 3\n\n\n")

#title of the project
print("PROJECT TITLE : EXPENSE TRACKER\n") 
print("THIS CAN BE USED TO TRACK/STORE/VIEW YOUR EXPENSE\n")





#defining lifts and entering sample inputs
expenses = []
expense1 = {'amount': '1400', 'category': 'Dress'}
expenses.append(expense1)
expense2 = {'amount': '2155', 'category': 'Fuel'}
expenses.append(expense2)

#Expense tracker menu 
def printMenu():
  print("Please choose from one of the following options...")
  print("1. Add A New Expense")
  print("2. Remove An Exepense")
  print("3. List All Exepenses")

#defining functions to add expenses 
  
def addExpense(amount, category):
  expense = {'amount': amount, 'category': category}
  expenses.append(expense)

#defining functions to remove expenses 
  
def removeExpense():
  while True:
    listExpenses()
    print("What expense would you like to remove?")
    try:
      expenseToRemove = int(input("> "))
      del expenses[expenseToRemove]
      break
    except:
      print("Invalid input. Please try again.")

#defining functions to show the expenses (viewing the data)
def listExpenses():
  print("\n------------------------------------")
  print("............YOUR EXPENSES.............")
  print("------------------------------------\n")
  counter = 0
  for expense in expenses:
    print("#", counter, " - ", expense['amount'], " - ", expense['category'])
    counter += 1
  print("\n\n")

#how the expense tracker works 
if __name__ == "__main__":
  while True:
    ### Prompt the user
    printMenu()
    optionSelected = input("> ")

    if (optionSelected == "1"):
      print("How much was this expense?")
      while True:
        try:
          amountToAdd = input("> ")
          break
        except:
          print("Invalid input. Please try again.")

      print("What category was this expense?")
      while True:
        try:
          category = input("> ")
          break
        except:
          print("Invalid input. Please try again.")

      addExpense(amountToAdd, category)
    elif (optionSelected == "2"):
      removeExpense()
    elif (optionSelected == "3"):
      listExpenses()
    else:
      print("Invalid input. Please try again.")