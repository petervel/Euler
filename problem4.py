def is_palindrome(number):
    if len(number) == 0:
        return True

    return number[0] == number[-1] and is_palindrome(number[1:-1])

def main():
    rng = range(1, 999)
    rng.reverse()

    highest = 0
    resultString = ""
    for x in rng:
        for y in rng:
            product = x * y
            if product > highest and is_palindrome(str(product)):
                highest = product
                resultString = "{0} x {1} = {2}".format(x, y, product)

    print resultString

main()
