[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21272808&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# Game Concept
A/your character awakes and roams the world. Having lost your memory you are to traverse the world to find a purpose. Whether that is to become a hero, villain, or a simple farmer is up to you.

# Design Choices
I added modifiers to stat progression as they level up based on the base stats of the character. If the stat starts high that state will grow the largest out of a medium and low base stat. 
Example:
A warrior will naturally level up their strength and health stats faster than a mage who has low strength and health.

# Bonus Creative Features
Besides the modifications based on the character class I didn't add any very creative features.

# AI Usage
I used AI to help explain the errors I was running into and with understanding where I should start in forming the functions. There are a few steps where I did use code from Google Gemini. I have added comments above said code. 

# How to Run
Upon being saved as a Python file open it into an IDE and use the if__name__=="__main__": block.
You can then go through and call the functions creating, saving, and loading a character while also calculating the stats as your character levels up. 
