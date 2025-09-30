from typing import List

def row_sums(mat: List[List[float|int]]) -> List[float]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        return 'ValueError'
    
    return [sum(row) for row in mat]

print(row_sums([[1, 2, 3], [4, 5, 6]])) 
print(row_sums([[-1, 1], [10, -10]]))     
print(row_sums([[0, 0], [0, 0]]))                               
print(row_sums([[1, 2], [3]]))          



