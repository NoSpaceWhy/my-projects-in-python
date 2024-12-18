def shopping():
    while True:
        item = input('Enter Name of the item: ')
        cost = input('Enter Cost of the item: ')
        if cost > budget:
            print("Insufficient budget!")
            continue
        else:
            with open('expenses.txt', 'a') as f:
                f.write(f"{item} | {cost}\n")
        mode()
        
def all_expenses():
    with open('expenses.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            item, cost = data.split('|')
            print("Item name: " + item + "\nCost: " + cost)
    mode()        

#Modes
def mode():
    print("Choose your mode (1 for shopping, 2 for showing all your expenses, 3 for changing the budget, q to quit): ")
    while True:
        choice = input().lower()
        if choice in ('1', '2', 'q', '3'):
            if choice == '1':
                shopping()
            elif choice == '2':
                all_expenses()
            elif choice == '3':
                budget = input("Enter your budget: ")
                if budget.isdigit():
                    print("Budget changed successfully.")
                    mode()
                else:
                    print("Invalid input. Please enter a number.")                    
            elif choice == 'q':
                quit()
        else:
            print("Invalid choice. Please enter 1 or 2 or 3 or q.")

#The starting point 
while True:
    budget = input("Enter the budget: ")
    if budget.isdigit():
        mode()
    else:
        print("Invalid input. Please enter a number.")
        continue