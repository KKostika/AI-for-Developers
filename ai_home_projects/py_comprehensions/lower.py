words_ = ["Python","" "IS","" "Better", "Than", "JAVA", "."]

cleaned_words = [w.lower() for w in words_ if w]
print(cleaned_words)

words = ["Hello", "", "World", "", "Python"]
clean_words = [w.lower() for w in words if w]
print(clean_words)