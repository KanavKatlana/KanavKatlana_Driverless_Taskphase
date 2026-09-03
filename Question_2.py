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

n = int(input("Enter number of strings: "))
strings = []
for i in range(n):
    strings.append(input("Enter string: "))


sorter = StringSorter()
sorted_list = sorter.selection_sort(strings)
print("Sorted list:", sorted_list)
