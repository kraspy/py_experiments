def get_slang_text(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError('Text must be a string!')

    splitted_words = text.split(' ')

    new_words = []

    for word in splitted_words:
        new_words.append(f'{word[1:]}{word[0]}КИ')

    return ' '.join(new_words)


print(
    get_slang_text('ПРОСПАЛ ПОЧТИ ВСЮ НОЧЬ'),
)
