class Date:
    '''
    This class represents a date and provides methods for working with it.

    Attributes:
        months (dict): A dictionary mapping month numbers to their names in Russian.
        months_days (dict): A dictionary mapping month numbers to the number of days in them
    '''

    months = {1: "янв", 2: "фев", 3: "мар", 4: "апр",
              5: "май", 6: "июн", 7: "июл", 8: "авг",
              9: "сен", 10: "окт", 11: "ноя", 12: "дек"}
    
    months_days = {1: 31, 2: 28, 3: 31,
                   4: 30, 5: 31, 6: 30,
                   7: 31, 8: 31, 9: 30,
                   10: 31, 11: 30, 12: 31}
        
    def __init__(self, date_str):
        '''
        Initializes a Date object with a date string.
        
        :param date_str: The date in string format.
        '''

        self.__date = None
        self.check_date(date_str)

    def check_date(self, date_str):
        '''
        Checking a date string on possibility of existence.

        :param date_str: The date in string format.
        '''

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
        '''
        Sets the date as a formatted string.

        :param date_str: The date in string format.
        '''

        self.check_date(date_str)

    @date.getter
    def date(self):
        '''
        Gets the date as a formatted string.
        '''

        if self.__date:
            day, month, year = self.__date
            return f"{day} {Date.months[month]} {year} г."


    def to_timestamp(self):
        '''
        Calculates the amount of seconds since 01.01.1970

        :return: amount of seconds
        '''

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
        '''
        Overriding the comparison operator '=='

        :return: result of comparison
        '''

        if isinstance(other, Date):
            return self.__date == other.__date
        return False

    def __ne__(self, other):
        '''
        Overriding the comparison operator '!='

        :return: result of comparison
        '''

        if isinstance(other, Date):
            return not self.__eq__(other)
        return False

    def __lt__(self, other):
        '''
        Overriding the comparison operator '<='

        :return: result of comparison
        '''

        day_1, month_1, year_1 = self.__date
        day_2, month_2, year_2 = other.__date

        if year_1 < year_2:
            if month_1 < month_2:
                if day_1 < day_2:
                    return True
                
        return False

    def __le__(self, other):
        '''
        Overriding the comparison operator '<='

        :return: result of comparison
        '''

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
        '''
        Overriding the comparison operator '>'

        :return: result of comparison
        '''

        day_1, month_1, year_1 = self.__date
        day_2, month_2, year_2 = other.__date
        
        if year_1 > year_2:
            if month_1 > month_2:
                if day_1 > day_2:
                    return True
                
        return False

    def __ge__(self, other):
        '''
        Overriding the comparison operator '>='

        :return: result of comparison
        '''

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
        '''
        Return string representation of an object (for users).
        '''
        
        return self.__date if self.__date != None else 'None'

