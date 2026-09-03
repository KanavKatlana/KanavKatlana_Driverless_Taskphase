hash_table = [[], [], [], [], [], [], [], [], [], []]


n = int(input("Enter how many numbers you want to input: "))

for i in range(n):
    num = int(input("Enter number: "))
    index = num % 10
    
    
    hash_table[index].append(num)


print("Hash Table ")
for i in range(10):
    print("Bucket", i, ":", hash_table[i])
