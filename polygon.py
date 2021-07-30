import math

class Polygon:
    """
    This is a class which generates a regular strict convex polygon with desired vertex and circumradius
    """

    def __init__(self,no_of_edges:int,circumradius:float)->None:
        """
        This is a constructor which initialises the number of edges/vertices and circumradius
        """
        if no_of_edges<3:
            raise ValueError("Number of edges/vertices should be equal to or greater than 3(Three)")

        self.count_vertices = no_of_edges
        self.count_edges = no_of_edges
        self.circumradius = circumradius
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None


    def __repr__(self)->str:
        """
        This is a representation function
        """
        return f'Polygon(n={self.count_vertices}, R={self.circumradius})'

    @property
    def interior_angle(self)->float:
        """
        This is a function which calculates the interior angle
        """

        if self._interior_angle == None:
            print("Interior_angle")
            self._interior_angle = (self.count_vertices - 2)*(180/self.count_vertices)
        return self._interior_angle

    @property
    def edge_length(self)->float:
        """
        This is a function which calculates the edge length of the polygon
        """
        if self._edge_length == None:
            print("edge_length")
            self._edge_length = (2*self.circumradius)*math.sin(math.pi/self.count_vertices)
        return self._edge_length


    @property
    def apothem(self)->float:
        """
        This is a function which calculates the apothem of the polygon
        """
        if self._apothem == None:
            print("_apothem")
            self._apothem = self.circumradius*math.cos(math.pi/self.count_vertices)
        return self._apothem


    @property
    def area(self)->float:
        """
        This is a function which calculates the area of the polygon

        """
        if self._area == None:
            print("_area")
            self._area = 0.5*self.count_vertices*self.apothem*self.edge_length
        return self._area

    @property
    def perimeter(self)->float:
        """
        This is a function which calculates the perimeter of the polygon

        """
        if self._perimeter == None:
            print("_perimeter")
            self._perimeter = self.count_vertices*self.edge_length
        return self._perimeter

    def __eq__(self, other:'Polygon class')->bool:
        """
        This is a equal to (==) function which checks for the number of edges and circumradius
        """

        if isinstance(other, Polygon):
            return True if self.count_vertices==other.count_vertices and self.circumradius == other.circumradius else False
        else:
            raise TypeError("This operation can be performed only with two polygon type objects")

    def __gt__(self, other:'Polygon class')->bool:
        """
        This is a greater than function which calculates based on number of edges.
        """
        if isinstance(other, Polygon):
            return True if self.count_vertices > other.count_vertices else False
        else:
            raise TypeError("This operation can be performed only with two polygon type objects")