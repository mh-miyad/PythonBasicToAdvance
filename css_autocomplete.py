import time
import random
import os
import sys

# Check if pyautogui is installed, if not provide instructions
try:
    import pyautogui
    # Disable fail-safe (with warning)
    print("WARNING: Disabling PyAutoGUI fail-safe. Press Ctrl+C to stop the script if needed.")
    pyautogui.FAILSAFE = False
except ImportError:
    print("Error: The 'pyautogui' module is not installed.")
    print("Please install it by running: pip install pyautogui")
    print("\nAfter installing, run this script again.")
    sys.exit(1)

# CSS selectors and properties from your existing CSS
CSS_SELECTORS = [
    "body", "header", "main", "footer", "nav", ".container", ".header",
    ".nav", ".main", "#header", "#footer", "#main", "h1", "h2", "p", "a",
    "button", ".btn", ".card", ".section", "div", "span", "ul", "li",
    ".card h2", ".nav a", ".footer p"
]

CSS_PROPERTIES = {
    "margin-top": ["0", "10px", "1rem", "auto"],
    "color": ["#333", "#007bff", "#fff", "red"],
    "gap": ["10px", "20px", "1rem", "2rem"],
    "flex-direction": ["row", "column", "row-reverse"],
    "display": ["flex", "block", "grid", "inline-block"],
    "padding": ["10px", "20px", "1rem", "0"],
    "background-color": ["#fff", "#f5f5f5", "#007bff"],
    "font-size": ["16px", "1.2rem", "14px"],
    "text-align": ["center", "left", "right"],
    "border-radius": ["5px", "10px", "50%"],
    "margin": ["0", "10px", "auto", "1rem"],
    "width": ["100%", "auto", "300px"],
    "height": ["auto", "100%", "50px"]
}

class CSSTyper:
    """Class to simulate human typing with CSS intelligence"""

    def __init__(self):
        self.typing_speed = random.uniform(40, 80)  # Words per minute
        self.current_selector = None
        self.used_properties = []

    def type_character(self, char, speed_factor=1.0):
        """Type a single character with human-like timing"""
        pyautogui.typewrite(char)
        delay = (60 / (self.typing_speed * 5)) * speed_factor  # 5 chars per word
        time.sleep(delay + random.uniform(0.01, 0.05))

    def type_string(self, text, speed_factor=1.0):
        """Type a string character by character"""
        for char in text:
            self.type_character(char, speed_factor)

    def trigger_suggestions(self):
        """Trigger code suggestions with Ctrl+Space"""
        pyautogui.hotkey('ctrl', 'space')
        time.sleep(random.uniform(0.2, 0.5))

    def type_selector_with_autocomplete(self):
        """Type a CSS selector and let VS Code auto-complete the braces"""
        # Choose a selector
        self.current_selector = random.choice(CSS_SELECTORS)

        # Type the selector
        self.type_string(self.current_selector)

        # Type space and opening brace - VS Code will auto-complete with closing brace
        self.type_character(' ')
        self.type_character('{')

        # VS Code auto-completes to "{}" - wait briefly
        time.sleep(random.uniform(0.1, 0.3))

        # In VS Code, the cursor is now between the braces
        # Press Enter to create a new line and get proper indentation
        pyautogui.press('enter')

        # VS Code should auto-indent the new line
        # No need to manually add indentation in the next step
        self.used_properties = []

    def type_property_with_autocomplete(self):
        """Type a CSS property with intelligent suggestions"""
        # VS Code should have auto-indented after pressing Enter
        # Choose a property that hasn't been used yet for this selector
        available_properties = [p for p in CSS_PROPERTIES.keys() if p not in self.used_properties]
        if not available_properties:
            available_properties = list(CSS_PROPERTIES.keys())

        property_name = random.choice(available_properties)
        self.used_properties.append(property_name)

        # Type the first few characters of the property
        chars_to_type = random.randint(2, len(property_name) - 1)
        self.type_string(property_name[:chars_to_type])

        # Pause briefly as if waiting for suggestions
        time.sleep(random.uniform(0.2, 0.5))

        # If suggestions don't appear automatically, trigger them
        if random.random() < 0.3:  # 30% chance to need manual trigger
            self.trigger_suggestions()
            time.sleep(random.uniform(0.2, 0.5))

        # Complete the property (either by accepting suggestion or typing)
        if random.random() < 0.7:  # 70% chance to use suggestion
            pyautogui.press('tab')  # Accept suggestion
        else:
            # Type the rest manually
            self.type_string(property_name[chars_to_type:])

        # Type colon - VS Code might auto-add a space after the colon
        self.type_character(':')

        # Sometimes VS Code adds the space automatically, sometimes not
        if random.random() < 0.5:  # 50% chance to need to add space manually
            self.type_character(' ')

        # Choose and type a value
        if property_name in CSS_PROPERTIES:
            value = random.choice(CSS_PROPERTIES[property_name])
            self.type_string(value)

        # Type semicolon
        self.type_character(';')

        # Press Enter to go to next line with auto-indentation
        pyautogui.press('enter')

    def close_rule(self):
        """Close the current CSS rule by moving past the auto-completed closing brace"""
        # VS Code has already added the closing brace when we opened the rule
        # We just need to press End to move to the end of the line
        # This will position the cursor after the closing brace
        pyautogui.press('end')

        # Press Enter for a new line
        pyautogui.press('enter')
        pyautogui.press('enter')  # Add an extra blank line between rules
        self.current_selector = None

    def create_css_rule(self):
        """Create a complete CSS rule with auto-completion"""
        self.type_selector_with_autocomplete()

        # Add 1-3 properties
        num_properties = random.randint(1, 3)
        for _ in range(num_properties):
            self.type_property_with_autocomplete()

        # After typing properties, we need to add the closing brace
        # VS Code has already added it, but we need to navigate to it

        # Press End to move to the end of the current line
        pyautogui.press('end')

        # Press Up to move up to the last property line
        pyautogui.press('up')

        # Press End to move to the end of that line
        pyautogui.press('end')

        # Press Enter to create a new line for the closing brace
        pyautogui.press('enter')

        # VS Code should auto-indent the closing brace
        # Type the closing brace
        self.type_character('}')

        # Add a new line after the rule
        pyautogui.press('enter')
        pyautogui.press('enter')  # Extra blank line

        self.current_selector = None
        time.sleep(random.uniform(0.5, 1.0))

    def create_css_content(self, num_rules=None):
        """Create CSS content with multiple rules"""
        if num_rules is None:
            num_rules = random.randint(2, 5)

        for i in range(num_rules):
            self.create_css_rule()

            # Occasionally add a comment
            if random.random() < 0.2 and i < num_rules - 1:
                self.type_string("/* ")
                comments = ["Header styles", "Navigation", "Main content", "Footer", "Responsive"]
                self.type_string(random.choice(comments))
                self.type_string(" */")
                pyautogui.press('enter')
                pyautogui.press('enter')

def safe_mouse_move(x, y, duration=0.5):
    """Move the mouse safely without triggering the fail-safe"""
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Ensure coordinates are within safe bounds (not at the very edge)
    safe_margin = 10  # pixels from the edge
    x = max(safe_margin, min(x, screen_width - safe_margin))
    y = max(safe_margin, min(y, screen_height - safe_margin))

    # Move the mouse
    pyautogui.moveTo(x, y, duration=duration)

def main():
    # Initialize the CSS typer
    typer = CSSTyper()

    print("\nCSS Auto-completion Simulator")
    print("This script simulates typing CSS with VS Code's auto-completion features.")
    print("\nReady to start. Please focus your cursor in a CSS file.")
    print("Press Ctrl+C in the terminal to stop the script.")
    print("You have 10 seconds to position your cursor...")

    # Countdown
    for i in range(10, 0, -1):
        print(f"{i}...", end="\r")
        time.sleep(1)
    print("Starting!      ")

    try:
        # Get current mouse position (where the user positioned it)
        current_x, current_y = pyautogui.position()

        # Click to ensure focus
        pyautogui.click()
        time.sleep(0.5)

        # Create CSS content
        num_rules = random.randint(2, 4)
        typer.create_css_content(num_rules)

        # Return to original position
        safe_mouse_move(current_x, current_y)

        print("\nTask completed successfully!")

    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("Script stopped due to an error.")

if __name__ == "__main__":
    main()
