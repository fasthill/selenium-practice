
import re
from datetime import datetime

date = ['May 19, 1937']

month_re = r'(January|February|March|April|May|June|July|August|September|October|November|December)'
date_re = r'\s(\d{1,2})\,'
year_re = r'\s(\d{4})'

datetime_re = rf'{month_re}{date_re}{year_re}'

def month_to_num(month):
    montonum = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
              'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    return montonum[month]

def change_date_to_num(i_date):
    mon = month_to_num(i_date.group(1))
    return mon+'-'+i_date.group(2)+'-'+i_date.group(3)

def datetime_conversion(date):
    if type(date) == list:
        for idate in date:
            i_date = re.search(datetime_re, idate)
    else:
        i_date = re.search(datetime_re, date)

    return datetime.strptime(change_date_to_num(i_date), '%m-%d-%Y')


dd = datetime_conversion(date)

print('datetime_c')
