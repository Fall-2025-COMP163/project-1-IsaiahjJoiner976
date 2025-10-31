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
    base_stats = {
        "Warrior": (20, 3, 60),
        "Mage": (8, 21, 20),
        "Rogue": (11, 12, 20),
        "Cleric": (11, 19, 40),
    }
    if character_class in base_stats:
        base_str, base_mag, base_hp = base_stats[character_class]
    else:
        print("ERROR: Invalid Class")
        return None
    
    stat_per_level_mod = (level - 1) * 5
    stat_per_level = (level - 1) * 3
    stat_per_level_low = (level - 1) * 2
    
    if level >= 1:
        if character_class == "Warrior":
            final_str = base_str + stat_per_level_mod
            final_mag = base_mag + stat_per_level_low
            final_hp = base_hp + stat_per_level_mod
            return (final_str, final_mag, final_hp)
        elif character_class == "Mage":
            final_str = base_str + stat_per_level_low
            final_mag = base_mag + stat_per_level_mod
            final_hp = base_hp + stat_per_level
            return (final_str, final_mag, final_hp)
        elif character_class == "Rogue":
            final_str = base_str + stat_per_level
            final_mag = base_mag + stat_per_level
            final_hp = base_hp + stat_per_level_low
            return (final_str, final_mag, final_hp)
        elif character_class == "Cleric":
            final_str = base_str + stat_per_level
            final_mag = base_mag + stat_per_level_mod
            final_hp = base_hp + stat_per_level_mod
            return (final_str, final_mag, final_hp)
        else:
            return None
    else:
        print("ERROR: Invalid level")
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
    directory_parts = os.path.split(filename)
    directory = directory_parts[0]

    if directory != "":
        if not os.path.exists(directory):
            print(f"ERROR: Directory '{directory}' does not exist. File cannot be saved.")
            return False

    if directory == "":
        directory = "."
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
        print(f"File '{filename}' not found.")
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
    current_class = character["class"]
    new_level = character["level"] + 1
    new_stats = calculate_stats(current_class, new_level)
    if new_stats == None:
        print(f"ERROR: Invalid Class or level calculation")
        return None
    character["level"] = new_level
    character["strength"] = new_stats[0]
    character["magic"] = new_stats[1]
    character["health"] = new_stats[2]
    return None
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
