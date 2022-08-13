def sort_words(input):
    return ' '.join(sorted(input.split(), key=str.casefold))

if __name__ == '__main__': # commands from explanation video
    print(sort_words('banana ORANGE apple'))
