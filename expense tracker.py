def save_expenses(filename, expenses):
    with open(filename, 'w') as file:
        for category, amount in expenses.items():
            file.write(f"{category},{amount}\n")

def main():
    expenses = {}

    try:
        numExpenses = int(input('Number of expenses: '))
    except ValueError:
        print('Must be a number!')
    
    for i in range(1, numExpenses+1):
        category = input('Type of purchase: ')
        try:
            amount = float(input(f'{category} cost: '))
        except ValueError:
            print('Invalid')
        expenses[category] = amount

    Filename = 'Expenses.txt'
    save_expenses(Filename, expenses)
    print('Expenses saved!') 

if __name__ == '__main__':
    main()
