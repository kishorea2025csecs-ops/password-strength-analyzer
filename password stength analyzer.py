
import math
import string
import getpass

def analyze_password(password):
    length = len(password)

    # Identify character types
    pool_size = 0

    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    # Calculate estimated entropy
    entropy = length * math.log2(pool_size) if pool_size else 0

    # Score out of 100
    score = 0

    if length >= 8:
        score += 20
    if length >= 12:
        score += 20
    if length >= 16:
        score += 10
    if pool_size >= 26:
        score += 10
    if pool_size >= 52:
        score += 10
    if pool_size >= 62:
        score += 10
    if pool_size >= 80:
        score += 10
    if entropy >= 60:
        score += 10

    score = min(score, 100)

    # Verdict
    if length < 8 or score < 40:
        verdict = "WEAK"
    elif score < 70:
        verdict = "MEDIUM"
    elif score < 90:
        verdict = "STRONG"
    else:
        verdict = "VERY STRONG"

    print("\n--- PASSWORD STRENGTH REPORT ---")
    print("Length  :", length, "characters")
    print("Entropy :", round(entropy, 2), "bits (estimated)")
    print("Score   :", str(score) + "/100")
    print("Verdict :", verdict)

password = getpass.getpass("Enter password: ")
analyze_password(password)
