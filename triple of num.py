def squ_num(n):
    return n * 3
nums=[1,2,3,4,5,6,7]
print("original list :",nums)
result = map(squ_num,nums)
print("triple of elements in the list")
print(list(result))