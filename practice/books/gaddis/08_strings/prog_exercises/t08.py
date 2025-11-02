def text_corrector(text: str) -> None:
    """Преобразует первый символ каждого предложения в верхний регистр."""

    END_SIGNS = '!?.'

    new_text = ''

    is_start_new_sentence = True
    for letter in text:
        if is_start_new_sentence and letter.isalpha():
            new_text += letter.upper()
            is_start_new_sentence = False
            continue

        if letter in END_SIGNS:
            is_start_new_sentence = True

        new_text += letter

    print(new_text)


text_corrector('привет! меня зовут Джо. а как твое имя?')
