keywords = [
    "urgent",
    "verify",
    "account",
    "password",
    "click here",
    "login",
    "bank",
    "security alert"
]

email = input("Enter email content: ").lower()

score = 0
for word in keywords:
    if word in email:
        score += 1

if score >= 2:
    print("⚠️ Possible Phishing Email Detected")
else:
    print("✅ Email Looks Safe")


Purpose

Demonstrates rule-based phishing detection

Used for learning, not production security
