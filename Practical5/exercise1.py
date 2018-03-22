

def main():
    total_numbers = 5
    numbers = []
    for i in range(total_numbers):
        number = int(input("Number:"))
        numbers.append(number)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))



main()