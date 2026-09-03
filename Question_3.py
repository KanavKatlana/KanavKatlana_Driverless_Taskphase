class StringSorter:
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
          
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
        return arr


class StringSearcher:
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == target:
                return mid  
            elif target < arr[mid]:
                high = mid - 1  
            else:
                low = mid + 1   
                
        return -1  


n = int(input("Enter number of strings: "))
user_strings = []
for i in range(n):
    user_strings.append(input("Enter string: "))

sorter = StringSorter()
sorted_list = sorter.selection_sort(user_strings)
print("\nSorted list:", sorted_list)


target_string = input("\nEnter the string to search for: ")


searcher = StringSearcher()
result_index = searcher.binary_search(sorted_list, target_string)

if result_index != -1:
    print("Found at index:", result_index)
else:
    print("Not found in the list.")
