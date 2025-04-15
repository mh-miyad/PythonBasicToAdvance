# Automated Input Simulation Tool with CSS Auto-Suggestion Support

## Overview
This Python script creates an automated system for simulating human-like typing and mouse movements, with special support for CSS files. It uses the `pyautogui` library to automate keyboard and mouse inputs while incorporating random variations to mimic natural human behavior, including intelligent auto-suggestion behavior for CSS properties.

## Key Improvements
The script has been enhanced to:

1. **Detect CSS files** - The script now attempts to detect when you're working in a CSS file
2. **Simulate auto-suggestions** - When typing CSS properties, it simulates the behavior of waiting for and selecting from auto-suggestions
3. **Use realistic CSS properties and values** - Contains a database of common CSS properties and their values
4. **Create complete CSS rules** - Can generate entire CSS rules with selectors and multiple properties
5. **Mimic human decision-making** - Sometimes accepts suggestions, sometimes continues typing manually

## Dependencies
- pyautogui
- time
- random
- os
- re

## Core Components

### 1. CSS Property Database
- Stores common CSS properties and their values in the `css_properties` dictionary
- Used for intelligent auto-suggestions and value selection

### 2. File Type Detection
- `detect_file_type()` attempts to determine if you're working in a CSS file
- In a real implementation, this would use platform-specific methods to check the active window title

### 3. CSS-Specific Typing Functions
- `simulate_css_typing()` - Simulates typing CSS properties with auto-suggestions
- `create_css_file()` - Creates complete CSS rules with selectors and properties
- `simulate_autocomplete_selection()` - Simulates selecting from an autocomplete dropdown

### 4. Human-Like Behavior
- Adds random pauses between keystrokes
- Sometimes accepts suggestions, sometimes types manually
- Occasionally looks up documentation for CSS properties
- Simulates mouse movements and clicks

## Usage
1. Run the script: `python index.py`
2. The script will start after a 5-second delay
3. Focus your cursor in the editor where you want the typing to occur
4. The script will detect if you're in a CSS file and use appropriate typing behavior
5. Press Ctrl+C in the terminal to stop the script

## Customization
- Adjust typing speed by modifying the `words_per_minute` parameter
- Add more CSS properties and values to the `css_properties` dictionary
- Modify the probability of different behaviors (accepting suggestions, looking up documentation, etc.)

## Safety Considerations
- Script takes control of mouse and keyboard
- Use with caution in production environments
- Ensure proper exit mechanism is available (Ctrl+C in terminal)
- Monitor system resource usage during extended runs
