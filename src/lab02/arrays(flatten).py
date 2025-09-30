from typing import List

def flatten(mat: List[list | tuple]) -> List:
    result: List = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            return ('TypeError')
        for elem in row:
            result.append(elem)
    return result


print(flatten([[1, 2], [3, 4]]))         
print(flatten(([1, 2], (3, 4, 5))))      
print(flatten([[1], [], [2, 3]]))        
print(flatten([[1, 2], 'ab']))           
