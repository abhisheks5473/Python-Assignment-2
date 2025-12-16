# Print if a number (int) is odd or even.
# even - when the number is divisible by 2. remainder is 0
# odd - the number is NOT divisible by 2. remainder is not 0

num = int(input('Enter your number: '))

print(f'{num} is an Even number') if num % 2 == 0 else print(f'{num} is an odd number')
