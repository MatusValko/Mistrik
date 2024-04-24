class Result:
    def __init__(self, SEN, SYL, V, S, N, L, I, R):
        self.SEN = SEN
        self.SYL = SYL
        self. V3 = round(V,3)
        self. V = round(V)
        self. S3 = round(S,3)
        self. S = round(S,1)
        self. N = N
        self. L = L
        self. I = round(I,2)
        self. R3 = round(R,3)
        self. R = round(R)

    def __str__(self):
        return "MISTRIK MEASURE OF READABILITY:\nSENTENCES: {}\nSYLLABLES: {}\nV: {} ({})\nS: {} ({})\nN: {}\nL: {}\nI: {}\nR: {} ({})". \
            format(self.SEN, self.SYL, self.V, self.V3,self.S,self.S3,self.N,self.L,self.I,self.R,self.R3)

class Mistrik:
    def __init__(self, text):
        self.text = self.__cleanText(text)
        # self.cleanText = self.__cleanText(text)

    def __cleanText(self, text):
        #CLEAN
        bad_chars = ['’' ,'`',"'", "„", '"', '“', '”', '(', ')', '[', ']', '{', '}', '=' ,'+', '*']
        #DELETE ALL QUOTATION MARKS, PARENTHESES AND OTHER SYMBOLS
        for char in bad_chars:
            text = text.replace(char,"")
        #SPLIT ALL COMPOUND WORDS INTO MULTIPLE WORDS: HORE-DOLE, BRINK-BRINK
        dash_chars = ['-', '–', '—', '/','\\']
        for dash in dash_chars:
            text = text.replace(dash,"  ")
        return text
    
    
    def __syllables(self,word):
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

    
    def readability(self):
        words = self.text.split()
        words_cleaned= []
        
        sentence_count = 1
        syllable_count = 0
        for i, word in enumerate(words):
            
            syllable_count += self.__syllables(word)
    
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
        
        V = len(words)/ sentence_count
        S = syllable_count / len(words)
        N = len(words)
        L = len (set(words))
        I = round (N / L,3)
        R = 50 - ((S * V) / I)
        
        return Result(SEN=sentence_count, SYL=syllable_count, V=V, S=S, N=N, L=L, I=I, R=R)