#starting with string 
#1. 
'''def analyze_word(text):
    s=text.startswith("Py")
    r=text.endswith("ing")
    e=text.count("o")
    return s, r, e
result=analyze_word("Python programming")
print(result)
#2. 
def analyze_word(text):
    spaces=text.strip()
    lower=text.lower()
    count=len(text.split())
    return spaces, lower, count
result=analyze_word("   Python is AMAZING   ")
print(result)'''

#3. 
def extract_digits(text):
    result= ""

    for char in text:
        if char.isdigit():
            result+=char
    return result

r=extract_digits("Python123abc45")
print(r)

