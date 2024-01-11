print('Enter the english message: ')
message = input()

Vowels = ('a', 'e', 'i', 'o', 'u')

PigLatin = []

for word in message.split():
     # Separate the non-letters at the start of this word:
    prefixNonLetter = ' '
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetter += word[0]
        word = word[1:]
    if len(word) == 0:
        PigLatin.append(prefixNonLetter)
        continue
    
    
     # Separate the non-letters at the end of this word:
    suffixNonLetter = ' '
    while not word[-1].isalpha():
        suffixNonLetter = word[-1] + suffixNonLetter
        word = word[:-1]
        
    # Remember if the word was in uppercase or title case.
    WasUpper = word.isupper()
    WasTittle = word.istitle()
    
    word = word.lower()  # Make the word lowercase for translation.
    
     # Separate the consonants at the start of this word:
    prefixConstants = ''
    while len(word) > 0 and not word[0] in Vowels:
        prefixConstants += word[0]
        word = word[1:]
        
    # Add the Pig Latin ending to the word:
    if prefixConstants != '': 
        word += prefixConstants + 'ay'
    else: 
        word += 'yay'
        
    # Set the word back to uppercase or title case:
    if WasUpper:
        word= word.upper()
    if WasTittle:
        word = word.title()
        
    # Add the non-letters back to the start or end of the word.
    PigLatin.append(prefixNonLetter + word + suffixNonLetter)
    
# Add the non-letters back to the start or end of the word.
print(' '.join(PigLatin))
        
    
    
