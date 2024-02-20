def load_expenses(filename):
    expenses = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                category, amount = line.strip().split(',')
                expenses[category] = float(amount)

    except:
        FileNotFoundError 
        print('No workout data!')
    return expenses

def display_expeneses(expenses):
    print('Expenses:')
    for category, amount in expenses:
        print(f'Category: {category}, Amount: ${amount}')

def main():
    filename = 'Expenses.txt'
    expenses = load_expenses(expenses)
    display_expeneses(expenses)

if __name__ == '__main__':
    main()