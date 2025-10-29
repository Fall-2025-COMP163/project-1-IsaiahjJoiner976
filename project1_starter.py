"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    char_stats = {"name": name, "class": character_class, "level": 1, "gold": 100}
    stats = calculate_stats(character_class, 1)
    if stats is None:
        print(f"Error: Invalid character class '{character_class}'")
        return None
    char_stats["strength"] = stats[0]
    char_stats["magic"] = stats[1]
    char_stats["health"] = stats[2]
    return char_stats
    pass

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    Warrior_char = (20, 3, 60)
    Mage_char = (8, 21, 20)
    Rogue_char = (11, 12, 20)
    Cleric_char = (11, 19, 40)
    if character_class == "Warrior":
        return Warrior_char
    elif character_class == "Mage":
        return Mage_char
    elif character_class == "Rogue":
        return Rogue_char
    elif character_class == "Cleric":
        return Cleric_char
    else:
        return None
    pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    with open(filename, 'w') as file:
        for key, value in character.items():
            if key == "name":
                file.write(f"Character {key.title()}: {value}\n")
                continue
            file.write(f"{key.title()}: {value}\n")
    return True
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    if os.path.exists(filename):
        load_char_data = {}
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue

                key_part, value_str = clean_line.split(':', 1)

                key_part = key_part.strip()
                value_str = value_str.strip()

                if key_part == "Character Name":
                    key = "name"
                else:
                    key = key_part.lower()

                if value_str.isdigit():
                    value = int(value_str)
                else:
                    value = value_str
                load_char_data[key] = value
        return load_char_data
    else:
        print(f"File '{filename} not found.")
        return None
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    character = str(character)
    if os.path.exists(character):
        with open(character, "r") as file:
            print("=== CHARACTER SHEET ===")
            for line in file:
                print(line.strip())
        return True
    else:
        print(f"Error: Character file '{character}' not found.")
        return None
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
