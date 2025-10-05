from rich import print


def input_number(prompt: str):
    try:
        number = int(input(prompt))
    except ValueError:
        print('[red]Invalid Number![/red]')
        exit()
    return number
