def multiply(*args):
    total = 1
    for number in args:
        total *= number

    print(total)

multiply(1, 2, 3, 4, 5, 6)

# odd or even number

def odd_even(number):
    odd_number = number % 2 == 0

    if odd_number:
        return f'The number {number} is odd.'
    
    return f'The number {number} is even.'

print(odd_even(2))
print(odd_even(3))
print(odd_even(16))
print(odd_even(17))