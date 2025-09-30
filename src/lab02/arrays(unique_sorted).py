from typing import List

def unique_sorted(nums: List[float | int]) -> List[float | int]:
    unique: List[float | int] = []
    
    for x in nums:
        if x not in unique:
            unique.append(x)
    
    unique.sort()
    
    return unique

print(unique_sorted([3, 1, 2, 1, 3]))       
print(unique_sorted([]))                    
print(unique_sorted([-1, -1, 0, 2, 2]))     
print(unique_sorted([1.0, 1, 2.5, 2.5, 0])) 
