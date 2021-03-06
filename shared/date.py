import datetime

def getdatesBetween(start_date, end_date):
  dates = getDatesArray(start_date, end_date)

def parseDateStringToDate(date_string):
  parsed_string =date_string.split('-')
  [year, month, day] = list(map(lambda word: int(word), parsed_string))
  date = datetime.datetime(year,month,day)
  return date

def getDatesArray(start_date, end_date):
  print(end_date-start_date)
  dates = []
  while(start_date <= end_date):
    dates.append(start_date.strftime("%Y-%m-%d"))
    start_date = start_date + datetime.timedelta(days=1)
  return dates