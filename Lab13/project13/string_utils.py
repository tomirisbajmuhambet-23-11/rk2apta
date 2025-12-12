def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())

def count_letters(s):
    return sum(1 for ch in s if ch.isalpha())
