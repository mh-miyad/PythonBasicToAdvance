"""
Task Executor Module

This module executes tasks by parsing task descriptions and using the code writer
to generate the required code.
"""

import os
import re
import json
import time
from pathlib import Path

# Try to import the WebSearchHandler
try:
    from .web_search_handler import WebSearchHandler
except ImportError:
    try:
        from web_search_handler import WebSearchHandler
    except ImportError:
        # Create a dummy WebSearchHandler class if the import fails
        print("Warning: WebSearchHandler module could not be imported.")
        print("Creating a dummy implementation.")

        class WebSearchHandler:
            def __init__(self, vs_code_controller):
                self.vs_code = vs_code_controller
                print("WebSearchHandler initialized with dummy implementation.")

            def implement_figma_card_layout(self, file_path):
                print(f"Would implement Figma card layout in {file_path}")
                return True

            def implement_dashboard_layout(self, file_path):
                print(f"Would implement dashboard layout in {file_path}")
                return True

class TaskExecutor:
    """Executes tasks by parsing task descriptions and generating code"""

    def __init__(self, project_path, tasks_path, code_writer, vs_code_controller):
        """Initialize the task executor with the project path and code writer"""
        self.project_path = project_path
        self.tasks_path = tasks_path
        self.code_writer = code_writer
        self.vs_code = vs_code_controller
        self.web_search_handler = WebSearchHandler(vs_code_controller)

        # Create the tasks directory if it doesn't exist
        os.makedirs(tasks_path, exist_ok=True)

    def execute_task(self, task_file):
        """Execute a task from a task file"""
        print(f"Executing task from {task_file}...")

        # Read the task description
        with open(task_file, 'r') as f:
            task_description = f.read()

        # Parse the task description
        task = self._parse_task(task_description)

        # Execute the task
        if task['type'] == 'create_file':
            self._create_file_task(task)
        elif task['type'] == 'modify_file':
            self._modify_file_task(task)
        elif task['type'] == 'delete_file':
            self._delete_file_task(task)
        elif task['type'] == 'web_search_implement':
            self._web_search_implement_task(task)
        else:
            print(f"Unknown task type: {task['type']}")
            # Try to handle it as a file creation task with default values
            if 'card' in task_description.lower() or 'layout' in task_description.lower():
                print("Attempting to handle as a card layout implementation task...")
                default_task = {
                    'type': 'web_search_implement',
                    'website': 'figma.com',
                    'component': 'card layout',
                    'file_type': 'HTML',
                    'file_path': 'index.html',
                    'description': task_description
                }
                self._web_search_implement_task(default_task)

        print(f"Task execution completed")

    def _parse_task(self, task_description):
        """Parse a task description to determine the task type and details"""
        # This is a simplified implementation
        # In a real implementation, you would use NLP techniques to parse the task

        task = {
            'description': task_description,
            'type': 'unknown'
        }

        # Check for web search and implementation tasks
        if ('search' in task_description.lower() and 'figma' in task_description.lower()) or \
           ('search' in task_description.lower() and 'website' in task_description.lower()) or \
           ('figma' in task_description.lower() and 'card' in task_description.lower()) or \
           ('figma' in task_description.lower() and 'layout' in task_description.lower()):
            task['type'] = 'web_search_implement'
            task['website'] = 'figma.com'

            # Determine the component
            if 'card' in task_description.lower():
                task['component'] = 'card layout'
            elif 'dashboard' in task_description.lower():
                task['component'] = 'dashboard layout'
            else:
                task['component'] = 'layout'

            # Set the file type and path
            task['file_type'] = 'HTML'
            task['file_path'] = 'index.html'

            return task

        # Check for file creation tasks
        create_match = re.search(r'create\s+(?:a\s+)?(?:new\s+)?file\s+(?:named\s+)?[\'"]?([^\'"]+)[\'"]?', task_description, re.IGNORECASE)
        if create_match:
            task['type'] = 'create_file'
            task['file_path'] = create_match.group(1)

            # Determine the file type
            _, ext = os.path.splitext(task['file_path'])
            ext = ext.lower()

            if ext in ['.html', '.htm']:
                task['file_type'] = 'HTML'
            elif ext in ['.css', '.scss', '.sass', '.less']:
                task['file_type'] = 'CSS'
            elif ext in ['.js', '.jsx']:
                task['file_type'] = 'JavaScript'
            else:
                task['file_type'] = 'Unknown'

            return task

        # Check for file modification tasks
        modify_match = re.search(r'modify\s+(?:the\s+)?file\s+(?:named\s+)?[\'"]?([^\'"]+)[\'"]?', task_description, re.IGNORECASE)
        if modify_match:
            task['type'] = 'modify_file'
            task['file_path'] = modify_match.group(1)
            return task

        # Check for file deletion tasks
        delete_match = re.search(r'delete\s+(?:the\s+)?file\s+(?:named\s+)?[\'"]?([^\'"]+)[\'"]?', task_description, re.IGNORECASE)
        if delete_match:
            task['type'] = 'delete_file'
            task['file_path'] = delete_match.group(1)
            return task

        # If no specific task type is detected, try to infer from context
        if 'dashboard' in task_description.lower() and 'js' in task_description.lower():
            task['type'] = 'create_file'
            task['file_type'] = 'JavaScript'
            task['file_path'] = 'dashboard.js'
            return task
        elif 'dashboard' in task_description.lower() and 'css' in task_description.lower():
            task['type'] = 'create_file'
            task['file_type'] = 'CSS'
            task['file_path'] = 'dashboard.css'
            return task
        elif 'dashboard' in task_description.lower():
            task['type'] = 'create_file'
            task['file_type'] = 'HTML'
            task['file_path'] = 'dashboard.html'
            return task
        elif 'html' in task_description.lower():
            task['type'] = 'create_file'
            task['file_type'] = 'HTML'
            task['file_path'] = 'index.html'
            return task
        elif 'css' in task_description.lower():
            task['type'] = 'create_file'
            task['file_type'] = 'CSS'
            task['file_path'] = 'styles.css'
            return task
        elif 'javascript' in task_description.lower() or 'js' in task_description.lower():
            task['type'] = 'create_file'
            task['file_type'] = 'JavaScript'
            task['file_path'] = 'script.js'
            return task
        elif 'card' in task_description.lower() or 'layout' in task_description.lower():
            task['type'] = 'web_search_implement'
            task['website'] = 'figma.com'
            task['component'] = 'card layout'
            task['file_type'] = 'HTML'
            task['file_path'] = 'index.html'
            return task

        return task

    def _create_file_task(self, task):
        """Execute a file creation task"""
        file_path = task['file_path']

        # If the path is not absolute, make it relative to the project path
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.project_path, file_path)

        # Create the file
        self.code_writer.create_file(file_path, task['file_type'], task['description'])

    def _modify_file_task(self, task):
        """Execute a file modification task"""
        file_path = task['file_path']

        # If the path is not absolute, make it relative to the project path
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.project_path, file_path)

        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist")
            return

        # Open the file in VS Code
        self.vs_code.open_file(file_path)

        # Determine the file type
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()

        if ext in ['.html', '.htm']:
            file_type = 'HTML'
        elif ext in ['.css', '.scss', '.sass', '.less']:
            file_type = 'CSS'
        elif ext in ['.js', '.jsx']:
            file_type = 'JavaScript'
        else:
            file_type = 'Unknown'

        # Parse the task description to determine what to modify
        if 'add' in task['description'].lower():
            # Add content to the file
            if file_type == 'HTML':
                # Find the body tag
                self.vs_code.search_in_file('<body>')
                self.vs_code.type_string("\n  <!-- Added content -->\n")
                self._parse_html_content(task['description'])
            elif file_type == 'CSS':
                # Go to the end of the file
                self.vs_code.type_string("\n/* Added styles */\n")
                self._parse_css_content(task['description'])
            elif file_type == 'JavaScript':
                # Go to the end of the file
                self.vs_code.type_string("\n// Added functionality\n")
                self._parse_js_content(task['description'])
        elif 'replace' in task['description'].lower():
            # Replace content in the file
            match = re.search(r'replace\s+[\'"]([^\'"]+)[\'"](?:\s+with\s+[\'"]([^\'"]+)[\'"])?', task['description'], re.IGNORECASE)
            if match:
                search_text = match.group(1)
                replace_text = match.group(2) if match.group(2) else ''
                self.vs_code.replace_in_file(search_text, replace_text)

        # Save the file
        self.vs_code.save_file()

    def _delete_file_task(self, task):
        """Execute a file deletion task"""
        file_path = task['file_path']

        # If the path is not absolute, make it relative to the project path
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.project_path, file_path)

        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist")
            return

        # Delete the file
        try:
            os.remove(file_path)
            print(f"Deleted file {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

    def _web_search_implement_task(self, task):
        """Execute a web search and implementation task"""
        print(f"Executing web search and implementation task: {task['website']} - {task['component']}")

        file_path = task['file_path']

        # If the path is not absolute, make it relative to the project path
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.project_path, file_path)

        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Create an empty file
            with open(file_path, 'w') as f:
                if task['file_type'] == 'HTML':
                    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

</body>
</html>""")
                else:
                    f.write("")

        # Implement the design based on the website and component
        if task['website'].lower() == 'figma.com' and 'card' in task['component'].lower():
            self.web_search_handler.implement_figma_card_layout(file_path)
        elif task['website'].lower() == 'figma.com' and 'dashboard' in task['component'].lower():
            self.web_search_handler.implement_dashboard_layout(file_path)
        else:
            print(f"No implementation available for {task['website']} - {task['component']}")
            # Default to card layout
            self.web_search_handler.implement_figma_card_layout(file_path)

    def _parse_html_content(self, description):
        """Parse the task description to determine what HTML content to add"""
        # This is a simplified implementation
        # In a real implementation, you would use NLP techniques to parse the task

        if 'heading' in description.lower():
            self.vs_code.type_html_element('h1', content='New Heading')
            self.vs_code.type_string("\n")

        if 'paragraph' in description.lower():
            self.vs_code.type_html_element('p', content='New paragraph text.')
            self.vs_code.type_string("\n")

        if 'list' in description.lower():
            self.vs_code.type_string("<ul>\n")
            self.vs_code.type_string("  <li>Item 1</li>\n")
            self.vs_code.type_string("  <li>Item 2</li>\n")
            self.vs_code.type_string("  <li>Item 3</li>\n")
            self.vs_code.type_string("</ul>\n")

    def _parse_css_content(self, description):
        """Parse the task description to determine what CSS content to add"""
        # This is a simplified implementation
        # In a real implementation, you would use NLP techniques to parse the task

        if 'body' in description.lower():
            self.vs_code.type_css_rule('body', {
                'font-family': 'Arial, sans-serif',
                'margin': '0',
                'padding': '0'
            })

        if 'container' in description.lower():
            self.vs_code.type_css_rule('.container', {
                'max-width': '1200px',
                'margin': '0 auto',
                'padding': '20px'
            })

    def _parse_js_content(self, description):
        """Parse the task description to determine what JavaScript content to add"""
        # This is a simplified implementation
        # In a real implementation, you would use NLP techniques to parse the task

        if 'function' in description.lower():
            self.vs_code.type_js_function('newFunction', ['param1', 'param2'], 'console.log("New function called");\nreturn param1 + param2;')

        if 'event' in description.lower():
            self.vs_code.type_string("document.addEventListener('DOMContentLoaded', function() {\n")
            self.vs_code.type_string("  console.log('DOM fully loaded');\n")
            self.vs_code.type_string("});\n")

    def create_task_file(self, task_description):
        """Create a new task file with the given description"""
        # Find the next available task number
        task_number = 1
        while True:
            task_file = os.path.join(self.tasks_path, f"task{task_number}.txt")
            if not os.path.exists(task_file):
                break
            task_number += 1

        # Write the task description to the file
        with open(task_file, 'w') as f:
            f.write(task_description)

        print(f"Created task file {task_file}")
        return task_file
