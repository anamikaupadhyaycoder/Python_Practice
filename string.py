#practice questions
#1
'''def analyze_text(text):
    count_upper=0
    count_lower=0
    count_digit=0
    for char in text:
        if char.isupper():
            count_upper+=1
        elif char.islower():
            count_lower+=1
        elif char.isdigit():
            count_digit+=1
    return count_upper, count_lower, count_digit
result=analyze_text("PyThOn123")
print(result)

#2. 
def clean_text(text):
    
    s= text.strip().lower()
    return s
result=clean_text(" Python Is AMAZING   ") 
print(result)

#3. 
def analyze_sentence(text):
    words=text.split()
    count=len(words)
    longest_word=None
    count_o=0
    for word in words:
        if longest_word is None or len(word)>len(longest_word):
            longest_word=word
        if "o" in word.lower():
            count_o+=1
    return count, longest_word, count_o
result=analyze_sentence("Python is powerful and easy")
print(result)

#Strings Deep — Level 2.2: Word Filtering
def analyze_sentence(text):
    words=text.split()
    longest_word=None
    count_with_4=0
    count_i=0

    for word in words:
        if longest_word is None or len(word)>len(longest_word):
            longest_word=word
        if len(word)>4:
            count_with_4+=1
        if "i" in word.lower():
            count_i+=1
    return longest_word, count_with_4, count_i
result=analyze_sentence("Python is powerful and programming is fun")
print(result)

#word-level processing → character-level processing.
def analyze_text(text):
    vowels="aeiouAEIOU"
    count_vowels=0
    count_consonants=0
    frequency={}
    
    for char in text:
        if char in vowels:
            count_vowels+=1
        if char.isalpha() and char not in vowels:
            count_consonants+=1
        if char.isalpha():
            char=char.lower()
            frequency[char]=frequency.get(char, 0)+1

            if char in frequency:
                frequency[char]+=1
            else:
                frequency[char]=1
    return count_vowels, count_consonants, frequency
result=analyze_text("Programming is Powerful")
print(result)

#
def analyze_sentence(text):
    words=text.split()

    total=0
    for word in words:
        if word.lower().count("a")>=2:
            total+=1
    return total
print(analyze_sentence("apple banana data area python"))

def analyze_sentence(text):
    words=text.split()
    result=[]

    for word in words:
        if len(word)>5 and word[0].lower()==word[-1].lower():
            result.append(word)
    return result
print(analyze_sentence("level Python radar apple civic banana"))

def analyze_text(text):
    words=text.split()
    longest=None
    count_long=0
    count=0

    for word in words:
        if len(word)>4:
            count_long+=1
        if longest is None or len(word)>len(longest) :
            longest=word
        if word.lower().count("a"):
            count+=1
    return longest, count_long, count
print(analyze_text("Pyhton is an amazing programming language")) '''

def analyze_sentence(text):
    words=text.split()
    vowels="aeioUAEIOU"
    vowels_count_2=0
    word_vowels=None
    max_vowels=0
    same_start_end_count=0
   

    for word in words:
        vowels_count=0

        for char in word:
            if char in vowels:
                vowels_count+=1
        if vowels_count>=2:
            vowels_count_2+=1
        if word_vowels is None or vowels_count>max_vowels:
            word_vowels=word
            max_vowels=vowels_count
        if word[0].lower()==word[-1].lower():
            same_start_end_count+=1
    return vowels_count_2, word_vowels, same_start_end_count
print(analyze_sentence("apple banana level education radar computer"))


