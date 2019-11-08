def binary_searching(arr, val):
	# from the mid index: if the value demanded is bigger
	# if the value is bigger than the middle element then we check from the left side
	# else check from the right side
	start = 0
	stop = len(arr) - 1

	while start <= stop:
		mid = round((start + stop) / 2)
		print(mid)
		if val == arr[mid]:
			return True
		elif val > arr[mid]:
			start = mid + 1
		else:
			stop = mid - 1
	return False



def main():
	# First we sort the list in ascending order
	array = [11, 7, -3, 86, 32, 16, -19] # -19, -3, 7, 11, 16, 32, 86
	array.sort()

	value = int(input("Search a value: "))

	if binary_searching(array, value):
		print("The value belongs to the list.")
	else:
		print("The value doesn't belong to the list.")

main()
