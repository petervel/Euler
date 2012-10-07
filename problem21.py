
def get_divisors(number):
    divisors = []
    half = int((number / 2) + 1)
    for i in range(1, half):
        if number % i == 0:
            divisors.append(i)
    return divisors

def sum_divisors(number):
    sum = 0
    for i in get_divisors(number):
        sum += i
    return sum

def is_amicable_number(number):
    sum = sum_divisors(number)
    if sum == number:
        return False
    return sum_divisors(sum) == number

def sum_amicable_numbers(numbers):
    sum = 0
    for i in numbers:
        if is_amicable_number(i):
            sum += i
    return sum

def main():
    numbers = range(1, 10000)
    sum = sum_amicable_numbers(numbers)
    print(sum)

main()
