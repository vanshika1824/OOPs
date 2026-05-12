#find the largest subarray with Sum k
#array[1,2,3,-2,5]    k=5

lst = eval(input())
k= int(input())

sum = 0
max = 0
dict = {}

for i in range(len(lst)):
    sum += lst[i]
    if dict.get(sum-k) != None:
        l = i - dict.get(sum-k)
        if max<l:
            max = l
    
    dict[sum] = i
print(max)
