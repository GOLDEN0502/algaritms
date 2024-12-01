def Quick_Sort(arr):
    if(len(arr) <= 1) :
        return arr
    else :
        pivot = arr[len(arr)// 2]
        left = [ x for x in arr if x < pivot]
        middle = [ x for x in arr if x == pivot]
        right = [ x for x in arr if x > pivot]
        return Quick_Sort(left) + middle + Quick_Sort(right)
arr = [52,14,88,69,72]
Sorted = Quick_Sort(arr)
print(Sorted)
        
