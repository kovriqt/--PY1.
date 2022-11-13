from random import randint
from typing import List
def get_unique_list_numbers(left,right,num) -> List[int]:
    list_numbers=[]
    while len(list_numbers)<=num and num<=len(range(left,right))+1:
        random=randint(left, right)
        if random not in list_numbers :
            list_numbers.append(random)
    return list_numbers
print(get_unique_list_numbers(-10,10,15))
