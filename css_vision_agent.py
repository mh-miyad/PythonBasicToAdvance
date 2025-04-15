import time
import random
import os
import re
import sys
import glob
import numpy as np

# Check if required modules are installed
missing_modules = []
try:
    import pyautogui
    pyautogui.FAILSAFE = False
except ImportError:
    missing_modules.append("pyautogui")

try:
    import cv2
except ImportError:
    missing_modules.append("opencv-python")

try:
    import pytesseract
except ImportError:
    missing_modules.append("pytesseract")

# If any modules are missing, provide installation instructions
if missing_modules:
    print("Error: The following required modules are not installed:")
    for module in missing_modules:
        print(f"  - {module}")

    print("\nPlease install them by running:")
    print(f"  pip install {' '.join(missing_modules)}")

    if "pytesseract" in missing_modules:
        print("\nNote: pytesseract also requires the Tesseract OCR engine to be installed:")
        print("  - Windows: https://github.com/UB-Mannheim/tesseract/wiki")
        print("  - macOS: brew install tesseract")
        print("  - Linux: apt-get install tesseract-ocr")

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
    "background-color": ["#fff", "#f5f5f5", "transparent", "rgba(0,0,0,0.1)"],
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

# Set path to Tesseract executable
def set_tesseract_path():
    """Set the path to the Tesseract executable based on common installation locations"""
    # Custom installation path - CHANGE THIS TO YOUR INSTALLATION PATH
    custom_path = r'D:\App\tesseract-ocr\tesseract.exe'

    # Check if the custom path exists
    if os.path.exists(custom_path):
        pytesseract.pytesseract.tesseract_cmd = custom_path
        print(f"Using Tesseract from: {custom_path}")
        return True

    # Try common installation paths
    common_paths = [
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        r'D:\Tesseract-OCR\tesseract.exe',
        r'D:\App\Tesseract-OCR\tesseract.exe'
    ]

    for path in common_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            print(f"Using Tesseract from: {path}")
            return True

    # If we get here, Tesseract wasn't found
    print("ERROR: Tesseract OCR not found in common locations.")
    print(f"Please edit the script and set the correct path to tesseract.exe")
    print(f"Current custom path is set to: {custom_path}")
    return False

# Try to set the Tesseract path
tesseract_available = set_tesseract_path()

class ScreenReader:
    """Class for reading and analyzing screen content"""

    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self.ocr_available = tesseract_available

    def take_screenshot(self, region=None):
        """Take a screenshot of the specified region or full screen"""
        if region is None:
            # Full screen
            screenshot = pyautogui.screenshot()
        else:
            # Specified region (x, y, width, height)
            screenshot = pyautogui.screenshot(region=region)

        # Convert to OpenCV format
        return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    def detect_text(self, image, min_conf=70):
        """Detect text in the image using OCR"""
        if not self.ocr_available:
            return "OCR not available - Tesseract not found"

        try:
            # Convert to grayscale for better OCR
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Use pytesseract to extract text
            custom_config = f'--oem 3 --psm 6 -c min_char_confidence={min_conf}'
            text = pytesseract.image_to_string(gray, config=custom_config)

            return text
        except Exception as e:
            print(f"Error in OCR: {e}")
            return ""

    def detect_suggestion_popup(self):
        """Detect if a suggestion popup is visible"""
        if not self.ocr_available:
            # If OCR is not available, assume suggestions are working
            # This is a fallback mode without visual detection
            return True

        try:
            # Get current mouse position
            mouse_x, mouse_y = pyautogui.position()

            # Take screenshot of area below and to the right of cursor
            # (where suggestion popup would typically appear)
            region = (mouse_x, mouse_y, 300, 200)
            screenshot = self.take_screenshot(region)

            # Look for visual cues of a suggestion popup
            # This is a simplified approach - in a real implementation,
            # you might use more sophisticated image recognition

            # Convert to grayscale
            gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

            # Apply threshold to find light areas (suggestion popups are usually light)
            _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

            # Count white pixels
            white_pixel_count = cv2.countNonZero(thresh)

            # If there are many white pixels, it might be a suggestion popup
            return white_pixel_count > (300 * 200 * 0.5)  # 50% of the region is white
        except Exception as e:
            print(f"Error detecting suggestion popup: {e}")
            return False  # Assume no popup on error

    def read_current_line(self):
        """Read the current line of text at cursor position"""
        if not self.ocr_available:
            # If OCR is not available, return empty string
            return ""

        try:
            # Get current mouse position
            mouse_x, mouse_y = pyautogui.position()

            # Take screenshot of area around cursor (current line)
            region = (0, mouse_y - 10, self.screen_width, 20)
            screenshot = self.take_screenshot(region)

            # Extract text
            return self.detect_text(screenshot)
        except Exception as e:
            print(f"Error reading current line: {e}")
            return ""

    def detect_errors(self, text):
        """Detect common CSS syntax errors in the text"""
        if not text or not self.ocr_available:
            return []

        try:
            errors = []

            # Check for double colons
            if "::" in text and "::before" not in text and "::after" not in text:
                errors.append("double_colon")

            # Check for missing semicolons
            if re.search(r':[^;{]*$', text):
                errors.append("missing_semicolon")

            # Check for unclosed brackets
            if text.count('{') != text.count('}'):
                errors.append("unclosed_bracket")

            # Check for property without value
            if re.search(r'[a-zA-Z-]+\s*:\s*$', text):
                errors.append("property_without_value")

            return errors
        except Exception as e:
            print(f"Error detecting errors: {e}")
            return []

class CSSLearner:
    """Class to learn from existing CSS files"""

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

class IntelligentCSSTyper:
    """Class to simulate human typing with CSS intelligence and visual feedback"""

    def __init__(self, css_learner, screen_reader):
        self.learner = css_learner
        self.screen_reader = screen_reader
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

            # After typing a few characters, check for errors
            if random.random() < 0.1:  # 10% chance to check
                current_line = self.screen_reader.read_current_line()
                errors = self.screen_reader.detect_errors(current_line)

                if errors:
                    print(f"Detected errors: {errors}")
                    self.fix_errors(errors)

    def trigger_suggestions(self):
        """Trigger code suggestions with Ctrl+Space"""
        pyautogui.hotkey('ctrl', 'space')
        time.sleep(random.uniform(0.2, 0.5))

        # Check if suggestions appeared
        if not self.screen_reader.detect_suggestion_popup():
            # Try again with a longer wait
            time.sleep(random.uniform(0.5, 1.0))
            if not self.screen_reader.detect_suggestion_popup():
                print("No suggestion popup detected after Ctrl+Space")

    def select_suggestion(self):
        """Select from the suggestion dropdown"""
        # Check if suggestions are visible
        if not self.screen_reader.detect_suggestion_popup():
            self.trigger_suggestions()

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

    def fix_errors(self, errors):
        """Fix detected CSS syntax errors"""
        for error in errors:
            if error == "double_colon":
                # Delete one colon
                pyautogui.press('left')  # Move left
                pyautogui.press('delete')  # Delete the extra colon

            elif error == "missing_semicolon":
                # Add semicolon
                pyautogui.typewrite(';')

            elif error == "unclosed_bracket":
                # Add closing bracket
                pyautogui.typewrite('}')

            elif error == "property_without_value":
                # Add a value
                property_name = re.search(r'([a-zA-Z-]+)\s*:\s*$',
                                         self.screen_reader.read_current_line()).group(1)
                value = self.learner.get_value_for_property(property_name)
                self.type_string(f" {value};")

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

            # Check if suggestions appeared automatically
            if not self.screen_reader.detect_suggestion_popup():
                # If suggestions don't appear automatically, trigger them
                self.trigger_suggestions()

            # Select from suggestions or continue typing
            if self.screen_reader.detect_suggestion_popup():
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

            # Check for errors after typing the property
            current_line = self.screen_reader.read_current_line()
            errors = self.screen_reader.detect_errors(current_line)
            if errors:
                print(f"Detected errors after typing property: {errors}")
                self.fix_errors(errors)

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

    def fix_existing_css(self):
        """Fix errors in existing CSS code"""
        # Read the current screen to detect errors
        screenshot = self.screen_reader.take_screenshot()
        text = self.screen_reader.detect_text(screenshot)

        print("Analyzing existing CSS code...")

        # Split into lines
        lines = text.split('\n')
        current_line_index = 0

        while current_line_index < len(lines):
            line = lines[current_line_index]
            errors = self.screen_reader.detect_errors(line)

            if errors:
                print(f"Found errors in line: {line}")
                print(f"Errors: {errors}")

                # Move to this line (approximate)
                # In a real implementation, you would need more precise cursor positioning
                for _ in range(current_line_index):
                    pyautogui.press('down')

                # Move to the end of the line
                pyautogui.hotkey('end')

                # Fix the errors
                self.fix_errors(errors)

            current_line_index += 1

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
    # Check if Tesseract is available
    if not tesseract_available:
        print("\nWARNING: Tesseract OCR not found. The script will run in limited mode without OCR capabilities.")
        print("Visual error detection and auto-suggestion detection will be disabled.")
        print("\nTo enable full functionality:")
        print("1. Make sure Tesseract OCR is installed")
        print("2. Edit the script to set the correct path to tesseract.exe")
        print("3. Run the script again")

        use_ocr = input("\nDo you want to continue in limited mode? (y/n): ").lower()
        if use_ocr != 'y':
            print("Exiting script.")
            return

    # Initialize the screen reader
    screen_reader = ScreenReader()

    # Initialize the CSS learner and scan existing files
    learner = CSSLearner()
    learner.scan_css_files()

    # Initialize the CSS typer
    typer = IntelligentCSSTyper(learner, screen_reader)

    print("\nCSS Vision Agent initialized.")
    if tesseract_available:
        print("This agent uses computer vision to detect and fix CSS errors.")
    else:
        print("Running in limited mode without OCR capabilities.")

    print("\nOptions:")
    print("1. Create new CSS rules")
    print("2. Fix existing CSS code")
    choice = input("\nEnter your choice (1 or 2): ")

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

        if choice == "2":
            # Fix existing CSS
            typer.fix_existing_css()
        else:
            # Create new CSS content
            num_rules = random.randint(2, 5)
            typer.create_css_file(num_rules)

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
