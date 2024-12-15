import argparse
from datetime import datetime

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def validate_month(month: str) -> bool:
    global MONTHS

    if month.capitalize() in MONTHS:
        return True


def validate_year(year: str) -> bool:
    if year.startswith("20") and len(year) == 4 and year.isdigit():
        year_int = int(year)
        if 2000 <= year_int <= 2025:
            return True
    return False


def validate_description(description: str) -> bool:
    if description is None:
        return True
    if len(description.split()) <= 5:
        return True
    return False


def validate_date(date_string: str) -> bool:
    print(f"Validating date: {date_string}")
    try:

        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
