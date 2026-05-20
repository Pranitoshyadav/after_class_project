start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

numbers = list(range(start, end + 1))

evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]

print("Numbers:", numbers)
print("Even numbers:", evens)
print("Odd numbers:", odds)