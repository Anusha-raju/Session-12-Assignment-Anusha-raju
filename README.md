# Session-12-Assignment



The notebook link :

https://deepnote.com/project/Starter-Project-3hCGzG0RTV2p2HFU7WcdPw/%2Fpolygon_notebook.ipynb



### Assignment :

The starting point for this project is the `Polygon` class and the `Polygons` sequence type created in the previous assignment.

##### Goal 1

Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").

##### Goal 2

Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.



***Note***:

- Goal 1 was already achieved in previous assignment.

- Goal 2 most of the code remains same except the following changes.





***Goal 2***

Only the `__next__` method had to be altered

```
        def __next__(self):
            if self._index >= self._highest_no_of_edges-2:
                raise StopIteration
            else:
                item = Polygon(self._index+3, self._circumradius)
                self._index += 1
                return item

```



The maximum efficiency ,

```
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

```

