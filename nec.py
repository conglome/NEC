alphabet = {"a": 5, "b": 2, "c": 1, "d": 3, "e": 4, "f": 7, "g": 54, "h": 62, "i": 74, "j": 99, "k": 12, "l": 43, "m": 56, "n": 32, "o": 50, "p": 85, "q": 22, "r": 8, "s": 20, "t": 27, "u": 60, "v": 78, "w": 11, "x": 13, "y": 16, "z": 51} # the alphabet we're gonna use

hello = alphabet["h"], alphabet["e"], alphabet["l"], alphabet["l"], alphabet["o"] # selecting the letters for the word "hello"

formatted_hello = str(hello).replace(' ', '') # removing spaces
formatted_hello = str(formatted_hello).replace(',', '') # removing commas
formatted_hello = str(formatted_hello).replace('(', '') # removing '('
formatted_hello = str(formatted_hello).replace(')', '') # removing ')'


print("Ciphered 'Hello' - > ", int(formatted_hello)) # printing the result
