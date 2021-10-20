# Book Cipher

This project is for decrypting [book ciphers](https://en.wikipedia.org/wiki/Book_cipher).

It includes the following functions useful for decrypting them:

```
clean_alpha_string(inputString:str) -> str
```

Takes a space delimited alphabet character string and
returns the string without any non-word characters
such as punctuation. Retains spaces for delimiting words.

```
clean_jsonp(jsonp)
```

Takes a JSONP response string and converts it JSON string.

```
clean_numeric_string(inputString:str) -> str
```

Takes a space delimited numeric character string and
returns the string without any non-numeric characters
such as punctuation. Retains spaces for delimiting numbers.

```
numeric_string_to_list_of_int(numericStr:str) -> list[int]
```

Takes a string of space delimited numbers and returns a list of integers

```
number_words(text:str) -> dict
```
Takes a space delimited string of words and
returns a dict with each position, starting at 1,
as the key and each word as the value.

```
lookup_numerical_cipher(cipher:list[int], dictionary:dict) -> list[str]
```
Takes a list of integers and a dictionary of keys and words.
Returns a list of words corresponding to the numbers.

```
first_letters(wordlist:list[str]) -> str
```
Takes list of strings and returns a string composed of
the first letters of each word in lowercase
```
reverse_words(text:str) -> str
```
Takes a space delimited text and returns the text
with the word order reversed.