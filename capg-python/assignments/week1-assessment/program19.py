def second_largest(lst):
    max2 = float('-inf')
    for num in lst:
        if(num < max(lst) and num > max2):
            max2 = num

    return max2

print(second_largest([1,2,3,4,5,6]))