from datetime import datetime

def convert_date_format(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

    formatted_date = date.strftime("%d/%m/%Y %I:%M:%S %p")

    return formatted_date
