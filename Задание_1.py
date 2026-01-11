def print_range(A, B):
    for i in range(A, B + 1):
        print(i, end=' ')
    print()
def print_range_order(A, B):
    if A < B:
        for i in range(A, B + 1):
            print(i, end=' ')
    else:
        for i in range(A, B - 1, -1):
            print(i, end=' ')
    print()
def print_odd_descending(A, B):
    for i in range(A, B - 1, -1):
        if i % 2 != 0:
            print(i, end=' ')
    print()
def sum_numbers():
    N = int(input("Введите количество чисел: "))
    total = 0
    for _ in range(N):
        total += int(input("Введите число: "))
    print("Сумма:", total)
def sum_cubes(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def sum_factorials(n):
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i  
        total += fact
    return total
def print_stairs(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
def fibonacci_sum(N):
    if N <= 0:
        return 0
    elif N == 1:
        return 1
    
    a, b = 0, 1
    total = 1  
    
    for _ in range(2, N): 
        a, b = b, a + b
        total += b
    return total
def fibonacci_sum_from_k(N, K):
    if K <= 0 or N <= 0:
        return 0
    
    a, b = 0, 1
    total = 0
    count = 0
    
    for i in range(1, K + N):
        if i >= K:  
            total += a
            count += 1
            if count == N:
                break
        a, b = b, a + b
    return total
# Тестирование функций
print("Задача 1:")
print_range(1, 5)

print("\nЗадача 2:")
print_range_order(5, 1)

print("\nЗадача 3:")
print_odd_descending(10, 1)

print("\nЗадача 4:")
sum_numbers()

print("\nЗадача 5:")
print(sum_cubes(3)) 

print("\nЗадача 6:")
print(factorial(5))

print("\nЗадача 7:")
print(sum_factorials(3)) 

print("\nЗадача 8:")
print_stairs(4)

print("\nЗадача 9:")
print(fibonacci_sum(5)) 

print("\nЗадача 10:")
print(fibonacci_sum_from_k(4, 3)) 