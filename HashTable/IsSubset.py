# A subset: is a collection of elements that belong to another set, called the "superset".
#Find whether an array is a subset of another array using Hashing
def isSubset(arr1, m, arr2, n):
    Hashset = set()
    for j in range(0, m):
        Hashset.add(arr1[j])

    for i in range(0, n):
        if arr2[i] in Hashset:
            continue
        else:
            return False
    return True
    
if __name__ == '__main__':
    arr1 = [12,4,8,1,3,2,5]
    arr2 = [4,3,12,1,9]
    m = len(arr1)
    n = len(arr2)

    if (isSubset(arr1, m, arr2, n)):
        print("arr2[] is a subset of arr1[]")
    else:
        print("arr2[] is not a subset of arr1[]")

isSubset(arr1,m,arr2,n)