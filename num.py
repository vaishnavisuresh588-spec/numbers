# Count Even and Odd Numbers in a List

# Input numbers separated by space
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_count = 0
odd_count = 0

# Counting even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Output
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
