def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold))
