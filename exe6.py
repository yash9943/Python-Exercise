string = "PQRQRQRQ"

substring = "QRQ"

# count = string.count(substring) 
# print(count)

count = 0
for str in range(len(string)):
    if string[str:str+len(substring)] == substring:
        count = count + 1
print(count)