"""
SofDes F2013
HW 9
Josh Langowitz
Double Day
"""

import datetime

def main():
    print dayOfWeek()
    age= ageOf(datetime.datetime(1993,9,23,8,57))
    print 'Age: %s\nTime to next Birthday: %s Days, %s Hours, \
%s Minutes, and %s Seconds'%age
    print nDay(datetime.date(2003,10,11),datetime.date(2006,12,26),2)

def nDay(b1,b2,n=2):
    if b1>b2:
        b1,b2=b2,b1
    return b2+(b2-b1)/(n-1)

def ageOf(birthday):
    now=getDate()
    happened=now>birthday.replace(year=now.year)
    age=now.year-birthday.year+ happened
    thisBirthday=birthday.replace(year=birthday.year+age)
    delta=thisBirthday-now
    print delta
    minutes,seconds=divmod(delta.seconds,60)
    hours,minutes=divmod(minutes,60)
    return (age,delta.days,hours,minutes,seconds)

def dayOfWeek():
    return getDay(getDate())

def getDay(date):
    days={0:'Monday',
        1:'Tuesday',
        2:'Wednesday',
        3:'Thursday',
        4:'Friday',
        5:'Saturday',
        6:'Sunday'}
    return days[date.weekday()]

def getDate():
    return datetime.datetime.now()

if __name__ == '__main__':
    main()