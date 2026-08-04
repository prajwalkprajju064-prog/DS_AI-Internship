def is_palindrome(text):
    
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
