from random import sample 

class PermutedListRepeatedElementException(Exception):
    def __init__(self, message: str="Repeated element within the list"):
        super().__init__(message)

class PermutedListSwapIndexException(Exception):
    def __init__(self, message: str="Index out of list range"):
        super().__init__(message)

class PermutedList:
    def __init__(self, l: list[int] = []):
        self._num_elems: int = len(l)
        self._list: list[int] = self.__make_list(l)
        
    def __make_list(self, l: list[int]) -> list[int]:
        res: list[int] = []
        
        for i in l:
            if not i in res:
                res.append(i)
            else:
                raise PermutedListRepeatedElementException
        
        return res
    
    @staticmethod
    def random_list(self, max: int, num_elems: int) -> 'PermutedList':
        """
        Returns a PermutedList containing a list of random elements from 0 to N of a specified size.
        
        Args:
            max (int): highest value that can be generated randomly
            num_elems (int): number of elements in the list

        Returns:
            PermutedList: permuted list of elements created with random values
        """
        return PermutedList(sample(0, max), num_elems)
    
    def list_elems(self) -> list[int]:
        return self._list
        
    def list_pair_elems(self) -> list[(int, int)]:
        """
        Returns a list where each element is a tuple containing the element of 
        the PermutedList at that position and its successor, the last element of
        the PermutedList list has no tuple
        """
        
        elem: int = self._list[0]
        res: list[(int, int)] = []
        
        for i in range(1, self._num_elems):
            res.append((elem, self._list[i]))
            elem = self._list[i]
        
        return res
    
    def swap_elems(self, index: int) -> None:
        """
        Performs the swap of a pair of elements according to an index,
        the index by the first element causes it to be swap with its successor, 
        only the last element is exchanged with its predecessor

        Args:
            index (int): index of the element to be exchanged

        Raises:
            PermutedListSwapIndexException: index out of range
        """
        if index >= 0 and index <= self._num_elems -1:
            
            if index == self._num_elems -1:
                index -= 1
                
            aux: int = self._list[index]
            
            self._list[index] = self._list[index + 1]
            self._list[index + 1] = aux
        else:
            raise PermutedListSwapIndexException()
        
    def __str__(self) -> str:
        return self._list.__str__()
    
if __name__ == "__main__":
    lp: PermutedList = PermutedList([1, 2])
    print(lp)