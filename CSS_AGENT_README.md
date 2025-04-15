# CSS Auto-Suggestion Agent

## Overview
This Python script creates an intelligent CSS typing agent that simulates human-like behavior when writing CSS code. It scans your existing CSS files to learn patterns, property names, values, and selector usage, then uses this knowledge to create realistic CSS code with proper auto-suggestion behavior.

## Key Features

1. **CSS Learning System**:
   - Scans all CSS files in your project
   - Learns selectors, properties, and values from your existing code
   - Tracks which properties are commonly used with specific selectors
   - Builds a knowledge base of your CSS coding patterns

2. **Intelligent Auto-Suggestion**:
   - Simulates VS Code's auto-suggestion behavior
   - Uses Ctrl+Space to trigger suggestions when they don't appear automatically
   - Navigates through suggestion dropdowns like a human would
   - Sometimes accepts suggestions, sometimes continues typing manually

3. **Human-Like Typing**:
   - Types at a realistic speed with natural variations
   - Adds pauses between keystrokes
   - Occasionally pauses to "think" about what to type next
   - Uses proper indentation and formatting

4. **Context-Aware CSS Generation**:
   - Creates CSS rules based on what it learned from your codebase
   - Uses selectors that exist in your project
   - Applies properties that are commonly used with specific selectors
   - Chooses values that match your coding style

## Requirements
- Python 3.6+
- pyautogui
- A project with CSS files to learn from

## Installation
1. Make sure you have Python installed
2. Install the required package: `pip install pyautogui`
3. Download the `new.py` script to your project directory

## Usage
1. Open your CSS file in VS Code or another editor
2. Run the script: `python new.py`
3. The script will:
   - Scan your project for CSS files
   - Learn from your existing CSS code
   - Wait 5 seconds for you to focus your cursor in the editor
   - Start typing CSS code with intelligent auto-suggestions
4. Press Ctrl+C in the terminal to stop the script

## How It Works

### Learning Phase
1. The script recursively searches for all `.css` files in your project
2. It parses each file to extract selectors, properties, and values
3. It builds a database of which properties are used with which selectors
4. It tracks the frequency of property usage to identify common patterns

### Typing Phase
1. The script chooses a selector (preferably one from your codebase)
2. It types the selector and opening brace
3. For each property:
   - It types the first few characters to trigger auto-suggestions
   - If suggestions don't appear, it presses Ctrl+Space
   - It selects from the suggestions or continues typing
   - It adds a value based on what it learned from your code
4. It closes the rule with a closing brace

## Customization
You can modify the script to:
- Change the typing speed
- Adjust the probability of using Ctrl+Space
- Change the number of CSS rules to generate
- Add more default CSS properties and values

## Troubleshooting
- If the script doesn't find any CSS files, make sure you're running it from the correct directory
- If auto-suggestions aren't working properly, try adjusting the timing parameters
- If the script is typing too fast or too slow, modify the typing_speed variable

## Safety Considerations
- The script takes control of your mouse and keyboard
- Make sure you have a way to stop it (Ctrl+C in the terminal)
- Save any important work before running the script
- Don't leave the script running unattended
