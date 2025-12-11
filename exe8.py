# bubble sort implementation
 
numbers = [2, 5, 6, 1, 3, 8, 9, 10] 

temp = 0

for num in range(0, len(numbers)):              # [2,]
    for j in range(num + 1, len(numbers)):      # [5,]
        if numbers[num] > numbers[j]:           # Compare current number with the next number (2>5)
            temp = numbers[num]                 # temp = 2
            numbers[num] = numbers[j]
            numbers[j] = temp
    
print("Sorted list is:", numbers)