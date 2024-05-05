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
        if self.__date:
            day, month, year = self.__date
            return f"{day} {Date.months[month]} {year} г."

class Meeting():
    lst_meeting = []
    NUM = 0

    def __init__(self, id=None, date=None, title=None, employees=None):
        self.id = id
        self.date = date
        self.title = title
        self.employees = employees or []

    def add_person(self, person):
        self.employees.append(person)

    def count(self):
        return len(self.employees)

    @staticmethod
    def count_meeting(date):
        count = 0
        for meeting in Meeting.lst_meeting:
            if Date(meeting.date) == date:
                count += 1
        return count

    @staticmethod
    def total():
        return Meeting.NUM

    def __str__(self):
        result = ''
    
        id_list = []
        for part in self.employees:
            if part['id_meet'] == self.id:
                id_list.append(part['id_pers'])

        for i in id_list:
            for person in User.lst_user:
                login_ind = str(person).find('LOGIN')
                if i == str(person)[3:login_ind].strip():
                    result += str(person) + '\n'

        return f"Рабочая встреча {self.id}\n" \
               f"{Date(self.date)} {self.title}\n" \
               f"{result}" 

class User:
    lst_user = []

    def __init__(self, id=None, nick_name=None, first_name=None,
                 last_name=None, middle_name=None, gender=None):
        
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __str__(self):        
        str_gender = ''

        if self.id != '':
            str_id = f'ID: {self.id} '
        
        if self.nick_name != '':
            str_nick = f'LOGIN: {self.nick_name} '

        if self.first_name != '' and self.last_name != '' \
            and self.middle_name != '':
            str_name = f'NAME: {self.last_name} {self.first_name} '\
                    f'{self.middle_name} '

        elif self.first_name != '' and self.last_name != '' \
            and self.middle_name == '':
            str_name = f'NAME: {self.last_name} {self.first_name} '

        elif self.first_name != '' and self.last_name == '' \
            and self.middle_name != '':
            str_name = f'NAME: {self.first_name} {self.middle_name} '
        
        elif self.first_name == '' and self.last_name != '' \
            and self.middle_name != '':
            str_name = f'NAME: {self.last_name} {self.middle_name} '

        elif self.first_name != '' and self.last_name == '' \
            and self.middle_name == '':
            str_name = f'NAME: {self.first_name} '

        elif self.first_name == '' and self.last_name != '' \
            and self.middle_name == '':
            str_name = f'NAME: {self.last_name} '

        elif self.first_name == '' and self.last_name == '' \
            and self.middle_name != '':
            str_name = f'NAME: {self.middle_name} '


        if self.gender != '':
            str_gender = f'GENDER: {self.gender}'

        return str_id + str_nick + str_name + str_gender
    
    def __repr__(self):
        return self.__str__()

class Load:
    @staticmethod
    def write(filename_1, filename_2, filename_3):

        with open(filename_1, "r", encoding="utf-8") as f_1:
            attributes = f_1.readline().strip().split(";")
            for line in f_1:
                values = line.strip().split(";")
                meet_data = dict(zip(attributes, values))
                meet_data.pop('')
                meeting = Meeting(**meet_data)
                Meeting.lst_meeting.append(meeting)


        with open(filename_2, "r", encoding="utf-8") as f_2:
            attributes = f_2.readline().strip().split(";")
            for line in f_2:
                values = line.strip().split(";")
                user_data = dict(zip(attributes, values))
                user_data.pop('')
                user = User(**user_data)
                User.lst_user.append(user)


        with open(filename_3, "r", encoding="utf-8") as f_3:
            attributes = f_3.readline().strip().split(";")
            for line in f_3:
                values = line.strip().split(";")
                meet_p_data = dict(zip(attributes, values))
                meet_p_data.pop('')
                meeting_id = meet_p_data['id_meet']
                if meeting_id:
                    for meeting in Meeting.lst_meeting:
                        if meeting.id == meeting_id:
                            meeting.add_person(meet_p_data)  
                            break
                    Meeting.NUM += 1
