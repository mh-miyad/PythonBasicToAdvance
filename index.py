import pyautogui
import time
import random
import os
import re

# Long HTML code as input
texts_to_type = [
    """<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Long HTML Page</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <!-- Content -->
  </body>
</html>
"""
]

# CSS properties and common values for auto-suggestions
css_properties = {
    "color": ["#fff", "#000", "red", "blue", "green", "rgba(0,0,0,0.5)", "transparent"],
    "background": ["#fff", "#f5f5f5", "transparent", "url(...)"],
    "margin": ["0", "10px", "1rem", "auto"],
    "padding": ["0", "10px", "1rem", "2em"],
    "display": ["block", "flex", "grid", "inline", "none"],
    "position": ["relative", "absolute", "fixed", "static"],
    "width": ["100%", "auto", "50%", "300px"],
    "height": ["100%", "auto", "50vh", "200px"],
    "font-size": ["16px", "1rem", "1.2em", "larger"],
    "font-weight": ["normal", "bold", "400", "700"],
    "text-align": ["left", "center", "right", "justify"],
    "border": ["none", "1px solid black", "2px dashed red"],
    "border-radius": ["0", "5px", "50%", "10px"],
    "box-shadow": ["none", "0 2px 5px rgba(0,0,0,0.3)"],
    "transition": ["all 0.3s ease", "opacity 0.5s"],
    "transform": ["scale(1.1)", "rotate(45deg)", "translateX(10px)"],
    "opacity": ["1", "0.8", "0.5", "0"],
    "z-index": ["1", "10", "100", "-1"],
    "overflow": ["hidden", "auto", "scroll", "visible"],
    "flex-direction": ["row", "column", "row-reverse"],
    "justify-content": ["center", "flex-start", "flex-end", "space-between"],
    "align-items": ["center", "flex-start", "flex-end", "stretch"],
    "gap": ["10px", "1rem", "20px"],
    "grid-template-columns": ["1fr 1fr", "repeat(3, 1fr)", "auto 1fr"],
    "grid-template-rows": ["auto", "1fr 2fr", "repeat(3, 100px)"],
}

# Function to detect file type based on window title or content
def detect_file_type():
    # This is a placeholder - in a real implementation, you would need to
    # use platform-specific methods to get the active window title or content
    # For demonstration, we'll randomly decide if we're in a CSS file
    # In a real implementation, you could use something like:
    # - Windows: win32gui, win32process
    # - macOS: AppKit
    # - Linux: xdotool, wmctrl

    # Simulate 30% chance we're in a CSS file for demonstration
    is_css_file = random.random() < 0.3

    # You could also check for specific window titles containing .css
    # window_title = get_active_window_title()
    # is_css_file = ".css" in window_title.lower()

    return "css" if is_css_file else "html"

# Function to simulate human typing with intelligent CSS suggestions
def simulate_typing(text, words_per_minute=40):
    delay_between_chars = 60 / (words_per_minute * 5)  # Approximate delay (5 chars per word)

    # Detect if we're in a CSS file
    file_type = detect_file_type()

    # If we're in a CSS file, use intelligent typing
    if file_type == "css":
        simulate_css_typing(words_per_minute)
    else:
        # Regular typing for non-CSS files
        for char in text:
            pyautogui.typewrite(char)  # Type the character
            time.sleep(delay_between_chars + random.uniform(0.01, 0.05))  # Add randomness to typing speed
            # Randomly move the mouse occasionally during typing
            if random.random() < 0.05:  # 5% chance to move the mouse
                random_mouse_move()

# Function to simulate typing CSS with intelligent suggestions
def simulate_css_typing(words_per_minute=40):
    delay_between_chars = 60 / (words_per_minute * 5)  # Approximate delay

    # Choose a random CSS property
    property_name = random.choice(list(css_properties.keys()))

    # Type the property name character by character
    for char in property_name:
        pyautogui.typewrite(char)
        time.sleep(delay_between_chars + random.uniform(0.01, 0.05))

    # Pause briefly as if waiting for suggestions
    time.sleep(random.uniform(0.2, 0.5))

    # Simulate pressing Tab or Enter to accept the suggestion
    if random.random() < 0.7:  # 70% chance to use Tab
        pyautogui.press('tab')
    else:
        pyautogui.press('enter')

    # Type the colon and space
    pyautogui.typewrite(': ')
    time.sleep(random.uniform(0.1, 0.3))

    # Choose and type a value for this property
    if property_name in css_properties:
        value = random.choice(css_properties[property_name])

        # Type the value character by character with pauses
        for char in value:
            pyautogui.typewrite(char)
            time.sleep(delay_between_chars + random.uniform(0.01, 0.05))
    else:
        # Fallback for properties not in our database
        pyautogui.typewrite('auto')

    # Type the semicolon
    pyautogui.typewrite(';')
    time.sleep(random.uniform(0.1, 0.3))

    # Press Enter to go to the next line
    pyautogui.press('enter')

# Function to randomly move the mouse to a nearby position
def random_mouse_move():
    current_x, current_y = pyautogui.position()  # Get current mouse position
    new_x = current_x + random.randint(-100, 100)  # Move mouse within ±100 pixels
    new_y = current_y + random.randint(-100, 100)
    pyautogui.moveTo(new_x, new_y, duration=random.uniform(0.1, 0.5))  # Smooth move
    if random.random() < 0.3:  # 30% chance to click
        pyautogui.click()

# Function to simulate selecting from an autocomplete dropdown
def simulate_autocomplete_selection():
    # Wait as if reading suggestions
    time.sleep(random.uniform(0.5, 1.5))

    # Simulate pressing down arrow 1-3 times to navigate suggestions
    for _ in range(random.randint(1, 3)):
        pyautogui.press('down')
        time.sleep(random.uniform(0.2, 0.5))

    # Accept the suggestion with Tab or Enter
    if random.random() < 0.6:
        pyautogui.press('tab')
    else:
        pyautogui.press('enter')

    # Small pause after selection
    time.sleep(random.uniform(0.2, 0.4))

# Function to simulate additional random activities
def simulate_extra_activity():
    # Open a random folder or file
    os.system("explorer .")  # Open current directory in Windows Explorer
    time.sleep(random.uniform(2, 5))

    # Random scrolling
    for _ in range(random.randint(3, 10)):
        pyautogui.scroll(random.randint(-300, 300))  # Scroll up or down
        time.sleep(random.uniform(1, 3))

    # Switching between applications (Alt+Tab)
    for _ in range(random.randint(2, 5)):
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")
        time.sleep(random.uniform(2, 5))

    # Simulate looking up CSS documentation (30% chance)
    if random.random() < 0.3:
        # Simulate opening browser and searching for CSS property
        property_name = random.choice(list(css_properties.keys()))
        print(f"Simulating looking up documentation for: {property_name}")
        # In a real implementation, you could actually open a browser with:
        # os.system(f'start https://developer.mozilla.org/en-US/docs/Web/CSS/{property_name}')

# Function to create a realistic CSS file
def create_css_file():
    # Choose a random number of CSS rules to create
    num_rules = random.randint(3, 8)

    # Create CSS selectors
    selectors = [
        "body", "header", "main", "footer", "nav", ".container", ".header", ".footer",
        ".nav", ".main", "#header", "#footer", "#main", "h1", "h2", "p", "a",
        "button", ".btn", ".card", ".section", "div", "span", "ul", "li", "img"
    ]

    # Simulate typing a complete CSS file
    for _ in range(num_rules):
        # Choose a selector
        selector = random.choice(selectors)

        # Type the selector
        for char in selector:
            pyautogui.typewrite(char)
            time.sleep(random.uniform(0.01, 0.05))

        # Type the opening brace and newline
        pyautogui.typewrite(' {\n')
        time.sleep(random.uniform(0.1, 0.3))

        # Add 2-5 properties to this rule
        num_properties = random.randint(2, 5)
        used_properties = []

        for _ in range(num_properties):
            # Add some indentation
            pyautogui.typewrite('  ')

            # Choose a property that hasn't been used yet in this rule
            available_properties = [p for p in css_properties.keys() if p not in used_properties]
            if not available_properties:  # If all properties used, just pick any
                available_properties = list(css_properties.keys())

            property_name = random.choice(available_properties)
            used_properties.append(property_name)

            # Simulate typing with auto-suggestions
            # Type first few characters to trigger suggestions
            suggestion_point = random.randint(2, len(property_name) - 1)

            # Type the beginning of the property
            for char in property_name[:suggestion_point]:
                pyautogui.typewrite(char)
                time.sleep(random.uniform(0.01, 0.05))

            # Pause as if suggestions appeared
            time.sleep(random.uniform(0.3, 0.7))

            # Accept suggestion
            if random.random() < 0.7:
                pyautogui.press('tab')
            else:
                # Continue typing the rest manually
                for char in property_name[suggestion_point:]:
                    pyautogui.typewrite(char)
                    time.sleep(random.uniform(0.01, 0.05))

            # Type colon and space
            pyautogui.typewrite(': ')
            time.sleep(random.uniform(0.1, 0.3))

            # Choose and type a value
            value = random.choice(css_properties[property_name])
            for char in value:
                pyautogui.typewrite(char)
                time.sleep(random.uniform(0.01, 0.05))

            # Type semicolon and newline
            pyautogui.typewrite(';\n')
            time.sleep(random.uniform(0.1, 0.3))

        # Close the rule
        pyautogui.typewrite('}\n\n')
        time.sleep(random.uniform(0.5, 1.0))

# Main function to run the typing and mouse simulation
def main():
    while True:
        # Determine if we should create HTML or CSS content
        file_type = detect_file_type()

        # Move cursor to a random position on the screen before typing
        screen_width, screen_height = pyautogui.size()
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_height)
        pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 1.5))
        pyautogui.click()  # Click before typing

        if file_type == "css":
            print("Detected CSS file, creating CSS content with auto-suggestions...")
            create_css_file()
        else:
            print("Creating HTML content...")
            for text in texts_to_type:
                simulate_typing(text)  # Type the current text

        time.sleep(random.uniform(2, 5))  # Simulate a short break between sessions

        # Simulate additional activities
        simulate_extra_activity()

# Entry point
if __name__ == "__main__":
    print("Debug coding started. ")
    time.sleep(5)  # Give the user time to focus on the desired input field
    main()