# Count Even, Odd, and Prime Numbers in a List

# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input numbers separated by space
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_count = 0
odd_count = 0
prime_count = 0
prime_numbers = []

# Counting even, odd, and prime numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if is_prime(num):
        prime_count += 1
        prime_numbers.append(num)

# Output
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
print("Prime numbers count:", prime_count)
print("Prime numbers are:", prime_numbers)