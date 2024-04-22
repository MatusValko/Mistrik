def count_syllables(word):
    # VOWELS + 'ŕ','ĺ','ô', WORDS: kŕdeľ, vŕba, stĺp, kôra
    vowels = ['a','á','ä','e','é','i','í','y','ý','o','ó','u','ú','ŕ','ĺ','ô']
    # DIPHTHONGS + 'au', 'ou', 'oo', WORDS: auto, láskou, zoo,
    diphthongs = ['ia', 'ie', 'iu','au', 'ou', 'oo']

    syllableCount = 0
    # WORDS WITH 2 OR LESS LETTERS HAVE ONLY ONE SYLLABLE: je, mi, to
    if len(word) <= 2:
        return 1
    else:
        word = word.lower()
        
        for diphthong in diphthongs:
            # SUBTRACT 1 FOR EACH DIPTHONG FOUND
            syllableCount -= word.count(diphthong)
        for vowel in vowels:
            # ADD 1 FOR EACH VOWEL FOUND
            syllableCount += word.count(vowel)
            #REPLACE VOWELS TO FIND SYLLABIC CONSONANTS 'R' AND 'L' 
            word = word.replace(vowel, '-')
        
        # FIND THE SYLLABIC CONSONANTS 'R' AND 'L', WORDS: najpRv, zahRmelo, hLboko
        parts = word.split("-")
        for part in parts:
            if len(part)> 2:
                if 'r' in part[1:-1] or 'l' in part[1:-1]:
                    syllableCount +=1
                    
        # WORDS LIKE: hmm, mhm
        if syllableCount <= 0:
            return 1
        # RETURN THE COUNT OF SYLLABLES IN THE WORD 
        return syllableCount

def mistrik_readability(text):
    #CLEAN
    bad_chars = ['’' ,'`',"'", "„", '"', '“', '”', '(', ')', '[', ']', '{', '}', '=' ,'+', '-', '*']
    #DELETE ALL QUOTATION MARKS, PARENTHESES AND OTHER SYMBOLS
    for char in bad_chars:
        text = text.replace(char,"")
    #SPLIT ALL COMPOUND WORDS INTO MULTIPLE WORDS: HORE-DOLE, BRINK-BRINK
    dash_chars = ['-', '–', '—', '/','\\']
    for dash in dash_chars:
        text = text.replace(dash," ")

    words = text.split()
    words_cleaned= []
    
    sentence_count = 1
    syllable_count = 0
    
    for i, word in enumerate(words):
        syllable_count += count_syllables(word)

        #END OF THE SENTENCE
        if word[-1] in ['.','?','!']:
            if i < len(words) - 1:  # #CHECK IF THERE'S A NEXT ITEM (AVOIDING INDEX OUT OF RANGE)
                next_word = words[i + 1]
                if next_word[0].isupper(): # NEXT WORD, FIRST LETTER IS CAPITAL = NEXT SENTENCE
                    sentence_count += 1
        # THE FINAL CLEANING OF THE WORD ENSURES AN ACCURATE COUNT OF UNIQUE WORDS.          
        for char in ['.','?','!',',',';',':']:
             word = word.replace(char,"")  
        if word != "":
            words_cleaned.append(word.lower())

    words = words_cleaned
    
    print("MISTRIK READABILITY METRIC:")
    print("SENTENCES: ",sentence_count)
    
    V = len(words)/ sentence_count
    print(f"V:  {round (V)} ({round(V,2)})")
    V = round (V)
    
    S = syllable_count / len(words)
    print(f"S:  {round (S,1)} ({round(S,3)})")
    S = round (S,1)
    
    N = len(words)
    print(f"N:  {N}")
    
    L = len (set(words))
    print(f"L:  {L}")
    
    I = round (N / L,3)
    print(f"I:  {I}")
    
    R = 50 - ((S * V) / I)
    print(f"R:  {round(R)} ({(round (R,3))})")
    R = round(R)
    return R