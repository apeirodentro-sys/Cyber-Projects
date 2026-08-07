import re

def checker(password):
    #criteria
    criterias = {
        "has_length": len(password) >= 8,
        "has_upper": bool(re.search(r"[A-Z]", password)),
        "has_lower": bool(re.search(r"[a-z]", password)),
        "has_special": bool(re.search(r"[^a-zA-Z0-9]", password)),
        "has_number": bool(re.search(r"[0-9]", password))
    }

    #feedback for missing criteria
    if not criterias.get("has_length"):
        print("Shorter than 8 characters")
    if not criterias.get("has_upper"):
        print("No upper character")
    if not criterias.get("has_lower"):
        print("No lower character")
    if not criterias.get("has_special"):
        print("No special character")
    if not criterias.get("has_number"):
        print("No numbers")
    
    #scoring
    points = sum(criterias.values())
    if points < 3:
        print("Weak Password")
    elif points == 3:
        print("Medium Password")
    else:
        print("Strong Password")

checker(input("Input your password: "))

#test