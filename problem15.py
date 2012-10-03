
def next_layer(layer):
    prev = 0
    list = []
    for i in layer:
        list.append(prev + i)
        prev = i
    list.append(1)
    return list

def main():
    list = [1]
    for i in range(0,42):
        list = next_layer(list)
        sum = 0
        for number in list:
            sum += number
            print(number),
        print("     -> {0}".format(list[len(list)/2]))

main()
