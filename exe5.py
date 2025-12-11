numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = 12 
pair = []
final_result = []
for num1 in numbers:
    for num2 in numbers:
        if num1 + num2 == n:
            pair.append((num1, num2))
result = list(set(pair))

print(result)

for res in result:
    res = list(res)
    final_result.append(res)

for a,b in final_result:
    for x,y in final_result:
        if a and b == y and x:
            final_result.remove([y,x])
print(final_result)