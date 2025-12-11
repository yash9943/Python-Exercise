names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 
'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White'] 


print("1")
print(" Names : ", end="")
for name in names:
    print(f" '{name}'", end=" ")

print("")

print("2")
length_of_name = []
for name in names:
    length_of_name.append(len(name))
print(' Names Lengths : ', length_of_name)



print("3")
print(" The three most frequent name lenghts are: ")

sorted_lengths = sorted(set(length_of_name), key=length_of_name.count, reverse=True)

'''Most frequent length names'''

first_most_frequent_length = []
print(f"\t {length_of_name.count(sorted_lengths[0])} Names of Length {sorted_lengths[0]} : ", end="")
for name in names:
    if len(name) == sorted_lengths[0]:
        first_most_frequent_length.append(name)
print(f" '{first_most_frequent_length}'", end=" ")

second_most_frequent_length = []
print(f"\n\t {length_of_name.count(sorted_lengths[1])} Names of Length {sorted_lengths[1]} : ", end="")
for name in names:
    if len(name) == sorted_lengths[1]:
        second_most_frequent_length.append(name)
print(f" '{second_most_frequent_length}'", end=" ")

third_most_frequent_length = []
print(f"\n\t {length_of_name.count(sorted_lengths[2])} Names of Length {sorted_lengths[2]} : ", end="")
for name in names:
    if len(name) == sorted_lengths[2]:
        third_most_frequent_length.append(name)
print(f" '{third_most_frequent_length}'", end=" ")

'''Least frequent length names'''

print(f"\n4.\n The three least frequent name lenghts are: ")
first_least_frequent_length = []
print(f'\t {length_of_name.count(sorted_lengths[-1])} Names of Length {sorted_lengths[-1]} : ', end="")
for name in names:
    if len(name) == sorted_lengths[-1]:
        first_least_frequent_length.append(name)
print(f" '{first_least_frequent_length}'", end=" ")

second_least_frequent_length = []
print(f'\n\t {length_of_name.count(sorted_lengths[-2])} Names of Length {sorted_lengths[-2]} : ', end="")
for name in names:
    if len(name) == sorted_lengths[-2]:
        second_least_frequent_length.append(name)
print(f" '{second_least_frequent_length}'", end=" ")


third_least_frequent_length = []
print(f'\n\t {length_of_name.count(sorted_lengths[-3])} Names of Length {sorted_lengths[-3]} : ', end="")
for name in names:
    if len(name) == sorted_lengths[-3]:
        third_least_frequent_length.append(name)
print(f" '{third_least_frequent_length}'", end=" ")


# length_of_name_list = [len(name) for name in names]
# print(length_of_name_list)