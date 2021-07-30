from polygon import Polygon as Polygon

class Polygon_sequence:
    """
    This is a polygon sequence class used to develop a custom sequence
    """
    def __init__(self,highest_no_of_edges:int,circumradius:float)->None:
        """
        This is a constructor which initialises the highest number of edges/vertices and circumradius
        """
        if highest_no_of_edges<3:
            raise ValueError("Number of edges/vertices should be equal to or greater than 3(Three)")

        self.highest_no_of_edges = highest_no_of_edges
        self.circumradius = circumradius
        #self.sequence = [Polygon(n, self.circumradius) for n in range(3,self.highest_no_of_edges+1)]
        #self.ratios = [p.area/p.perimeter for p in self.sequence]


    def __repr__(self)->str:
        """
        This is a representation function
        """
        return f'This is a polygon sequence of {self.highest_no_of_edges-2} elements with {self.highest_no_of_edges} as highest edge with common circumradius: {self.circumradius}'


    def __len__(self)->int:
        """
        This is a length function
        """
        return self.highest_no_of_edges - 2

    def __iter__(self):
        return self.PolygonIterator(self,self.circumradius,self.highest_no_of_edges)

    class PolygonIterator:
        def __init__(self,polygon_obj,r,n):
            self.polygon_obj = polygon_obj
            self._index = 0
            self._circumradius = r
            self._highest_no_of_edges = n

        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= self._highest_no_of_edges-2:
                raise StopIteration
            else:
                item = Polygon(self._index+3, self._circumradius)
                self._index += 1
                return item


    def _ratios(self,n):
        polygon_obj = Polygon(n,self.circumradius)
        return polygon_obj.area/polygon_obj.perimeter



    @property
    def max_efficiency(self)->str:
        """
        This function calculates the maximum_efficieny:highest area/perimeter ratio

        """
        maximum_efficieny = max(self._ratios(n) for n in range(3,self.highest_no_of_edges))
        return f"maximum_efficieny is {maximum_efficieny}"

