def printPairs(arr, arr_size, sum):

    # Create an empty hash map
    # using an hashmap allows us to store the indices
    hashmap = {}

    for i in range(0, arr_size):
        diff = sum-arr[i]
        if (diff in hashmap):
            print(f"Yes! there is a pair ({diff},{arr[i]})")
            return
        hashmap[arr[i]] = i
    print("No")


A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)
