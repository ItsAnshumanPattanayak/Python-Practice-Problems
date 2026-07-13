def selection_sort(arr):
  n =len(arr)

  for i in range(0,n):
    min_index = i 
    for j in range (i+1 , n):
      if arr[j] < arr[min_index] :

        min_index = j
    arr[i] , arr [min_index] = arr[min_index] , arr[i]

  return arr
  
nums = [14,53,23,9,1,22]
sorted_array = selection_sort(nums)
print("Sorted Array:" , sorted_array)