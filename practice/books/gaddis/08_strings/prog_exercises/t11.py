def split_words(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError('Text must be a string')

    splitted_words = []
    current_word_letters = []

    for index in range(len(text)):
        if not index + 1 >= len(text) and text[index + 1].isupper():
            current_word_letters.append(text[index])
            splitted_words.append(''.join(current_word_letters))
            current_word_letters.clear()
            continue
        current_word_letters.append(text[index])
        continue

    result = ' '.join([word for word in splitted_words]).capitalize()

    return result


text = 'ОстановисьИПочувствуйЗапахРоз'

print(
    split_words(text),
)
