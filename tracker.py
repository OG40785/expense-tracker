# controller.py
import argparse
import validations
from expences import ExpencesTracker


def start():
    request = commands()
      
    if request.operation  == "add":
        month = request.month[0]
        year = request.year[0]
        amount = request.amount[0]
        shop = request.shop[0]
        category = request.category[0]
        date = request.date[0]
        description = request.description[0] 

        if not do_validations(month,year,description):
            exit()

        add_expense(year,month,amount, shop, date, category, description)
        
          
    elif request.operation  == "delete":
        amount_to_delete = request.amount[0]
        print(f"Deleting amount: {amount_to_delete}")

    elif request.operation  == "":
        print("No action provided. Use --help for options.")

    else:
        print("This command  does not exist. Use --help for options.")



def do_validations(month: str, year: str, description: str) -> bool:
    message = ''
    if not validations.validate_month(month):
        message += 'Please enter a valid month name in English (e.g., January, February, etc.).\n'
    if not validations.validate_year(year):
        message += 'Please enter a valid year between 2000 and 2025 inclusive.\n'
    if not validations.validate_description(description):
        message += 'Description must be 5 words or fewer.\n'
    if message != '':
        print(message)
        return False
    else:
        return True




def add_expense(year, month, amount, shop, category, description, date=None):
    try:
        tracker = ExpencesTracker(year)
        tracker.add_expense(month, amount, shop, category, description, date)
        print("Expense successfully added.")
    except Exception as e:
        print("Error adding expense.")
        print(e)

def delete_expense(year, amount):
    try:
        tracker = ExpencesTracker(year)
        tracker.delete_expense(amount)
        print("Expense successfully deleted.")
    except Exception as e:
        print("Error deletting expense.")
        print(e)

def list_expenses(year):
    try:
        tracker = ExpencesTracker(year)
        expenses = tracker.list_expenses()
        print(expenses)
    except Exception as e:
        print("Error listing expenses.")
        print(e)




def commands():
    # Create the parser
    parser = argparse.ArgumentParser(description="Expense tracker")
    
    # Add the command-line arguments

    subparsers = parser.add_subparsers(dest='operation',help="Available actions")
   
    add_parser = subparsers.add_parser('add', help='Addition')
    add_parser.add_argument('year', nargs=1, type=str, help='Year of the expence')
    add_parser.add_argument('month', nargs=1, type=str, help='Month of the expence')
    add_parser.add_argument('amount', nargs=1, type=float, help='Amount to add to the expense (e.g., 20.50)')
    add_parser.add_argument('shop', nargs=1, type=str, help='Name of the shop where the expense occurred (e.g., SuperMart)')
    add_parser.add_argument('date', nargs=1, type=str, help='Date of the expense in format YYYY-MM-DD (e.g., 2024-12-13)')
    add_parser.add_argument('category', nargs=1, type=str, help='Category of the expense (e.g., Groceries, Electronics)')
    add_parser.add_argument('description', nargs=1, type=str, help='Description of the expense, limited to 5 words (e.g., Bought snacks for the party)')

    delete_parser = subparsers.add_parser('delete', help='Deletion')
    delete_parser.add_argument('amount', nargs=1, type=float, help='Amount to delete')
    
    list_parser = subparsers.add_parser('list', help='List all expences')

    total_parser = subparsers.add_parser('total',help ='Show total expences')
   
    args = parser.parse_args()
  
    # Parse the arguments
    return parser.parse_args()


