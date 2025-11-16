import re

def is_valid_email(email):
    """
    Validate an email address based on these rules:
    1. Must contain '@' and '.' characters.
    2. Must not start or end with special characters (., _, @).
    3. Should not allow multiple '@' symbols.
    """
    if not email or not isinstance(email, str):
        return False

    # Rule 1: Must contain '@' and '.'
    if '@' not in email or '.' not in email:
        return False

    # Rule 2: Should not start or end with special characters
    if email[0] in {'.', '_', '@'} or email[-1] in {'.', '_', '@'}:
        return False

    # Rule 3: Should not contain multiple '@'
    if email.count('@') != 1:
        return False

    # Optional regex pattern for email structure
    pattern = r'^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if not re.match(pattern, email):
        return False

    return True


# ✅ Test cases
test_emails = [
    "user@example.com",          # Valid
    "user.name@domain.co",       # Valid
    "@example.com",              # Invalid
    "user@@example.com",         # Invalid
    "user@.com",                 # Invalid
    "user@domaincom",            # Invalid
    "userdomain.com",            # Invalid
    ".user@domain.com",          # Invalid
    "user@domain.com.",          # Invalid
    "user_name@domain.org",      # Valid
    "user@domain..com"           # Invalid
]

print("📧 Testing predefined emails:\n")
for email in test_emails:
    print(f"{email:25} -> {is_valid_email(email)}")

print("\n------------------------------")
# ✅ User input
user_email = input("Enter an email address to validate: ").strip()
if is_valid_email(user_email):
    print(f"✅ '{user_email}' is a valid email address!")
else:
    print(f"❌ '{user_email}' is NOT a valid email address.")
