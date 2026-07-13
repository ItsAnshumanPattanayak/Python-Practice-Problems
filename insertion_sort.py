def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
       key = arr[i]
       j = i -1

       while j>= 0 and nums[j] > key:  
            nums[j+1] = nums[j]
            j-= 1

       nums[j+1] = key

    return arr



nums = [14,53,23,9,1,22]
sorted_array = insertion_sort(nums)
print("Sorted Array:" , sorted_array)