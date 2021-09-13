from datetime import datetime
import re

date = ['May 19, 1937']

month_list = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
month_re = r'(January|February|March|April|May|June|July|August|September|October|November|December)'
date_re = r'\s(\d{1,2})\,'
year_re = r'\s(\d{4})'

datetime_re = rf'{month_re}{date_re}{year_re}'

# delete unnecessary portion with '()' with in Release date expression list
def clean_date(date):
    return date.split("(")[0].strip()

def relocate_date_format(date):  # June 1963, 11 June 1964, => June 1, 1963, June 11, 1964
    date = date.replace('\xa0', ' ')
    date_s = date.split(' ')
    if len(date_s) == 1:
        m_date = 'January' + ' 1, ' + date_s[0]
        return m_date
    if len(date_s) == 2 :
        m_date = date_s[0] + ' 1, ' + date_s[1]
        return m_date
    if len(date_s) == 1: print(" dddd ", date_s)
    if date_s[1] in month_list:
        m_date = date_s[1] + ' ' + date_s[0]+', ' + date_s[2]
        return m_date
    else:
        return date

def date_conversion(date):
    if isinstance(date, list):
        date = date[0]
    if date == 'N/A':
        return None
    c_date = clean_date(date)
    m_date = relocate_date_format(c_date)
    return datetime_conversion(m_date)

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


if __name__ == '__main__':
    dd = datetime_conversion(date)
    print('datetime_c')
