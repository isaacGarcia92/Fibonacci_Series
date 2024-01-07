def parse_int(string):
    try:
        return int(string)
    except ValueError:
        return None


def validate_int():
    while True:
        num_input = input('Enter a number: ')
        parsed_int = parse_int(num_input)

        if parsed_int is None:
            print('Invalid Input!')
        elif parsed_int <= 0:
            print('Please enter a number greater than 0')
        else:
            return parsed_int


def fibonacci_sequence(user_range):
    first_number, sec_number = 0, 1
    array_range = []

    for i in range(user_range):
        array_range.append(first_number)
        first_number, sec_number = sec_number, first_number + sec_number
    print('Your fibonacci sequence is the following:')
    print(array_range)


def main():
    user_number = validate_int()
    fibonacci_sequence(user_number)


if __name__ == '__main__':
    main()




