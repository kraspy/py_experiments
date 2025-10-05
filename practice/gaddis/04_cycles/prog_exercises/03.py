from rich import print

plan_monthly_expense = int(input('Enter your monthly expense (plan): '))

expense_categories: dict[str, int] = {}
actual_monthly_expense = 0

while True:
    category = input('Enter the category name: ')

    try:
        amount = int(input('Enter the amount: '))
    except ValueError:
        print('[red]Invalid Number![/red]')
        continue

    if category in expense_categories:
        expense_categories[category] += amount
    else:
        expense_categories[category] = amount

    actual_monthly_expense += amount

    user_choice = input('Do you want to add another category? (y/n)')
    if user_choice == 'y':
        continue
    elif user_choice == 'n':
        break
    else:
        print('[red]Invalid Input[/red]')

rest = plan_monthly_expense - actual_monthly_expense


if rest > 0:
    print(f'✅ You saved: {rest}')
elif rest < 0:
    print(f"❌ Yo've exceeded the plan: {plan_monthly_expense}")
else:
    print('👍 You are great planner!')
