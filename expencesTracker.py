import pandas as pd
import os
import datetime


class ExpencesTracker:
    """
A class to track expenses throughout the year using a CSV file.

Attributes:
    year (str): The year for which expenses are being tracked.
    filename (str): The name of the CSV file where expenses are stored.
    df (pd.DataFrame): A pandas DataFrame containing the expenses data.

Methods:
    load_expenses(): Loads expenses data from a CSV file into a pandas DataFrame.
    save_expenses(): Saves the current expenses data to the CSV file.
    add_expense(month, amount, shop, category, description, date=None): Adds a new expense to the tracker.
    delete_expense(month, amount, shop, date): Deletes an expense matching the given month, amount, shop, and date.
    delete_expence_by_id(id): Deletes an expense by its unique DataFrame index.
    list_expenses(): Lists all expenses for the current year.
    filter_by_month(month): Filters expenses for a specific month.
    amount_total(): Calculates the total amount of expenses for the current year.
"""
     

    def __init__(self, year: str) -> None:
        self.year = year
        self.filename = f"expences_{self.year}.csv"
        self.df = self.load_expenses()

    def load_expenses(self) -> pd.DataFrame:
        """Load expenses from the CSV file into a pandas DataFrame."""
        if os.path.exists(self.filename):
            return pd.read_csv(self.filename, sep=";")
        else:
            return pd.DataFrame(
                columns=["Month", "Amount", "Shop", "Date", "Category", "Description"]
            )

    def save_expenses(self) -> None:
        """Save the current state of the expenses to the CSV file."""
        self.df.to_csv(self.filename, sep=";", index=False)

    def add_expense(
        self,
        month: str,
        amount: float,
        shop: str,
        category: str,
        description: str,
        date: str = None,
    ) -> None:
        """Add a new expense to the tracker."""
        if date is None:
            date = datetime.date.today()

        new_expense = {
            "Month": month,
            "Amount": amount,
            "Shop": shop,
            "Date": date,
            "Category": category,
            "Description": description,
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_expense])])

        self.save_expenses()

    def delete_expense(self, month: str, amount: float, shop: str, date: str) -> None:
        """Delete an expense matching the given month,amount,shop,date."""
        self.df = self.df[
            (self.df["Amount"] != amount)
            | (self.df["Shop"] != shop)
            | (self.df["Month"] != month)
            | (self.df["Date"] != date)
        ]
        self.save_expenses()

    def delete_expence_by_id(self, id: int) -> None:
        """Delete an expense matching the given id."""
        self.df = self.df.drop([id])
        self.save_expenses()

    def list_expenses(self) -> pd.DataFrame:
        """List all expenses for the current year."""
        return self.df

    def filter_by_month(self, month: str) -> pd.DataFrame:
        """Filter expenses for a specific month."""
        return self.df[self.df["Month"] == month]

    def amount_total(self) -> float:
        """Count total amount of expenses for the current year."""
        total = self.df["Amount"].sum()
        return total
