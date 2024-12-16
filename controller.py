# controller.py
import argparse
import validations
from expencesTracker import ExpencesTracker

def read_description()->str:
    try:
        with open('description.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Description file not found."

def start():
    try:
        request = commands()

        if request.operation == "add":
            year = request.year[0]
            month = request.month[0].capitalize()
            amount = request.amount[0]
            shop = request.shop[0].capitalize()
            date = request.date[0]
            category = request.category[0].capitalize()
            description = request.description[0].capitalize()

            if not do_validations(month, year, date, description):
                exit()

            add_expense(year, month, amount, shop, category, description, date)

        elif request.operation == "delete":
            year = request.year[0]
            month = request.month[0].capitalize()
            amount = request.amount[0]
            shop = request.shop[0].capitalize()
            date = request.date[0]

            if not do_validations(month, year, date):
                exit()
            delete_expense(year, month, amount, shop, date)

        elif request.operation == "deleteId":
            year = request.year[0]
            id = request.id[0]
            delete_expense_by_id(year, id)

        elif request.operation == "list":
            year = request.year[0]
            list_expenses(year)

        elif request.operation == "total":
            year = request.year[0]
            total_expenses(year)

    except Exception as e:
        print("Error")
        print(e)


def do_validations(month: str, year: str, date: str, description: str = None) -> bool:
    message = ""
    if not validations.validate_month(month):
        message += "Please enter a valid month name in English (e.g., January, February, etc.).\n"
    if not validations.validate_year(year):
        message += "Please enter a valid year between 2000 and 2025 inclusive.\n"
    if not validations.validate_date(date):
        message += (
            "Please enter a valid date in format YYYY-MM-DD (e.g., 2024-12-13).\n"
        )
    if not validations.validate_description(description):
        message += "Description must be 5 words or fewer.\n"
    if message != "":
        print(message)
        return False
    else:
        return True


def add_expense(
    year: str,
    month: str,
    amount: float,
    shop: str,
    category: str,
    description: str,
    date=None,
) -> None:
    try:
        tracker = ExpencesTracker(year)
        tracker.add_expense(month, amount, shop, category, description, date)
        print("Expense successfully added.")
    except Exception as e:
        print("Error adding expense.")
        print(e)


def delete_expense(year: str, month: str, amount: float, shop: str, date: str) -> None:
    try:
        tracker = ExpencesTracker(year)
        tracker.delete_expense(month, amount, shop, date)
        print("Expense successfully deleted.")
    except Exception as e:
        print("Error deletting expense.")
        print(e)


def delete_expense_by_id(year: str, id: int) -> None:
    try:
        tracker = ExpencesTracker(year)
        tracker.delete_expence_by_id(id)
        print("Expense successfully deleted.")
    except Exception as e:
        print("Error deletting expense.")
        print(e)


def list_expenses(year: str) -> None:
    try:
        tracker = ExpencesTracker(year)
        expenses = tracker.list_expenses()
        print(expenses)
    except Exception as e:
        print("Error listing expenses.")
        print(e)


def total_expenses(year) -> None:
    try:
        tracker = ExpencesTracker(year)
        expenses = tracker.amount_total()
        print(f"Total expenses done in {year} = {expenses}")
    except Exception as e:
        print("Error listing expenses.")
        print(e)


def commands() -> argparse.Namespace:
    text = read_description()
    # Create the parser
    parser = argparse.ArgumentParser(prog='Expence tracker',description=text)

    # Add the command-line arguments

    subparsers = parser.add_subparsers(dest="operation", help="Available actions")


    add_parser = subparsers.add_parser("add", help="Adds a new expense to the tracker.")
    add_parser.add_argument("--year", nargs=1, type=str, help="Year of the expence")
    add_parser.add_argument("--month", nargs=1, type=str, help="Month of the expence")
    add_parser.add_argument(
        "--amount",
        nargs=1,
        type=float,
        help="Amount to add to the expense (e.g., 20.50)",
    )
    add_parser.add_argument(
        "--shop",
        nargs=1,
        type=str,
        help="Name of the shop where the expense occurred (e.g., SuperMart)",
    )
    add_parser.add_argument(
        "--date",
        nargs=1,
        type=str,
        help="Date of the expense in format YYYY-MM-DD (e.g., 2024-12-13)",
    )
    add_parser.add_argument(
        "--category",
        nargs=1,
        type=str,
        help="Category of the expense (e.g., Groceries, Electronics)",
    )
    add_parser.add_argument(
        "--description",
        nargs=1,
        type=str,
        help="Description of the expense, limited to 5 words (e.g., Bought snacks for the party)",
    )
    delete_by_id_parser = subparsers.add_parser("deleteId", help="Deletes an expense by its unique ID.")
    delete_by_id_parser.add_argument(
        "--year", nargs=1, type=str, help="Year of the expence"
    )
    delete_by_id_parser.add_argument(
        "--id", nargs=1, type=int, help="ID of the expence"
    )

    delete_parser = subparsers.add_parser("delete", help="Deletes an expense")

    delete_parser.add_argument("--year", nargs=1, type=str, help="Year of the expence")
    delete_parser.add_argument(
        "--month", nargs=1, type=str, help="Month of the expence"
    )
    delete_parser.add_argument("--amount", nargs=1, type=float, help="Amount to delete")
    delete_parser.add_argument(
        "--shop",
        nargs=1,
        type=str,
        help="Name of the shop where the expense occurred (e.g., SuperMart)",
    )
    delete_parser.add_argument(
        "--date",
        nargs=1,
        type=str,
        help="Date of the expense in format YYYY-MM-DD (e.g., 2024-12-13)",
    )

    list_parser = subparsers.add_parser("list", help="Lists all recorded expenses.")
    list_parser.add_argument("--year", nargs=1, type=str, help="Year of the expence")

    total_amount_parser = subparsers.add_parser(
        "total", help="Shows the total amount of all expenses"
    )
    total_amount_parser.add_argument(
        "--year", nargs=1, type=str, help="Year of the expence"
    )

    args = parser.parse_args()

    return args
