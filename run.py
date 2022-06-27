from shared.date import parseDateStringToDate
from check_args.check_args import check_args

try:
    start_at="2022-01-01"
    end_at="2022-01-10"
    table_name="table_name"

    start_date=parseDateStringToDate(start_at)
    end_date=parseDateStringToDate(end_at)
    check_args(start_date, end_date, table_name)

except Exception as err_msg:
    print("err:", err_msg)