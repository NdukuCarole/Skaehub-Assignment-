from datetime import datetime, date
from datetime import timedelta


def get_date(days = 3):
    #Format as Year Month Day 
    print((date.today() - timedelta(1)).strftime("%Y-%m-%d"))
    print((date.today() - timedelta()).strftime("%Y-%m-%d"))
    print((date.today() + timedelta(1)).strftime("%Y-%m-%d"))
    
         #Format as Year Month Day Hour Minutes and Seconds 985
    print(datetime.now() - timedelta(days=days))


if __name__ == '__main__':
    get_date()
