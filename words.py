def print_upper_words(words, must_start_with):
    for x in words:
        for letter in must_start_with:
            if x.startswith(letter):
                print(x.upper())
                
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})