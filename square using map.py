def squ_num(n):
    return n*n
nums=[4,5,2,9,10]
print("original list :",nums)
result = map(squ_num,nums)
print("square of elements in the list")
print(list(result))