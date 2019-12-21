import time
import math

start = time.time()

f1 = open('names_1.txt')
f2 = open('names_2.txt')
names1 = f1.readlines()
names2 = f2.readlines()

########################## use the in check for each name in the names1.txt.  runtime ~ 2.15 sec############################
# rawnames1 = [n.strip('\n') for n in names1]
# rawnames2 = [n.strip('\n') for n in names2]

# duplicates = []

# for rn1 in rawnames1:
#     if rn1 in rawnames2:
#         duplicates.append(rn1)

# # for d in duplicates:
# #     print(d,'\n')

# print(len(duplicates),' duplicates')


# end = time.time()
# execution = end - start
# print('execution time: ', execution)
########################## use the in check for each name in the names1.txt.  runtime ~ 2.15 sec############################

########################## sorting names w/ binary search on a sorted array (list) #################################################
start = time.time()
rawnames1 = [n.strip('\n') for n in names1]
rawnames2 = [n.strip('\n') for n in names2]

rawnames1.sort()
rawnames2.sort()

def binary_search(val,arr):
    #array has been sorted already.  arr.sort()
    arr.sort()
    # print('array', arr, len(arr))
    if len(arr) <= 2:
        if val in arr:
            return val
        else: return None

    mid = math.floor(len(arr) / 2)

    if val >= arr[mid]:
        # print('arr[mid:]',arr[mid:])
        return binary_search(val,arr[mid:])
    else: #val < arr[mid]
        # print('arr[:mid]', arr[:mid])
        return binary_search(val,arr[:mid])

arr = [2,3,4,1,5,5,6,20,4,5,2,1]


duplicates = []

for n in rawnames1:
    found = binary_search(n,rawnames2)
    if found:
        duplicates.append(found)


end = time.time()

print('duplicate length: ', len(duplicates))
print('execution time: ', end - start)
#####################################binary search on every name : ~ 7 seconds execution time#####