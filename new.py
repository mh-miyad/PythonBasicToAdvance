import time
import random
import os
import re
import glob
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

# Standard CSS properties and values
CSS_PROPERTIES = {
    "position": ["absolute", "relative", "fixed", "static", "sticky"],
    "display": ["block", "flex", "grid", "inline", "none", "inline-block"],
    "flex-direction": ["row", "column", "row-reverse", "column-reverse"],
    "justify-content": ["center", "flex-start", "flex-end", "space-between", "space-around"],
    "align-items": ["center", "flex-start", "flex-end", "stretch", "baseline"],
    "gap": ["10px", "20px", "1rem", "2rem"],
    "color": ["red", "blue", "green", "#fff", "#000", "rgba(0,0,0,0.5)"],
    "background": ["#fff", "#f5f5f5", "transparent", "url(...)"],
    "margin": ["0", "10px", "1rem", "auto"],
    "padding": ["0", "10px", "1rem", "2em"],
    "width": ["100%", "auto", "50%", "300px"],
    "height": ["100%", "auto", "50vh", "200px"],
    "font-size": ["16px", "1rem", "1.2em", "larger"],
    "font-weight": ["normal", "bold", "400", "700"],
    "text-align": ["left", "center", "right", "justify"],
    "border": ["none", "1px solid black", "2px dashed red"],
    "border-radius": ["0", "5px", "50%", "10px"],
}

# Class to learn from existing CSS files
class CSSLearner:
    def __init__(self):
        self.properties = dict(CSS_PROPERTIES)  # Start with standard properties
        self.selectors = []
        self.property_frequencies = {}  # Track how often properties are used
        self.selector_properties = {}   # Track which properties are used with which selectors

    def scan_css_files(self, directory="."):
        """Scan all CSS files in the directory and its subdirectories"""
        print(f"Scanning CSS files in {os.path.abspath(directory)}...")

        # Find all CSS files
        css_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.css'):
                    css_files.append(os.path.join(root, file))

        print(f"Found {len(css_files)} CSS files")

        # Process each CSS file
        for css_file in css_files:
            self.process_css_file(css_file)

        print(f"Learned {len(self.selectors)} unique selectors")
        print(f"Learned {len(self.properties)} properties")

    def process_css_file(self, file_path):
        """Extract CSS knowledge from a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract selectors and their properties
            # This is a simple parser and might not handle all CSS syntax correctly
            selector_blocks = re.findall(r'([^{]+)\s*{([^}]+)}', content)

            for selector, properties_block in selector_blocks:
                selector = selector.strip()
                if selector not in self.selectors:
                    self.selectors.append(selector)

                # Extract individual properties
                properties = re.findall(r'([a-zA-Z-]+)\s*:\s*([^;]+);', properties_block)

                # Store which properties are used with this selector
                if selector not in self.selector_properties:
                    self.selector_properties[selector] = []

                for prop, value in properties:
                    prop = prop.strip()
                    value = value.strip()

                    # Update property frequencies
                    if prop not in self.property_frequencies:
                        self.property_frequencies[prop] = 0
                    self.property_frequencies[prop] += 1

                    # Add to selector properties
                    if prop not in self.selector_properties[selector]:
                        self.selector_properties[selector].append(prop)

                    # Add to known properties and values
                    if prop not in self.properties:
                        self.properties[prop] = []

                    if value not in self.properties[prop]:
                        self.properties[prop].append(value)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    def get_common_properties(self, limit=10):
        """Get the most commonly used properties"""
        sorted_props = sorted(self.property_frequencies.items(),
                             key=lambda x: x[1], reverse=True)
        return [prop for prop, _ in sorted_props[:limit]]

    def get_properties_for_selector(self, selector):
        """Get properties commonly used with a specific selector"""
        # Try to find an exact match
        if selector in self.selector_properties:
            return self.selector_properties[selector]

        # Try to find a similar selector (e.g., both are classes or IDs)
        selector_type = self._get_selector_type(selector)
        similar_selectors = [s for s in self.selector_properties.keys()
                            if self._get_selector_type(s) == selector_type]

        if similar_selectors:
            # Combine properties from similar selectors
            properties = []
            for s in similar_selectors:
                properties.extend(self.selector_properties[s])
            return list(set(properties))  # Remove duplicates

        # Fallback to common properties
        return self.get_common_properties()

    def _get_selector_type(self, selector):
        """Determine the type of selector (class, id, element, etc.)"""
        selector = selector.strip()
        if selector.startswith('.'):
            return 'class'
        elif selector.startswith('#'):
            return 'id'
        elif '::' in selector:
            return 'pseudo-element'
        elif ':' in selector:
            return 'pseudo-class'
        else:
            return 'element'

    def get_value_for_property(self, property_name):
        """Get a likely value for a property"""
        if property_name in self.properties and self.properties[property_name]:
            return random.choice(self.properties[property_name])
        return ""

# Class to simulate human typing with CSS intelligence
class CSSTyper:
    def __init__(self, css_learner):
        self.learner = css_learner
        self.typing_speed = random.uniform(30, 70)  # Words per minute
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

    def select_suggestion(self):
        """Select from the suggestion dropdown"""
        # Wait as if reading suggestions
        time.sleep(random.uniform(0.3, 0.8))

        # Sometimes navigate through suggestions
        if random.random() < 0.4:
            for _ in range(random.randint(1, 3)):
                pyautogui.press('down')
                time.sleep(random.uniform(0.1, 0.3))

        # Accept suggestion
        if random.random() < 0.7:
            pyautogui.press('tab')
        else:
            pyautogui.press('enter')

        time.sleep(random.uniform(0.1, 0.3))

    def type_selector(self):
        """Type a CSS selector"""
        try:
            # Choose a selector
            if self.learner.selectors:
                self.current_selector = random.choice(self.learner.selectors)
            else:
                # Fallback selectors if none were learned
                basic_selectors = [
                    "body", "header", "main", "footer", "nav", ".container", ".header",
                    ".nav", ".main", "#header", "#footer", "#main", "h1", "h2", "p", "a",
                    "button", ".btn", ".card", ".section", "div", "span", "ul", "li"
                ]
                self.current_selector = random.choice(basic_selectors)

            # Type the selector
            self.type_string(self.current_selector)

            # Type opening brace and newline
            self.type_string(" {\n")
            self.used_properties = []
        except Exception as e:
            print(f"Error typing selector: {e}")

    def type_property(self):
        """Type a CSS property with intelligent suggestions"""
        try:
            # Add indentation
            self.type_string("  ")

            # Choose a property that hasn't been used yet for this selector
            if self.current_selector:
                potential_properties = self.learner.get_properties_for_selector(self.current_selector)
                available_properties = [p for p in potential_properties if p not in self.used_properties]

                if not available_properties:
                    # If all selector-specific properties used, choose from common properties
                    available_properties = [p for p in self.learner.get_common_properties()
                                           if p not in self.used_properties]

                if not available_properties:
                    # If still no properties, choose any property
                    available_properties = list(self.learner.properties.keys())
            else:
                # If no selector context, use common properties
                available_properties = self.learner.get_common_properties()

            property_name = random.choice(available_properties)
            self.used_properties.append(property_name)

            # Decide how much of the property to type before triggering suggestions
            if len(property_name) <= 3:
                suggestion_point = len(property_name)  # Type the whole property
            else:
                suggestion_point = random.randint(2, len(property_name) - 1)

            # Type the beginning of the property
            self.type_string(property_name[:suggestion_point])

            # Simulate waiting for suggestions
            time.sleep(random.uniform(0.2, 0.5))

            # If suggestions don't appear automatically, trigger them
            if random.random() < 0.3:  # 30% chance suggestions don't appear
                self.trigger_suggestions()

            # Select from suggestions or continue typing
            if random.random() < 0.8:  # 80% chance to use suggestions
                self.select_suggestion()
            else:
                # Continue typing the rest manually
                self.type_string(property_name[suggestion_point:])

            # Type colon and space
            self.type_string(": ")

            # Choose and type a value
            value = self.learner.get_value_for_property(property_name)
            self.type_string(value)

            # Type semicolon and newline
            self.type_string(";\n")
        except Exception as e:
            print(f"Error typing property: {e}")

    def close_rule(self):
        """Close the current CSS rule"""
        self.type_string("}\n\n")
        self.current_selector = None

    def create_css_rule(self):
        """Create a complete CSS rule"""
        self.type_selector()

        # Add 2-5 properties
        num_properties = random.randint(2, 5)
        for _ in range(num_properties):
            self.type_property()
            time.sleep(random.uniform(0.1, 0.3))

        self.close_rule()
        time.sleep(random.uniform(0.5, 1.0))

    def create_css_file(self, num_rules=None):
        """Create a complete CSS file with multiple rules"""
        if num_rules is None:
            num_rules = random.randint(3, 8)

        for _ in range(num_rules):
            self.create_css_rule()

            # Occasionally add a comment
            if random.random() < 0.2:
                self.type_string("/* ")
                comments = [
                    "Main navigation styles",
                    "Header section",
                    "Footer styles",
                    "Card component",
                    "Button styles",
                    "Responsive adjustments",
                    "TODO: Fix alignment issues",
                    "Media query for mobile"
                ]
                self.type_string(random.choice(comments))
                self.type_string(" */\n\n")

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
    # Initialize the CSS learner and scan existing files
    learner = CSSLearner()
    learner.scan_css_files()

    # Initialize the CSS typer
    typer = CSSTyper(learner)

    print("Ready to start typing. Please focus your cursor in a CSS file.")
    print("Press Ctrl+C in the terminal to stop the script.")
    print("You have 10 seconds to position your cursor...")

    # Countdown
    for i in range(10, 0, -1):
        print(f"{i}...", end="\r")
        time.sleep(1)
    print("Starting!      ")

    try:
        while True:
            # Get current mouse position (where the user positioned it)
            current_x, current_y = pyautogui.position()

            # Click to ensure focus
            pyautogui.click()
            time.sleep(0.5)

            # Create CSS content
            num_rules = random.randint(2, 5)
            typer.create_css_file(num_rules)

            # Take a break between sessions
            time.sleep(random.uniform(2, 5))

            # Return to original position
            safe_mouse_move(current_x, current_y)

    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("Script stopped due to an error.")

if __name__ == "__main__":
    main()
