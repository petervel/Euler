def is_divisible_by(number, divider):
    if number < divider:
        return False
    return number % divider == 0

def is_prime(number):
    return not [y for y in range(2,number) if number % y == 0]

def generate_primes(max):
    primes = []
    for i in range(2, max):
        if is_prime(i):
            primes.append(i)
    return primes

def algorithm(number, primes):
    for i in primes:
        if is_divisible_by(number, i):
            quotient = number / i
            success = True
            if quotient != 1:
                success = algorithm(quotient, primes)

            if success:
                print " {0} ".format(i)
                return success
    return False

def main():
    number = 600851475143
    primes = generate_primes(10000)
    primes.reverse()
    algorithm(number, primes)

main()

