class AirTicket:
    '''
    Represents an air ticket with passenger and flight information.
    '''

    def __init__(self, passenger_name, _from, 
                 to, date_time, flight, seat, 
                 _class, gate):
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate
        '''
        Initializes an AirTicket object with the provided details.

        :param passenger_name: The name of the passenger.
        :param _from: The departure airport code.
        :param to: The arrival airport code.
        :param date_time: The date and time of the flight.
        :param flight: The flight number.
        :param seat: The assigned seat number.
        :param _class: The travel class.
        :param gate: The departure gate number.
        '''

    def __str__(self):
        '''
        Return string representation of an object (for users).
        '''
        
        name_len = len(self.passenger_name)
        from_len = len(self._from)
        to_len = len(self.to)
        date_time_len = len(self.date_time)
        flight_len = len(self.flight)
        seat_len = len(self.seat)
        class_len = len(self._class)
        gate_len = len(self.gate)

        return f"|{self.passenger_name}{(16 - name_len) * ' '}|" \
               f"{self._from}{(4 - from_len) * ' '}|" \
               f"{self.to}{(3 - to_len) * ' '}|" \
               f"{self.date_time}{(16 - date_time_len) * ' '}|" \
               f"{self.flight}{(20 - flight_len) * ' '}|" \
               f"{self.seat}{(4 - seat_len) * ' '}|" \
               f"{self._class}{(3 - class_len) * ' '}|" \
               f"{self.gate}{(4 - gate_len) * ' '}|"
    
class Load:
    '''
    Provides a method to load air ticket data from file.

    Attributes:
        data (list): A list considering information about ticket
    '''
    
    data = []

    def write(filename):
        '''
        Reads air ticket data from file and stores it in the data list.

        :param filename: Name of the file.
        '''
        
        with open(filename, "r", encoding="utf-8") as f:
            attributes = f.readline().strip().split(";")
            for line in f:
                values = line.split(";")
                ticket_data = dict(zip(attributes, values))
                ticket_data.pop('')
                ticket = AirTicket(**ticket_data)
                Load.data.append(ticket)
