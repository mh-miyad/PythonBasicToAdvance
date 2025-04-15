"""
VS Code Controller Module

This module controls VS Code to navigate between files, edit files,
and perform other actions like a human would.
"""

import os
import time
import random
import subprocess
import platform
import pyautogui

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False

class VSCodeController:
    """Controls VS Code to navigate and edit files like a human"""

    def __init__(self):
        """Initialize the VS Code controller"""
        self.typing_speed = random.uniform(40, 80)  # Words per minute
        self.current_file = None

    def open_vs_code(self, project_path=None):
        """Open VS Code, optionally with a specific project"""
        system = platform.system()

        try:
            if system == "Windows":
                if project_path:
                    subprocess.Popen(["code", project_path])
                else:
                    subprocess.Popen(["code"])
            elif system == "Darwin":  # macOS
                if project_path:
                    subprocess.Popen(["open", "-a", "Visual Studio Code", project_path])
                else:
                    subprocess.Popen(["open", "-a", "Visual Studio Code"])
            elif system == "Linux":
                if project_path:
                    subprocess.Popen(["code", project_path])
                else:
                    subprocess.Popen(["code"])

            # Wait for VS Code to open
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Error opening VS Code: {e}")
            return False

    def open_file(self, file_path):
        """Open a file in VS Code"""
        # First, try to use keyboard shortcuts to open the file
        self._open_file_with_keyboard(file_path)

        # Update the current file
        self.current_file = file_path

    def _open_file_with_keyboard(self, file_path):
        """Open a file using keyboard shortcuts"""
        # Press Ctrl+P to open the quick open dialog
        pyautogui.hotkey('ctrl', 'p')
        time.sleep(0.5)

        # Type the file name
        file_name = os.path.basename(file_path)
        self.type_string(file_name)
        time.sleep(0.5)

        # Press Enter to open the file
        pyautogui.press('enter')
        time.sleep(0.5)

    def create_new_file(self, file_path):
        """Create a new file in VS Code"""
        # Extract the directory and file name
        directory = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)

        # Make sure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Open the Explorer view
        pyautogui.hotkey('ctrl', 'shift', 'e')
        time.sleep(0.5)

        # Navigate to the directory
        # This is a simplified implementation
        # In a real implementation, you would need to navigate through the directory tree

        # Right-click to open the context menu
        pyautogui.rightClick()
        time.sleep(0.5)

        # Select "New File"
        pyautogui.press('down', presses=5)  # Adjust the number of presses as needed
        pyautogui.press('enter')
        time.sleep(0.5)

        # Type the file name
        self.type_string(file_name)
        pyautogui.press('enter')
        time.sleep(0.5)

        # Update the current file
        self.current_file = file_path

    def type_string(self, text, speed_factor=1.0):
        """Type a string with human-like timing"""
        for char in text:
            self.type_character(char, speed_factor)

    def type_character(self, char, speed_factor=1.0):
        """Type a single character with human-like timing"""
        pyautogui.typewrite(char)
        delay = (60 / (self.typing_speed * 5)) * speed_factor  # 5 chars per word
        time.sleep(delay + random.uniform(0.01, 0.05))

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

    def save_file(self):
        """Save the current file"""
        pyautogui.hotkey('ctrl', 's')
        time.sleep(0.5)

    def close_file(self):
        """Close the current file"""
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)
        self.current_file = None

    def type_html_element(self, element, content=None, attributes=None):
        """Type an HTML element with content and attributes"""
        # Type the opening tag
        self.type_character('<')
        self.type_string(element)

        # Type attributes if provided
        if attributes:
            for attr, value in attributes.items():
                self.type_character(' ')
                self.type_string(attr)
                # Type the equals sign and first quote
                self.type_character('=')
                self.type_character('"')
                # Type the attribute value
                self.type_string(value)
                # Type the closing quote
                self.type_character('"')

        self.type_character('>')

        # Type content if provided
        if content:
            self.type_string(content)

            # Type the closing tag
            self.type_string(f"</{element}>")
        else:
            # Position cursor inside the element
            pyautogui.press('left')
            for _ in range(len(element) + 1):
                pyautogui.press('left')

    def type_css_rule(self, selector, properties):
        """Type a CSS rule with selector and properties"""
        # Type the selector
        self.type_string(selector)
        self.type_string(" {")
        pyautogui.press('enter')

        # Type properties
        for prop, value in properties.items():
            self.type_string("  ")  # Indentation
            self.type_string(prop)
            self.type_string(": ")
            self.type_string(value)
            self.type_string(";")
            pyautogui.press('enter')

        # Close the rule
        self.type_string("}")
        pyautogui.press('enter')

    def type_js_function(self, name, params=None, body=None):
        """Type a JavaScript function"""
        # Type the function declaration
        self.type_string("function ")
        self.type_string(name)
        self.type_character('(')

        # Type parameters if provided
        if params:
            self.type_string(", ".join(params))

        self.type_string(") {")
        pyautogui.press('enter')

        # Type the function body if provided
        if body:
            lines = body.split('\n')
            for line in lines:
                self.type_string("  ")  # Indentation
                self.type_string(line)
                pyautogui.press('enter')

        # Close the function
        self.type_string("}")
        pyautogui.press('enter')

    def simulate_human_behavior(self):
        """Simulate human-like behavior while coding"""
        # Randomly perform some human-like actions
        action = random.choice([
            'pause',
            'scroll',
            'move_cursor',
            'select_text',
            'undo',
            'redo'
        ])

        if action == 'pause':
            # Pause for a moment as if thinking
            time.sleep(random.uniform(1, 3))
        elif action == 'scroll':
            # Scroll up or down
            direction = random.choice(['up', 'down'])
            for _ in range(random.randint(1, 5)):
                pyautogui.scroll(100 if direction == 'up' else -100)
                time.sleep(random.uniform(0.1, 0.3))
        elif action == 'move_cursor':
            # Move the cursor to a random position
            x, y = pyautogui.position()
            new_x = x + random.randint(-100, 100)
            new_y = y + random.randint(-50, 50)
            pyautogui.moveTo(new_x, new_y, duration=random.uniform(0.2, 0.5))
        elif action == 'select_text':
            # Select some text
            pyautogui.keyDown('shift')
            for _ in range(random.randint(1, 10)):
                pyautogui.press('right')
                time.sleep(random.uniform(0.05, 0.1))
            pyautogui.keyUp('shift')
            time.sleep(random.uniform(0.5, 1))
            pyautogui.press('escape')  # Deselect
        elif action == 'undo':
            # Undo an action
            pyautogui.hotkey('ctrl', 'z')
            time.sleep(random.uniform(0.5, 1))
        elif action == 'redo':
            # Redo an action
            pyautogui.hotkey('ctrl', 'y')
            time.sleep(random.uniform(0.5, 1))

    def type_code_from_template(self, template, replacements=None):
        """Type code from a template, with optional replacements"""
        if replacements:
            for key, value in replacements.items():
                template = template.replace(f"{{{key}}}", value)

        # Split the template into lines
        lines = template.split('\n')

        for i, line in enumerate(lines):
            self.type_string(line)

            # Press Enter after each line except the last one
            if i < len(lines) - 1:
                pyautogui.press('enter')

            # Occasionally simulate human behavior
            if random.random() < 0.1:
                self.simulate_human_behavior()

    def search_in_file(self, text):
        """Search for text in the current file"""
        # Press Ctrl+F to open the search dialog
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.5)

        # Type the search text
        self.type_string(text)
        time.sleep(0.5)

        # Press Enter to search
        pyautogui.press('enter')
        time.sleep(0.5)

    def replace_in_file(self, search_text, replace_text):
        """Replace text in the current file"""
        # Press Ctrl+H to open the replace dialog
        pyautogui.hotkey('ctrl', 'h')
        time.sleep(0.5)

        # Type the search text
        self.type_string(search_text)
        time.sleep(0.5)

        # Tab to the replace field
        pyautogui.press('tab')
        time.sleep(0.5)

        # Type the replace text
        self.type_string(replace_text)
        time.sleep(0.5)

        # Press Alt+A to replace all
        pyautogui.hotkey('alt', 'a')
        time.sleep(0.5)
