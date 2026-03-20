


def advanced_check(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")

    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    return score, feedback


pwd = input("Enter password: ")
score, feedback = advanced_check(pwd)

print("Score:", score, "/ 5")

if score == 5:
    print("Strong Password ✅")
else:
    print("Improve:")
    for f in feedback:
        print("-", f)
