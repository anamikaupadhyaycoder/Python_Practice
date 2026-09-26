
'''def analyze_words(text):
    words=text.split()
    vowels="aeiouAEIOU"
    max_vowels=0
    word_with_most_vowels=None
    longest_word=None
    no_words_with_atleast_2_vowels=0

    for word in words:
        vowels_count=0

        for char in word:
            if char in vowels:
                vowels_count+=1
            if vowels_count>max_vowels:
                max_vowels=vowels_count
                word_with_most_vowels=word
            
    for word in words:
        if longest_word is None or len(word)>len(longest_word):
            longest_word=word

    for word in words:
        vowel_count_2=0

        for char in word:
            if char in vowels:
                vowel_count_2+=1
        if vowel_count_2>=2:
            no_words_with_atleast_2_vowels+=1
    return word_with_most_vowels, longest_word, no_words_with_atleast_2_vowels
print(analyze_words("apple banana education computer sky programming"))

def analyze_text(text):
    vowels="aeiouAEIOU"
    words=text.split()
    max_vowels=0
    word_with_most_vowels=None
    count_palindrome=0
    longest_palindrome=None
    count_palind_2=0
    max_palindrome=0

    for word in words:
        vowel_count=0

        for char in word:
            if char in vowels:
                vowel_count+=1
            if vowel_count>max_vowels:
                max_vowels=vowel_count
                word_with_most_vowels=word
    
    for word in words:
        original=word

        reverse=word[::-1]

        if reverse==original:
            count_palindrome+=1

    for word in words:
        original=word
        reverse=word[::-1]

        if reverse==original:
            count_palind_2+=1
            if len(word)>max_palindrome:
                max_palindrome=len(word)
                longest_palindrome=word
    return word_with_most_vowels, count_palindrome, longest_palindrome
print(analyze_text("hello apple banana level radar education"))

def analyze_text(text):
    words=text.split()
    longest_word=None
    count_a=0
    seen=[]
    repeated_count=0
    
    for word in words:
        if longest_word is None or len(word) > len(longest_word):
            longest_word=word

    for word in words:
        if "a" in word:
            count_a+=1

    for word in words:
        if word in seen:
            repeated_count+=1
        else:
            seen.append(word)
    return longest_word, count_a, repeated_count
print(analyze_text("Python is an amazing programming language and Python is powerful"))


def analyze_words(text):
    words=text.split()
    longest_palindrome=None
    palindrome_count=0
    vowels="aeiouAEIOU"
    max_vowels=0
    highest_vowel_word=None

    for word in words:
        original=word
        reverse=word[::-1]
        if reverse==original:
            palindrome_count+=1
            if longest_palindrome is None or len(word)>len(longest_palindrome):
                longest_palindrome=word

    for word in words:
        count_vowels=0
        for char in word:
            if char in vowels:
                count_vowels+=1
        if count_vowels>max_vowels:
            max_vowels=count_vowels
            highest_vowel_word=word

    return longest_palindrome, palindrome_count, highest_vowel_word
print(analyze_words("apple level banana radar computer civic education"))'''

def analyze_text(text):
    words=text.split()
    longest_palindrome=None
    vowels="aeiouAEIOU"
    count_2_vowels=0
    count_same_start_end=0

    for word in words:
        original=word
        reverse=word[::-1]
        if reverse==original:
            if longest_palindrome is None or len(word)>len(longest_palindrome):
                longest_palindrome=word

    for word in words:
        count_vowels=0
        for char in word:
            if char in vowels:
                count_vowels+=1
        if count_vowels>=2:
            count_2_vowels+=1
    
    for word in words:
        if word[0]==word[-1]:
            count_same_start_end+=1
    return longest_palindrome, count_2_vowels, count_same_start_end
print(analyze_text("apple banana level education radar computer civic"))






            






    



