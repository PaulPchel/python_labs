from typing import List

def transpose(mat: List[List[float|int]]) -> List[List]:
    if not mat:
        return []

    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        return 'ValueError'
    
    return [list(col) for col in zip(*mat)]


print(transpose([[1, 2, 3]]))      
print(transpose([[1], [2], [3]])) 
print(transpose([[1, 2], [3, 4]])) 
print(transpose([]))               
print(transpose([[1, 2], [3]]))

