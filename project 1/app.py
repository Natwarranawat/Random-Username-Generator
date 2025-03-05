import random
import string

def generate_username(include_numbers=True, include_special_chars=True, length=8):
    """Generates a random username based on user preferences."""
    adjectives = ["Cool", "Happy", "Fast", "Brave", "Clever", "Funny", "Loud", "Strong", "Mighty", "Epic"]
    nouns = ["Tiger", "Dragon", "Warrior", "Phoenix", "Ninja", "Knight", "Wizard", "Panther", "Falcon", "Wolf"]
    
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    return username[:length]  # Ensure username length constraint

def save_to_file(username, filename="usernames.txt"):
    """Saves the generated username to a file."""
    try:
        with open(filename, "a") as file:
            file.write(username + "\n")
        print(f"Username '{username}' saved to {filename}")
    except IOError:
        print("Error: Could not write to file.")

def get_user_input(prompt, default_value, value_type=str):
    """Handles user input with validation."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                return default_value
            return value_type(user_input)
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    """Main function to interact with the user."""
    print("Welcome to the Random Username Generator!")
    include_numbers = get_user_input("Include numbers? (y/n): ", 'y').lower() == 'y'
    include_special_chars = get_user_input("Include special characters? (y/n): ", 'y').lower() == 'y'
    length = get_user_input("Enter preferred username length (default 8, max 20): ", 8, int)
    length = min(max(4, length), 20)  # Ensure length is within valid range
    
    num_usernames = get_user_input("How many usernames would you like to generate? ", 1, int)
    
    usernames = [generate_username(include_numbers, include_special_chars, length) for _ in range(num_usernames)]
    
    print("Generated Usernames:")
    for username in usernames:
        print(username)
        save_to_file(username)

if __name__ == "__main__":
    main()
