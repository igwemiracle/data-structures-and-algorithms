# each number represents the maximum you can advance to in the array---> A1 = [3, 3, 1, 0, 2, 0, 1]
# to keep track of the last index 
# so we dont want to read pass the index and also keep
# track if we actually hit the last index of the array
# ( i = 0), keeps track of the index we are processing, thereby iterating through the element
# Note: while loop terminates when 1 > furthest_reached 
# furthest_reached >= last_idx : This implies that the end is reachable.
# In each iteration of the while loop, we update furthest_reached to the maximum of furthest_reached and (A[i] + i). i increments by 1 in the next line.

def array_advance(A):
        furthest_reached = 0
        last_idx = len(A) - 1 
        i = 0
        while i <= furthest_reached and furthest_reached < last_idx:
                furthest_reached = max(furthest_reached, A[i] + i)
                i += 1
        return furthest_reached >= last_idx

A1 = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A1))

A2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A2))

print("\n")

       # <---------------- Arbitrary Precision Increment --------------->
#1)⚽️---We add 1 to the last number in list A

#2)⚽️---To handle the carry as a result of this addition, therefore, using a for loop 
# we iterate the list from the last index to the index 1 through the reversed function

#3)⚽️---Next on line 39, we check if we get 10 as a result of adding 1. If not,
# then the carry from the addition is 0, and we break the loop 

#4)⚽️---However, if A[i] is 10 then we put 0 in its place and add 1 to the preceding index 
# this is repeated for every position in the list from the last index to index 1

#5)⚽️---Now to handle the edge case where the value at the first index is 10. 
# we set A[0] to 1 and append 0. 
A1 = [1, 4, 9]
A2 = [9, 9, 9]

def plus_one(A):
	A[-1] += 1
	for each_item in reversed(range(1, len(A))):  # iterating over A
		if A[each_item] != 10:
			break
		A[each_item] = 0
		A[each_item-1] += 1
	if A[0] == 10:
		A[0] = 1
		A.append(0)
	return A

print(plus_one(A1))
print(plus_one(A2))

print("\n")


#          <---------------- TWO-SUM PROBLEM --------------->
# Given a sorted array of integers, return the two numbers such that_
# they add up to a specific target. You may assume that each input_
# would have exactly one solution, and you may not use the same element twice.

      # <---------- solution 1----------->
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(A, target):
	for i in range(len(A)-1): # iterates over all the elements in A
		for j in range(i+1, len(A)): # iterates from the next index of i_items
			# for example: ("-2", 1), (-2, 2)... and ("1", 2), (1, 4), (1, 7)... and ("2", 4), (2, 7), (2, 11)...
			if A[i] + A[j] == target:
				print(A[i], A[j])
				return True
	return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_brute_force(A,target))
target = 20
print(two_sum_brute_force(A,target))

print("\n")


     # <---------- solution 2----------->
# Time Complexity: O(n)
# Space Complexity: O(n)
# This is a slightly better approach Time-wise, but worse from a space standpoint
# In this approach we add each element of the array as we process it one by one 
# and we can add it to our hash-table ("ht"), and test whether or not the target minus the element
# is present in the hash table. And if it is, we know that we've found the element we're on 
# and also the element we've encountered before, such that if we add them together, 
# they will sum to the target value
def two_sum_hash_table(A, target):
	A = [-2, 1, 2, 4, 7, 11]
	ht = dict()
	# ht = dict( 15, 12, 11, 9,...2 )
	for i in range(len(A)): 
		if A[i] in ht:
			print(ht[A[i]], A[i]) # Using the formular: ht[target - curElement]
			#****🟥 is -2 in "ht" --> None, bcuz the "ht" is empty for now.
			# therefore, ht[13-(-2)] =  15
			# therefore, ht[15] = -2

			#****🟥 is 1 in "ht" --> None
			# therefore, ht[13-1] = 12
			# therefore, ht[12] = 1
 
			#****🟥 is 2 in "ht" --> None
			# therefore, ht[13-2] = 11
			#therefore, ht[11] = 2

			#****🟥 is 4 in "ht" --> None
			# therefore, ht[13-4] = 9
			# therefore, ht[9] = 4   ...

			
			#****🟥 is 11 in "ht" equals YES!!!, since through the previous cal. we had 11 in the "ht"
			# therefore, ht[13-11] = 2
			# therefore, ht[2] = 11  
			# therefore, print(ht[2], [11]) which also means print(ht[A], [A])
			return True 
		else:
			ht[target - A[i]] = A[i]
	return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_hash_table(A,target))
print("\n")


    # <---------- solution 3----------->
# Time Complexity: O(n)
# Space Complexity: O(1)
# This is a slightly better approach Time-wise, but worse from a space standpoint
def two_sum(A, target):
	i = 0 # starts at the head of the array
	j = len(A) - 1 # starts at the tail of the array

	while i < j: # as long as "i" is less than "j", we iterate along
		if A[i] + A[j] == target:
			print(A[i], A[j])
			return True
		elif A[i] + A[j] < target:
			i += 1 # so that A[i] will be a greater value in the next iteration 
			       # and will produce a greater sum than the current sum. 
				   # for example: -2+11 = 9, this is lesser than the target so we increment
				   # 🟥  1+11 = 12, lesser than the target so we increment or iterate along
				   # 🟥  2+11= 13, we have gotten both values of i and j that sum up to 13

		else: # if A[1] + A[j] > target
			j -= 1 # to achieve a lesser sum by moving to an index with a smaller value.
	return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum(A,target))
print("\n")

# <---------------- Optimal task assignment --------------->
# each worker must be assigned two task each

A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
	print((A[i], A[~i]))
print("\n")

# <---------------- Intersection of Two Sorted Arrays --------------->
# Given two sorted arrays, A and B, determine their intersection.
# What elements are common to A and B?
#                   <--------- SOLUTION 1 --------->

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(set(A).intersection(B))
print("\n")

#                   <--------- SOLUTION 2 --------->

def intersect_sorted_array(A, B):
	i = 0
	j = 0
	intersection = []
	while i < len(A) and j < len(B):
		if A[i] == B[j] and A[i] != A[i-1]: 
			# Using A[i] != A[i-1], we check 
			# for duplicates(if the current element != the previous we've encountered)
			# then we know that the current element is the first occurence in the array
			intersection.append(A[i])
			i += 1
			j += 1
		elif A[i] < B[j]:
			i += 1
		else:
			j += 1
	return intersection

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersect_sorted_array(A, B))
print("\n")


# <---------------- EXERCISE: BUY and Sell stocks --------------->
# MY WORK:::😎
def buy_and_sell_stock_once(prices):
    for b in range(len(A)):
        for s in range(b+1, len(A)):
            if A[s] - A[b] == prices:
                print(A[s], A[b])
                return True
    return False

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250 ]
print(buy_and_sell_stock_once(30))
print("\n")


#                   <--------- SOLUTION 1: Buy and Sell Stocks  --------->
# Time Complexity: O(n^2) --> n = size of the array
# Space Complexity: O(1)
def buy_and_sell_stock_once(prices):
    max_profit = 0
    for b in range(len(A)-1):
        for s in range(b+1, len(A)):
            if A[s] - A[b] > max_profit:
                max_profit = A[s] - A[b]
    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_once(A))
print("\n")

#                   <--------- SOLUTION 2: Buy and Sell Stocks  --------->
# Time Complexity: O(n)
# Space Complexity: O(n)

# This is done by Tracking the MINIMUM price:
# for each index, we calculate the most profit we can make by selling at that time. 
#       0     5    0    20   0   10    👍30   0    25   20
#  A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# ❌ Starting at the first index(310) of the array, we are going to check:
# what is the smallest number we've seen so far?... ANS = 310,  
# therefore we subtract 310 - 310 = 0 (buying - selling).
# ❌ Next to the other index(315) and keeping in mind that the smallest number we've 
# seen so far is 310, we subtract 315 from 310 == 5 (buy - sell).
# ❌ Starting at the other index(275) that we are on, we check for the Minimum == 275
# so we subtract (275 - 275) == 0.
# ❌ Next to the other index(295) and keeping in mind the Minimum 
# we've seen so far is 275, we subtract 295 from 275 == 20
# ❌ Starting at the other index(260) that we are on, we check for the Minimum == 260
# so we subtract (260 - 260) == 0.
# ❌ Next to the other index(270) and keeping in mind the Minimum 
# we've seen so far is 260, we subtract 270 from 260 == 10
# ❌ Starting at the other index(290) that we are on, we check for the Minimum == 260
# so we subtract (290 - 260) == 30.
# ❌ Next to the other index(230), we check for the Minimum == 230 
# so we subtract (230 - 230) == 0.
# ❌ Starting at the other index(255) that we are on, we check for the Minimum == 230
# so we subtract (255 - 230) == 25.
# ❌ Next to the other index(250) and keeping in mind the Minimum we've seen
# so far is 230, we subtract 250 from 230 == 20. 
#      THEREFORE  ❌ ❌ ❌ We keep track of our Maximum Profit, which is "30".
 
A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
  max_profit = 0.0
  min_price = float('inf')
  for price in prices:
    min_price = min(min_price, price)
    compare_profit = price - min_price
    max_profit = max(max_profit, compare_profit)
  return max_profit

print(buy_and_sell_once(A))



