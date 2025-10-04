from rich import print
from fractions import Fraction

result = Fraction(0)
for i in range(30):
    current_fraction = Fraction(i + 1, 30 - i)
    result += current_fraction

print('🏁 [green]Finish[/green] 🏁 ')
print(result)
