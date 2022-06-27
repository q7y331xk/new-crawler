import datetime

def check_args(start_date, end_date, table_name):
    valid_date = check_date(start_date, end_date)
    valid_table = check_table(table_name)
    return True

def check_date(start_date, end_date):
    date_diff = end_date - start_date
    if date_diff < datetime.timedelta(days=0):
        raise Exception("start_date is later than end_date")
    return True

def check_table(table_name):
    # check db table
    return True