
def analyze_words(text):
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
            






    



