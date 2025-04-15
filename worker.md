# Automated Input Simulation Tool Documentation

## Overview
This Python script creates an automated system for simulating human-like typing and mouse movements. It uses the `pyautogui` library to automate keyboard and mouse inputs while incorporating random variations to mimic natural human behavior.

## Dependencies
- pyautogui
- time
- random
- os

## Core Components

### 1. Input Data
- Stores HTML code templates in `texts_to_type` list
- Currently contains a basic HTML5 template structure

### 2. Key Functions

#### `simulate_typing(text, words_per_minute=40)`
- Purpose: Simulates human-like typing
- Parameters:
  - text: Content to be typed
  - words_per_minute: Typing speed (default: 40 WPM)
- Features:
  - Calculates delay between characters based on WPM
  - Adds random delays (0.01-0.05 seconds)
  - 5% chance to trigger random mouse movement while typing

#### `random_mouse_move()`
- Purpose: Simulates natural mouse movements
- Features:
  - Moves mouse ±100 pixels from current position
  - Smooth movement with random duration (0.1-0.5 seconds)
  - 30% chance to perform mouse click

#### `simulate_extra_activity()`
- Purpose: Adds realistic user activity simulation
- Actions:
  - Opens Windows Explorer in current directory
  - Performs random scrolling (3-10 times)
  - Simulates Alt+Tab application switching (2-5 times)
  - Includes random delays between actions

#### `main()`
- Purpose: Orchestrates the simulation sequence
- Flow:
  1. Moves cursor to random screen position
  2. Clicks to set focus
  3. Types configured text
  4. Adds random breaks (2-5 seconds)
  5. Triggers extra activities
  6. Loops continuously

## Execution
- Entry point includes 5-second startup delay
- Prints "Debug coding started" message
- Runs in infinite loop until manually stopped

## Usage Notes
1. Ensure proper screen space for mouse movements
2. Script requires appropriate permissions for system interaction
3. Can be stopped using keyboard interrupt (Ctrl+C)
4. Designed for debugging/testing purposes

## Safety Considerations
- Script takes control of mouse and keyboard
- Use with caution in production environments
- Ensure proper exit mechanism is available
- Monitor system resource usage during extended runs

## Customization Points
1. Typing speed (WPM) can be adjusted
2. Mouse movement range can be modified
3. Activity frequencies can be tuned
4. Additional text templates can be added to `texts_to_type`