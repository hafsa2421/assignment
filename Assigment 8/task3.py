import string

def is_sentence_palindrome(sentence):
    """
    Check if a sentence is a palindrome.
    Ignores case, punctuation, and spaces.
    """
    if not isinstance(sentence, str):
        return False

    # Remove punctuation and spaces, convert to lowercase
    cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())

    # Empty string check
    if not cleaned:
        return False

    # Compare cleaned string with its reverse
    return cleaned == cleaned[::-1]


# ✅ AI-Generated Test Cases
test_sentences = [
    ("A man a plan a canal Panama", True),
    ("No lemon, no melon", True),
    ("Was it a car or a cat I saw", True),
    ("Eva, can I see bees in a cave?", True),
    ("Hello World", False),
    ("Python", False),
    ("", False),  # Empty string
    ("  ", False),  # Only spaces
    ("Madam", True),
    ("Step on no pets!", True),
    ("Top spot", True),
    ("This is not palindrome", False),
    ("12321", True),
    ("12345", False),
]

# ✅ Run AI Test Cases
print("Sentence".ljust(35), "Expected".ljust(10), "Output".ljust(10), "Result")
print("-" * 70)

for sentence, expected in test_sentences:
    result = is_sentence_palindrome(sentence)
    status = "✅ Pass" if result == expected else f"❌ Fail ({result})"
    print(f"{sentence[:30].ljust(35)} {str(expected).ljust(10)} {str(result).ljust(10)} {status}")

# 🧠 User Input Section
print("\nNow test your own sentence!")
user_input = input("Enter a sentence: ")

user_result = is_sentence_palindrome(user_input)

if user_result:
    print("✅ The sentence is a palindrome.")
else:
    print("❌ The sentence is NOT a palindrome.")
