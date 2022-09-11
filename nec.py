alphabet = {"a": 5, "b": 2, "c": 1, "d": 3, "e": 4, "f": 7, "g": 54, "h": 62, "i": 74, "j": 99, "k": 12, "l": 43, "m": 56, "n": 32, "o": 50, "p": 85, "q": 22, "r": 8, "s": 20, "t": 27, "u": 60, "v": 78, "w": 11, "x": 13, "y": 16, "z": 51} # the alphabet we're gonna use

input_word = input("Input a sentence : ") # user input

for q in input_word: # looping trough the alphabet
    result = alphabet[q] + alphabet[q] # doubling the numbers as a obfuscation technique, to decode just cut them in half.
    print("Number - > ", result) # printing the result

