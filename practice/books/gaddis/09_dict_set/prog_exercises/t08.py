import pickle
from pathlib import Path
from textwrap import dedent

from rich import print

BASEDIR = Path(__file__).resolve().parent

PKL_FILEPATH = BASEDIR / 't08.pkl'

if PKL_FILEPATH.exists():
    with open(BASEDIR / PKL_FILEPATH, 'rb') as f:
        contacts = pickle.load(f)
        print('Contacts database loaded from disc!')
else:
    contacts = {}
    print('Contacts database Created!')


green_text = '[green]{text}[/green]'
red_text = '[red]{text}[/red]'
yellow_text = '[yellow]{text}[/yellow]'
pupr_text = '[purple]{text}[/purple]'

menu = {
    'title': ' MENU ',
    'width': 20,
    'deco_char': '-',
    'choices': dedent("""\
        1. [green]Search contact[/green]
        2. [green]Add contact[/green]
        3. [green]Edit contact[/green]
        4. [red]Remove contact[/red]
        5. [yellow]Exit[/yellow]"""),
}


def show_menu() -> None:
    """Display menu for select email adress-book"""
    print(
        pupr_text.format(
            text=menu['title'].center(menu['width'], menu['deco_char']),
        ),
    )
    print(menu['choices'])
    print(
        pupr_text.format(
            text=menu['deco_char'] * menu['width'],
        ),
        end='\n\n',
    )


def menu_search() -> None:
    search_query = input('Enter contact name: ')

    if search_query in contacts:
        print(green_text.format(text=f'"{search_query}" found!: '))
        print(
            f'[green]User[/green]: {search_query}\n'
            f'[green]E-mail[/green]: {contacts[search_query]}'
        )
    else:
        print(
            red_text.format(text=f'User "{search_query}" not found!'),
        )
    input('Press Enter to go to menu...')


def menu_add() -> None:
    while True:
        contact_name = input('Enter contact Name: ')

        if contact_name in contacts:
            print(
                red_text.format(text='Contact name already exists!\n'),
                'Please enter Another name: ',
            )
            continue

        contact_email = input('Enter contact E-mail: ')

        contacts[contact_name] = contact_email

        print(
            f'Contact "{green_text.format(text=contact_name)} '
            f'({contact_email})" successfully added!'
        )
        break

    input('Press Enter to go to menu...')


def menu_edit() -> None:
    contact_name = input('Enter contact Name which you need to Edit: ')

    if contact_name not in contacts:
        print(
            red_text.format(text="Contact name doesn't exist!\n"),
        )
        return

    contact_email = input('Enter new contact E-mail: ')

    contacts[contact_name] = contact_email

    print(
        f'Contact "{green_text.format(text=contact_name)} '
        f'({contact_email})" successfully Edited!'
    )

    input('Press Enter to go to menu...')


def menu_remove() -> None:
    contact_name = input('Enter contact Name which you need to Delete: ')

    if contact_name not in contacts:
        print(
            red_text.format(text="Contact name doesn't exist!\n"),
        )
        return

    del contacts[contact_name]

    print(f'Contact "{green_text.format(text=contact_name)} successfully Deleted!')

    input('Press Enter to go to menu...')


def menu_exit() -> None:
    print(green_text.format(text='Good bye! 👋'))

    with open(BASEDIR / PKL_FILEPATH, 'wb') as f:
        pickle.dump(contacts, f)
        print('Contacts database saved to disc!')

    exit(0)


def main():
    while True:
        show_menu()

        user_choice = input('Select a menu item: ')

        if not user_choice.isdigit():
            print(
                red_text(text='Please, select a number!'),
            )
            continue

        selected_menu_item = int(user_choice)

        if not 1 <= selected_menu_item <= 5:
            print(
                red_text(text='Please, enter number from 1 to 5.'),
            )
            continue

        match selected_menu_item:
            case 1:
                menu_search()
            case 2:
                menu_add()
            case 3:
                menu_edit()
            case 4:
                menu_remove()
            case 5:
                menu_exit()


if __name__ == '__main__':
    main()
