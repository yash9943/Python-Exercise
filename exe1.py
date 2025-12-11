numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3] 
print('===============================')
print('Given List:', numbers)
print('Menu Options:')
print('----------------------------------')
print('A. Length of the list')
print('B. Display first 3 numbers')
print('C. Display sum of odd numbers')
print('D. Number of duplicate numbers')
print('E. Display list without duplicate numbers')
print('----------------------------------')
print()
user_input = str(input("Choose option: "))


while True:
    if user_input:
        if user_input == 'A' or user_input == 'a':
            print("Length of the list is :", len(numbers))
            break
        elif user_input == 'B' or user_input == 'b':
            print("First 3 numbers are :", numbers[0:3])
            break
        elif user_input == 'C' or user_input == 'c':
            odd_sum = 0
            for num in numbers:
                if num % 2 != 0:
                    odd_sum += num
            print("Sum of odd numbers is :", odd_sum)
            break
        elif user_input == 'D' or user_input == 'd':
            duplicate_num = []
            for i in numbers:
                if numbers.count(i) > 1 and i not in duplicate_num:
                    duplicate_num.append(i)
            print("Number of duplicate numbers is :",len(duplicate_num))
            break
        elif user_input == 'E' or user_input == 'e':
            unique_list = []
            for i in numbers:
                if i not in unique_list:
                    unique_list.append(i)
            print("List without duplicate numbers is :", unique_list)
            break
        else:
            print("Invalid option. Please choose A, B, C, D, or E.")
            break
    else:
        print("No input provided.")
        break