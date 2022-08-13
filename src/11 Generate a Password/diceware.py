import secrets

def generate_passphrase(num_words):
    with open('diceware.wordlist.asc', 'r') as file:    
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)

# commands used in solution video for reference
if __name__ == '__main__':
    print(generate_passphrase(7))
    print(generate_passphrase(7))