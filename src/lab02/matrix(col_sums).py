from typing import List

def col_sums(mat:List[List[float|int]]) -> List[float]:
    if not mat:
        return []
    
    row_len = len(mat[0])
    if any(len(row) != row_len for row in mat):
        return 'ValueError'
    
    return [sum(row[i] for row in mat) for i in range(row_len)]


print(col_sums([[1, 2, 3], [4, 5, 6]]))   
print(col_sums([[-1, 1], [10, -10]]))     
print(col_sums([[0, 0], [0, 0]]))        
print(col_sums([[1, 2], [3]]))            
