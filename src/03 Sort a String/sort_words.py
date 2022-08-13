def sort_words(input):
    return ' '.join(sorted(input.split(), key=str.casefold))

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
