# in a sorted list:
#Compare x with the middle element.
#If x matches with the middle element, we return the mid index.
#Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
#Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

def binary_search2(vetor, item):
	found = False
	last = len(vetor) -1
	first = 0
	while not found and first <= last:
		mid = (first + last) // 2
		if vetor[mid] == item:
			found = True
		elif item > vetor[mid]:
			first = mid + 1
		elif item < vetor[mid]:
			last = mid - 1
	return found, mid            
			


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

found, index = binary_search2(arr, x)

if found:
	print(index)

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
