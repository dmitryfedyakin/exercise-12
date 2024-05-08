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

        return f"|{self.passenger_name.ljust(16)}|" \
               f"{self._from.ljust(4)}|" \
               f"{self.to.ljust(3)}|" \
               f"{self.date_time.ljust(16)}|" \
               f"{self.flight.ljust(20)}|" \
               f"{self.seat.ljust(4)}|" \
               f"{self._class.ljust(3)}|" \
               f"{self.gate.ljust(4)}|"
    
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
