
hash_table = [[], [], [], [], [], [], [], [], [], []]

n = int(input("Enter how many numbers you want to input: "))

for i in range(n):
    num = int(input("Enter number: "))
    
    
    index = num % 10
    sublist = hash_table[index]
    
   
    low = 0
    high = len(sublist) - 1
    insert_pos = len(sublist) 
    
    while low <= high:
        mid = (low + high) // 2
        
        if sublist[mid] >= num:
            insert_pos = mid  
            high = mid - 1
        else:
            low = mid + 1     
            
    sublist.append(0)
    
    
    j = len(sublist) - 1
    while j > insert_pos:
        sublist[j] = sublist[j - 1]
        j = j - 1
        
    
    sublist[insert_pos] = num


print("Sorted Hash Table ")
for i in range(10):
    print("Bucket", i, ":", hash_table[i])
