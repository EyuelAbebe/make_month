from math import floor

def leap_year(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

class make_month(object):
    def __init__(self, year, month):
        self.days = { 1: "Monday",
                      2: "Tuesday",
                      3: "Wednesday",
                      4: "Thursday",
                      5: "Friday",
                      6: "Saturday",
                      0: "Sunday"}

        self.month = ((month + 9)%12) + 1
        self.c = int(year/100)
        self.y = int(year%100)  
        if month in [1, 2]:
            self.y = self.y - 1 
    
    def day(self, day):

        date = int(day + floor(2.6*self.month - 0.2) + self.y + floor(self.y/4) + floor(self.c/4) - 2*self.c) % 7
        
        return self.days[date]


if __name__ == '__main__':
    import datetime, random, sys

    for j in range(100):
        year = random.randint(1901, 2014)
        month = random.choice([i+1 for i in range(12)])
        date = random.choice([i+1 for i in range(31)])

        if month == 2 and leap_year(year):
            date = date % 29
        elif month == 2:
            date = date % 28

        day = datetime.date(year, month, date).strftime("%A").lower()
        m_m_day = make_month(year, month).day(date).lower()

        print day, m_m_day, year, month, date
        if day != m_m_day:
            print "Test Fails."
            sys.exit()
    print "Test Passes."

