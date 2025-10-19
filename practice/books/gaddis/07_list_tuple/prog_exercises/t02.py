import random


def get_random_int() -> int:
    return random.randint(1, 9)


def generate_ticket(length: int = 7) -> list:
    ticket_numbers = [get_random_int() for _ in range(length)]

    return ticket_numbers


def main():
    ticket = generate_ticket()

    print(''.join(map(str, ticket)))


if __name__ == '__main__':
    main()
