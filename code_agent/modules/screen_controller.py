"""
Screen Controller Module

This module uses computer vision to interact with the screen,
identify UI elements, and automate actions like clicking, typing, and selecting.
"""

import os
import time
import subprocess
import sys

class ScreenController:
    """Controls the screen using computer vision and automation"""
    
    def __init__(self):
        """Initialize the screen controller"""
        # Check if pyautogui is installed
        try:
            import pyautogui
            self.pyautogui = pyautogui
            self.pyautogui.FAILSAFE = True
            self.has_pyautogui = True
            print("PyAutoGUI is available for screen control")
        except ImportError:
            self.has_pyautogui = False
            print("PyAutoGUI is not installed. Screen control will be limited.")
            print("To enable full screen control, install PyAutoGUI: pip install pyautogui")
    
    def click_element(self, element_name):
        """Click on an element with the given name"""
        if not self.has_pyautogui:
            print(f"Cannot click on {element_name}: PyAutoGUI not installed")
            return False
        
        try:
            # Try to locate the element on screen
            print(f"Looking for element: {element_name}")
            
            # This is a simplified implementation
            # In a real implementation, you would use image recognition or OCR
            # to locate the element on screen
            
            # For now, we'll just simulate finding common elements
            if element_name.lower() == 'explorer':
                self.pyautogui.click(100, 100)
            elif element_name.lower() == 'dist folder':
                self.pyautogui.click(100, 200)
            elif element_name.lower() == 'index.html':
                self.pyautogui.click(200, 200)
            elif element_name.lower() == 'live server':
                self.pyautogui.click(800, 20)
            else:
                print(f"Element not found: {element_name}")
                return False
            
            print(f"Clicked on element: {element_name}")
            return True
        except Exception as e:
            print(f"Error clicking on element {element_name}: {e}")
            return False
    
    def type_text(self, text):
        """Type text at the current cursor position"""
        if not self.has_pyautogui:
            print(f"Cannot type text: PyAutoGUI not installed")
            return False
        
        try:
            self.pyautogui.typewrite(text)
            print(f"Typed text: {text}")
            return True
        except Exception as e:
            print(f"Error typing text: {e}")
            return False
    
    def press_key(self, key):
        """Press a key"""
        if not self.has_pyautogui:
            print(f"Cannot press key: PyAutoGUI not installed")
            return False
        
        try:
            self.pyautogui.press(key)
            print(f"Pressed key: {key}")
            return True
        except Exception as e:
            print(f"Error pressing key: {e}")
            return False
    
    def open_file_in_vscode(self, file_path):
        """Open a file in VS Code"""
        try:
            if sys.platform == 'win32':
                os.system(f'code "{file_path}"')
            else:
                os.system(f'code "{file_path}"')
            print(f"Opened file in VS Code: {file_path}")
            return True
        except Exception as e:
            print(f"Error opening file in VS Code: {e}")
            return False
    
    def start_live_server(self, file_path):
        """Start Live Server for the given file"""
        try:
            # First, open the file in VS Code
            self.open_file_in_vscode(file_path)
            
            # Wait for VS Code to open
            time.sleep(2)
            
            if self.has_pyautogui:
                # Press Alt+L, then Alt+O to start Live Server
                self.pyautogui.hotkey('alt', 'l')
                time.sleep(0.5)
                self.pyautogui.hotkey('alt', 'o')
                print(f"Started Live Server for: {file_path}")
            else:
                print("Cannot start Live Server: PyAutoGUI not installed")
                print("Please start Live Server manually by right-clicking the HTML file and selecting 'Open with Live Server'")
            
            return True
        except Exception as e:
            print(f"Error starting Live Server: {e}")
            return False
    
    def take_screenshot(self, output_path):
        """Take a screenshot and save it to the given path"""
        if not self.has_pyautogui:
            print(f"Cannot take screenshot: PyAutoGUI not installed")
            return False
        
        try:
            screenshot = self.pyautogui.screenshot()
            screenshot.save(output_path)
            print(f"Saved screenshot to: {output_path}")
            return True
        except Exception as e:
            print(f"Error taking screenshot: {e}")
            return False
    
    def find_image_on_screen(self, image_path, confidence=0.7):
        """Find an image on the screen"""
        if not self.has_pyautogui:
            print(f"Cannot find image: PyAutoGUI not installed")
            return None
        
        try:
            location = self.pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                print(f"Found image at: {location}")
                return location
            else:
                print(f"Image not found: {image_path}")
                return None
        except Exception as e:
            print(f"Error finding image: {e}")
            return None
