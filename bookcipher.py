#!/usr/local/bin/python3
import re
import doctest

def clean_alpha_string(inputString:str) -> str:
    """ Takes a space delimited alphabet character string and
        returns the string without any non-word characters
        such as punctuation. Retains spaces for delimiting words.

        >>> clean_alpha_string('This! is, a string.')
        'This is a string'

    """
    return re.sub('[^\w\s]', '', inputString)

def clean_jsonp(jsonp):
    """ Takes a JSONP response string and converts it JSON string.

        >>> clean_jsonp("foo({'book': { chapters: [1, 2, 3, 4]}})")
        "{'book': { chapters: [1, 2, 3, 4]}}"
    """
    startidx = jsonp.find('(')
    endidx = jsonp.rfind(')')
    return jsonp[startidx + 1:endidx]


def clean_numeric_string(inputString:str) -> str:
    """ Takes a space delimited numeric character string and
        returns the string without any non-numeric characters
        such as punctuation. Retains spaces for delimiting numbers.

        >>> clean_numeric_string('11, 22, 33, 44, 55')
        '11 22 33 44 55'
        >>> clean_numeric_string('(11) (22) (33) (44) (55)')
        '11 22 33 44 55'
    """
    return re.sub('[^\d\s]', '', inputString)

def numeric_string_to_list_of_int(numericStr:str) -> list[int]:
    """ Takes a string of space delimited numbers and
        returns a list of integers
    
        >>> numeric_string_to_list_of_int('11 22 33 44 55')
        [11, 22, 33, 44, 55]
    """
    return list(map(int, numericStr.split()))

def number_words(text:str) -> dict:
    """ Takes a space delimited string of words and
        returns a dict with each position, starting at 1,
        as the key and each word as the value.

        >>> number_words('when in the course of human events')
        {1: 'when', 2: 'in', 3: 'the', 4: 'course', 5: 'of', 6: 'human', 7: 'events'}
    """
    dictionary = {}
    words = text.split()
    for index, word in enumerate(words):
        dictionary[index + 1] = word
    return dictionary

def lookup_numerical_cipher(cipher:list[int], dictionary:dict) -> list[str]:
    """ Takes a list of integers and a dictionary of keys and words.
        Returns a list of words corresponding to the numbers.

        >>> lookup_numerical_cipher([2,4,3,5,1,6], {1: 'meet', 2:'its', 3: 'nice', 4:'very', 5:'to', 6:'you'})
        ['its', 'very', 'nice', 'to', 'meet', 'you']
    """
    wordlist = []
    for num in cipher:
        wordlist.append(dictionary[num])
    return wordlist

def first_letters(wordlist:list[str]) -> str:
    """ Takes list of strings and returns a string composed of
        the first letters of each word in lowercase

        >>> first_letters(['happy', 'elephant', 'lion', 'lives', 'open'])
        'hello'
    
    """
    plaintext = []
    for word in wordlist:
        plaintext.append(word[0].lower())
    return ''.join(plaintext)

def reverse_words(text:str) -> str:
    """ Takes a space delimited text and returns the text
        with the word order reversed.

        >>> reverse_words('This will be backwards')
        'backwards be will This'
    
    """
    return ' '.join(reversed(text.split()))

if __name__ == "__main__":
    import doctest
    doctest.testmod()