import argparse

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def validate_month(month:str)-> bool:
    global MONTHS

    if month.capitalize() in MONTHS:
        return True
    
def validate_year(year:str)-> bool:
    if year.startswith("20") and len(year) == 4 and year.isdigit():
        year_int = int(year)
        if 2000 <= year_int <= 2025:
            return True
    return False
    
def validate_description(description:str)->bool:
    if len(description.split()) <= 5:
        return True
    return False

    