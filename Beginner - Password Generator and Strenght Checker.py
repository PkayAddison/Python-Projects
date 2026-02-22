import string
import random
def generate_password(length,upper_case,lower_case,number,special):
    characters = ""
    if upper_case:
        characters += string.ascii_uppercase
    if lower_case:
        characters += string.ascii_lowercase
    if number:
        characters += string.digits
    if special:
        characters += string.punctuation
    if not characters:
        return "No character types selected"
    
    password = "" .join(random.choice(characters) for _ in range(length))
    return password


def strenght_checker(password):
    length = len(password)
    score = 0
    if length >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score +=1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if score<= 2:
        return "Weak Password"
    elif score == 3:
        return "Moderate"
    else:
        return "Strong Password"
        
        




def main_code():
    print("Welcome to Password Generator/Strength Checker")
    
    length = int(input("How long do you want your password to be? "))
    upper_case = input("Do you want to include an upper case character?(y/n) ").lower() == "y"
    lower_case = input("Do you want to include a lower case character?(y/n) ").lower() == "y"
    number = input("Do you want to include a number?(y/n) ").lower() == "y"
    special = input("Do you want to include a special charcter?(y/n)" ).lower() == "y"
    
    password = generate_password(length,upper_case,lower_case,number, special)
    print(f"Password Generated: {password}")
    
    strength = strenght_checker(password)
    print(f"Password Strength: {strength}")
    
if __name__ == "__main__":
    main_code()