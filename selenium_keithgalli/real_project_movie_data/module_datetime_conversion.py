from datetime import datetime
import re

month_list = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
month_re = r'(January|February|March|April|May|June|July|August|September|October|November|December)'
date_re = r'\s(\d{1,2})\,'
date_re2 = r'\d{1,2}\s'
year_re = r'\s(\d{4})'

date_re_1 = rf'{month_re}{date_re}{year_re}'
date_re_2 = rf'{date_re2}{month_re}{year_re}'
date_re_3 = rf'{month_re}{year_re}'
date_re_4 = r'\d{4}'
datetime_re = [date_re_1, date_re_2, date_re_3, date_re_4]

def arange_date_string(date):  # data
    for d_re in datetime_re:
        try:
            i_date = re.search(d_re, date).group()
            return i_date
        except:
            pass
    return None
    
    
# delete unnecessary portion with '()' with in Release date expression list
def clean_date(date):
    c_date = date.split("(")[0].strip()
    return c_date.replace('\xa0', ' ')


def date_conversion(date):
    if isinstance(date, list):
        date = date[0]
    if date == 'N/A':
        return None
    c_date = clean_date(date)
    return datetime_conversion(c_date)


def month_to_num(month):
    montonum = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
              'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    return montonum[month]


def change_date_to_num(i_date):
    mon = month_to_num(i_date.group(1))
    return mon+'-'+i_date.group(2)+'-'+i_date.group(3)


def datetime_conversion(date):
    i_date = arange_date_string(date)

    fmts = ['%B %d, %Y', '%d %B %Y', '%B %Y', '%Y']
    for fmt in fmts:
        try:
            return datetime.strptime(i_date, fmt)  # for this, no need to change to num. use %B
        except:
            pass

    return None


if __name__ == '__main__':
    date = ['May 19, 1937']
    dd = date_conversion(date)
    print('date ', date, ': datetime ', dd)
