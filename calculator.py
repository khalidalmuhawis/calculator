
def main():
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    operation = input("Choose an operation: ")

    if first_number.isdigit() and second_number.isdigit():
        first_number = int(first_number)
        second_number = int(second_number)
        if operation == "+":
            print(first_number + second_number)
        elif operation == "-":
            print(first_number - second_number)
        elif operation == "/":
            print(first_number / second_number)
        elif operation == "*":
            print(first_number * second_number)
        else:
            print("invalid operation")

    else:
        print("invalid numbers")

    pass




if __name__ == '__main__':
    main()
