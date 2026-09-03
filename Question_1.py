n = int(input("Enter the number of strings: "))

strings_list = []
print("Enter n strings:")
for _ in range(n):
    strings_list.append(input())

counts = {}
for string in strings_list:
  
    for char in string:
        
        lower_char = char.lower()
        
        
        if 'a' <= lower_char <= 'z':
            if lower_char in counts:
                counts[lower_char] += 1
            else:
                counts[lower_char] = 1


print(counts)
