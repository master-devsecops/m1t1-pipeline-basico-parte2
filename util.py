import datetime


def getyear():
    today = datetime.date.today()
    return today.year


def getmonth():
    today = datetime.date.today()
    return today.month


def getday():
    today = datetime.date.today()
    return today.day


print(getyear())
print(getmonth())
print(getday())
