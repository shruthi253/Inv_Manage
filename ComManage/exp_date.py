from datetime import datetime
from datetime import date

def __datetime(date_str):
    return datetime.strptime(date_str, '%m/%d/%y')

def date_avb(item_expiry):
    a =__datetime(item_expiry.get())
    b = datetime.today().strftime('%Y-%m-%d %H:%M:%S')  #string format
    b_dt = datetime.strptime(b, '%Y-%m-%d %H:%M:%S') #back to date format
    diff = (a-b_dt).days #to get days
    return diff

