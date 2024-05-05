class Date:

    months = {1: "янв", 2: "фев", 3: "мар", 4: "апр",
              5: "май", 6: "июн", 7: "июл", 8: "авг",
              9: "сен", 10: "окт", 11: "ноя", 12: "дек"}
    
    months_days = {1: 31, 2: 28, 3: 31,
                   4: 30, 5: 31, 6: 30,
                   7: 31, 8: 31, 9: 30,
                   10: 31, 11: 30, 12: 31}
        
    def __init__(self, date_str):
        self.__date = None
        self.check_date(date_str)

    def check_date(self, date_str):
        day, month, year = map(int, date_str.split('.'))
        leap = True
        if year % 4 != 0:
            leap = False
        elif year % 100 == 0:
            if year % 400 != 0:
                leap = False
        
        if leap == True:
            Date.months_days[2] = 29
        else:
            Date.months_days[2] = 28

        if 1 <= month <= 12 and day <= Date.months_days[month]:
            self.__date = (day, month, year)

        else:
            print("ошибка")

    date = property()

    @date.setter
    def date(self, date_str):
        self.check_date(date_str)

    @date.getter
    def date(self):
        if self.__date:
            day, month, year = self.__date
            return f"{day} {Date.months[month]} {year} г."


    def to_timestamp(self):
        if self.__date is not None:

            day, month, year = self.__date

            begin_y = 1970
            days_years = 0
            while begin_y != year:
                leap = True
                if begin_y % 4 != 0:
                    leap = False
                elif begin_y % 100 == 0:
                    if begin_y % 400 != 0:
                        leap = False

                if leap:
                    days_in_year = 366
                else:
                    days_in_year = 365

                days_years += days_in_year
                begin_y += 1
            
            begin_y_m = 1
            days_months = 0

            leap = True
            if year % 4 != 0:
                leap = False
            elif year % 100 == 0:
                if year % 400 != 0:
                    leap = False
            if leap:
                Date.months_days[2] = 29 
            else:
                Date.months_days[2] = 28

            while begin_y_m != month:

                days_in_month = Date.months_days[begin_y_m]
                days_months += days_in_month
                begin_y_m += 1

            days = days_years + days_months + day
            seconds = (days - 1) * 86400

            return seconds
            

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.__date == other.__date
        return False

    def __ne__(self, other):
        if isinstance(other, Date):
            return not self.__eq__(other)
        return False

    def __lt__(self, other):
        day_1, month_1, year_1 = self.__date
        day_2, month_2, year_2 = other.__date

        if year_1 < year_2:
            if month_1 < month_2:
                if day_1 < day_2:
                    return True
                
        return False

    def __le__(self, other):
        day_1, month_1, year_1 = self.__date
        day_2, month_2, year_2 = other.__date
        
        if year_1 < year_2:
            return True
        elif year_1 == year_2:
            if month_1 < month_2:
                return True
            elif month_1 == month_2:
                if day_1 <= day_2:
                    return True
                
        return False
        
    def __gt__(self, other): 
        day_1, month_1, year_1 = self.__date
        day_2, month_2, year_2 = other.__date
        
        if year_1 > year_2:
            if month_1 > month_2:
                if day_1 > day_2:
                    return True
                
        return False

    def __ge__(self, other):
        day_1, month_1, year_1 = self.__date
        day_2, month_2, year_2 = other.__date
        
        if year_1 > year_2:
            return True
        elif year_1 == year_2:
            if month_1 > month_2:
                return True
            elif month_1 == month_2:
                if day_1 >= day_2:
                    return True
                
        return False  
    
    def __str__(self):
        return self.__date if self.__date != None else 'None'

