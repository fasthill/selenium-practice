from module_datetime_conversion import date_conversion
import datetime

def test_date_conversion_normal():
    assert date_conversion(['May 19, 1937']) == datetime.datetime.strptime('1937-5-19', '%Y-%m-%d')

def test_date_conversion_without_day():
    assert date_conversion(['May 1937 ( Center Theatre )', 'May 1937 (United States)']) == datetime.datetime.strptime('1937-5-1', '%Y-%m-%d')

def test_date_conversion_different_location():
    assert date_conversion(['13 December 1963']) == datetime.datetime.strptime('1963-12-13', '%Y-%m-%d')

def test_date_conversion_year_only():
    assert date_conversion(['1963']) == datetime.datetime.strptime('1963-1-1', '%Y-%m-%d')

def test_date_conversion_space_character():
    assert date_conversion(['February\xa04,\xa01966']) == datetime.datetime.strptime('1966-2-4', '%Y-%m-%d')
