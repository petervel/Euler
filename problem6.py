def square_of_sums(rng):
    sum = 0
    for i in rng:
        sum += i
    return pow(sum, 2)

def sum_of_squares(rng):
    sum = 0
    for i in rng:
        sum += pow(i, 2)
    return sum

def main():
    rng = range(1,101)
    print square_of_sums(rng) - sum_of_squares(rng)

main()
