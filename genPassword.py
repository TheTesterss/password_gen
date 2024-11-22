import random
import string

def genPassword(size: int, accept_uppers: bool, accept_numbers: bool, accept_punctuation: bool) -> str:
    # ? Default password.
    password = ""
    # ? The probability to get a certain type of letters.
    chars = {
        "lowers": {
            "value": string.ascii_lowercase,
            "percentage": 100,
            "accepted": True
        },
        "uppers": {
            "value": string.ascii_uppercase,
            "percentage": 0,
            "accepted": False
        },
        "numbers": {
            "value": string.digits,
            "percentage": 0,
            "accepted": False
        },
        "punctuation": {
            "value": string.punctuation,
            "percentage": 0,
            "accepted": False
        }
    }
    keys = list(chars.keys())
    
    # ? Update the accepted types of chars.
    if accept_uppers:
        chars["uppers"]["accepted"] = True
    if accept_numbers:
        chars["numbers"]["accepted"] = True
    if accept_punctuation:
        chars["punctuation"]["accepted"] = True
    
    # ? Adjust the percentages based on the accepted values. 
    accepted = len(list(filter(lambda key: chars[key]["accepted"], keys)))
    default = 100 // accepted if accepted > 0 else 0 
    # ? Manages the rate of each type depending on how much types are accepted.
    for key in keys: 
        if chars[key]["accepted"]: 
            chars[key]["percentage"] = default 
        else: 
            chars[key]["percentage"] = 0
        r = 100 - default * accepted 
        if r > 0: 
            chars["lowers"]["percentage"] += r
    
    # ? Starts creating the string.
    for _ in range(size):
        num = random.randint(1, 100)
        value_1 = 0
        # ? Filtering to give a character that corresponds to the chosen type.
        for key in keys:
            value = chars[key]
            value_1 += value["percentage"]
            if num <= value_1:
                password += random.choice(value["value"])
                break
    
    # ? Returns the final password.
    return password