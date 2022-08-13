import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

if __name__ == '__main__': # commands from explanation video
    print(is_palindrome('hello world'))
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))
