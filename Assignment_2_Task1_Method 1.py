# Print if a number (int) is odd or even.
# even - when the number is divisible by 2. remainder is 0
# odd - the number is NOT divisible by 2. remainder is not 0

num = int(input("Enter a number: "))

if num%2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
