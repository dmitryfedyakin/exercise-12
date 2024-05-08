from math import pi

class GeometricObject:
    '''
    Class describes some geometry object.
    '''
    
    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        '''
        Initializes geometry object parametres.

        :param x: X coordinate
        :param y: Y coordinate
        :param color: Object color
        :param filled: Filling of the object
        '''
        
        self.__x = float(x)
        self.__y = float(y)
        self.color = color
        self.filled = filled

    def set_coordinate(self, x, y):
        '''
        Sets geometry object coordinates.

        :param x: X coordinate
        :param y: Y coordinate
        '''

        self.__x = float(x)
        self.__y = float(y)
    
    def set_color(self, color):
        '''
        Sets geometry object color
        
        :param color: Object color
        '''

        self.color = color

    def set_filled(self, filled):
        '''
        Sets filling of the geometry object.

        :param filled: Status of object filling
        '''

        self.filled = filled

    def get_x(self):
        '''
        Returns X coordinate.
        '''

        return self.__x
    
    def get_y(self):
        '''
        Returns Y coordinate.
        '''

        return self.__y
    
    def get_color(self):
        '''
        Returns object color.
        '''

        return self.color
    
    def is_filled(self):
        '''
        Returns object filling
        '''

        return self.filled
    
    def __str__(self):
        '''
        Returns string representation of an object (for users).
        '''

        return f'({self.__x}, {self.__y})\n' \
            f'color: {self.color}\nfilled: {self.filled}'
    
    def __repr__(self):
        '''
        Returns formal string representation of an object (for developers).
        '''

        if self.filled:
            fill_status = ''
        else:
            fill_status = ' no'
        return f'({int(self.__x)}, {int(self.__y)}) ' \
        f'{self.color}{fill_status} filled'


class Circle(GeometricObject):
    '''
    Class describes Circle.
    '''

    def __init__(self, x=0.0, y=0.0, radius=0.0, 
                 color='black', filled=False):
        '''
        Initializes Circle parametres.

        :param x: X coordinate
        :param y: Y coordinate
        :param radius: Circle radius
        :param color: Circle color
        :param filled: Filling of the circle
        '''
        
        super().__init__(x, y, color, filled)

        if radius >= 0:
            self.__radius = float(radius)
        else:
            self.__radius = 0.0

    radius = property()

    @radius.setter
    def radius(self, radius):
        '''
        Sets circle radius.

        :param radius: Circle radius
        '''
        
        if radius >= 0:
            self.__radius = float(radius)
        else:
            self.__radius = 0.0

    @radius.getter
    def radius(self):
        '''
        Returns circle radius.
        '''
        
        return self.__radius

    def get_area(self):
        '''
        Returns circle area.
        '''
        
        return pi * (self.__radius ** 2)

    def get_perimetr(self):
        '''
        Returns circle perimeter.
        '''

        return pi * 2 * self.__radius

    def get_diametr(self):
        '''
        Returns circle diameter.
        '''

        return 2 * self.__radius

    def __str__(self):
        '''
        Returns string representation of an object (for users).
        '''
                
        return f'radius: {self.__radius}\n{super().__str__()}'

    def __repr__(self):
        '''
        Returns formal string representation of an object (for developers).
        '''

        return f'radius: {int(self.__radius)} {super().__repr__()}'

class Rectangle(GeometricObject):
    '''
    Class describes Rectangle.
    '''
    
    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, 
                 color='black', filled=False):
        '''
        Initializes Rectangle parametres.

        :param x: X coordinate
        :param y: Y coordinate
        :param width: Rectangle width
        :param height: Rectangle height
        :param color: Rectangle color
        :param filled: Filling of the rectangle
        '''
        
        
        super().__init__(x, y, color, filled)

        if width >= 0:
            self.width = float(width)
        else:
            self.width = 0.0

        if height >= 0:
            self.height = float(height)
        else:
            self.height = 0.0
    
    def set_width(self, width):
        '''
        Sets rectangle width.

        :param width: Rectangle width
        '''

        if width >= 0:
            self.width = float(width)
        else:
            self.width = 0.0

    def set_height(self, height):
        '''
        Sets rectangle height.

        :param width: Rectangle height
        '''

        if height >= 0:
            self.height = float(height)
        else:
            self.height = 0.0

    def get_width(self):
        '''
        Returns rectangle width.
        '''
        
        return self.width

    def get_height(self):
        '''
        Returns rectangle height.
        '''
     
        return self.height

    def get_area(self):
        '''
        Returns rectangle area.
        '''
     
        return self.width * self.height

    def get_perimetr(self):
        '''
        Returns rectangle perimeter.
        '''
     
        return 2 * (self.width + self.height)

    def __str__(self):
        '''
        Returns string representation of an object (for users).
        '''

        return f'width: {self.width}\n' \
            f'height: {self.height}\n' \
            f'{super().__str__()}'

    def __repr__(self):
        '''
        Returns formal string representation of an object (for developers).
        '''

        return f'width: {int(self.width)} ' \
            f'height: {int(self.height)} ' \
            f'{super().__repr__()}'