def mof(arr, k):
	k -= 30
	arr = sorted(arr)
	lo, hi = 0, len(arr)-1
	max_val = 0
	while lo < hi:
		if arr[lo] + arr[hi] <= k:
			if max_val < arr[lo] + arr[hi]:
				max_val = arr[lo] + arr[hi]
				i, j = lo, hi
			lo += 1
		else:
			hi -= 1
	return (arr[i], arr[j])
