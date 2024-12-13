import pandas as pd
import os
import datetime

class ExpencesTracker:
    def __init__(self, year: str):
        self.year = year
        self.filename = f'expences_{self.year}.csv'
        self.df = self.load_expenses()

    def load_expenses(self):
        """Load expenses from the CSV file into a pandas DataFrame."""
        if os.path.exists(self.filename):
            return pd.read_csv(self.filename, sep=';')
        else:
            return pd.DataFrame(columns=['Month', 'Amount', 'Shop', 'Date', 'Category', 'Description'])

    def save_expenses(self):
        """Save the current state of the expenses to the CSV file."""
        self.df.to_csv(self.filename, sep=';', index=False)

    def add_expense(self, month, amount, shop, category, description, date=None):
        """Add a new expense to the tracker."""
        if date is None:
            date = datetime.date.today()

        new_expense = {
            'Month': month,
            'Amount': amount,
            'Shop': shop,
            'Date': date,
            'Category': category,
            'Description': description
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_expense])], ignore_index=True)

        self.save_expenses()

    def delete_expense(self, amount):
        """Delete an expense matching the given amount."""
        self.df = self.df[self.df['Amount'] != amount]
        self.save_expenses()

    def list_expenses(self):
        """List all expenses for the current year."""
        return self.df

    def filter_by_month(self, month):
        """Filter expenses for a specific month."""
        return self.df[self.df['Month'] == month]
