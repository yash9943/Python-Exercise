# Fibonacci sequence up to n terms using Recursion
n = 8 
def fibo(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print(fibo(n))
print(fibo(60))
print(fibo(90))

# Sum of numbers using Recursion
print()
numbers =  [23, 44, 5, 67, 1, 1, 2, 4, 5] 
def sum_num(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_num(numbers[1:])

print(sum_num(numbers))