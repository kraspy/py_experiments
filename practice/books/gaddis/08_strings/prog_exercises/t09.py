# Гласные и согласные. Напишите программу с функцией, которая в качестве аргумента
# принимает строковое значение и возвращает количество содержащихся в нем гласных.
# Приложение должно иметь еще одну функцию, которая в качестве аргумента принимает
# строковое значение и возвращает количество содержащихся в нем согласных.
# Приложение должно предоставить пользователю возможность ввести строковое значение
# и показать содержащееся в нем количество гласных и согласных

VOWELS_RU = 'аеёиоуыэюя'
CONSONANTS_RU = 'бвгджзйклмнпрстфхцчшщ'


def count_letter(text: str) -> tuple[int, int]:
    vowels_count = 0
    consonants_count = 0

    for char in text:
        if char.lower() in VOWELS_RU:
            vowels_count += 1
        elif char.lower() in CONSONANTS_RU:
            consonants_count += 1

    return vowels_count, consonants_count


vowels_num, consonants_num = count_letter('АБВГДЕЁЖЗ')

print(f'Гласных: {vowels_num}, Согласных: {consonants_num}.')
