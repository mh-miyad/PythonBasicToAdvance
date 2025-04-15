"""
Code Writer Module

This module writes code based on the knowledge base and web learning.
It generates HTML, CSS, and JavaScript code based on tasks and existing patterns.
"""

import os
import re
import random
import time
from pathlib import Path

class CodeWriter:
    """Writes code based on the knowledge base and web learning"""

    def __init__(self, knowledge_base, web_learner, vs_code_controller):
        """Initialize the code writer with the knowledge base and web learner"""
        self.knowledge_base = knowledge_base
        self.web_learner = web_learner
        self.vs_code = vs_code_controller

    def create_file(self, file_path, file_type, task_description):
        """Create a new file based on the task description"""
        print(f"Creating {file_type} file: {file_path}")

        # Make sure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Determine the file type based on extension if not provided
        if not file_type:
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

        # Get a template for the file type
        template = self.knowledge_base.get_template(file_type)

        # Create the file with the template content
        if template:
            with open(file_path, 'w') as f:
                f.write(template)

            print(f"Created {file_type} file with template")
        else:
            # Create an empty file
            with open(file_path, 'w') as f:
                pass

            print(f"Created empty {file_type} file")

        # Open the file in VS Code
        self.vs_code.open_file(file_path)

        # Generate code based on the task description
        if file_type == 'HTML':
            self._generate_html(task_description)

            # Also create a matching CSS file if it doesn't exist
            css_file_path = os.path.splitext(file_path)[0] + '.css'
            if not os.path.exists(css_file_path):
                print(f"Creating matching CSS file: {css_file_path}")
                self.vs_code.save_file()  # Save the HTML file first
                self.create_file(css_file_path, 'CSS', task_description)
                self.vs_code.open_file(file_path)  # Go back to the HTML file
        elif file_type == 'CSS':
            self._generate_css(task_description)
        elif file_type == 'JavaScript':
            self._generate_javascript(task_description)

        # Save the file
        self.vs_code.save_file()

        return file_path

    def _generate_html(self, task_description):
        """Generate HTML code based on the task description"""
        print("Generating HTML code...")

        # Check if the task involves Bootstrap
        if 'bootstrap' in task_description.lower():
            self._generate_bootstrap_html(task_description)
            return

        # Parse the task description to identify required elements
        elements = self._parse_html_elements(task_description)

        # Get common HTML patterns from the knowledge base
        patterns = self.knowledge_base.get_common_patterns('HTML', 'patterns')

        # Type the HTML structure
        for element in elements:
            if element['type'] == 'container':
                self.vs_code.type_html_element('div', attributes={'class': 'container'})
                self.vs_code.type_string("\n")
            elif element['type'] == 'heading':
                level = element.get('level', 1)
                self.vs_code.type_html_element(f'h{level}', content=element.get('content', 'Heading'))
                self.vs_code.type_string("\n")
            elif element['type'] == 'paragraph':
                self.vs_code.type_html_element('p', content=element.get('content', 'Paragraph text'))
                self.vs_code.type_string("\n")
            elif element['type'] == 'list':
                self.vs_code.type_html_element('ul', content="\n")
                for item in element.get('items', ['Item 1', 'Item 2', 'Item 3']):
                    self.vs_code.type_string("  ")
                    self.vs_code.type_html_element('li', content=item)
                    self.vs_code.type_string("\n")
                self.vs_code.type_string("</ul>\n")
            elif element['type'] == 'link':
                self.vs_code.type_html_element('a', content=element.get('content', 'Link'),
                                              attributes={'href': element.get('href', '#')})
                self.vs_code.type_string("\n")
            elif element['type'] == 'image':
                self.vs_code.type_html_element('img', attributes={
                    'src': element.get('src', 'image.jpg'),
                    'alt': element.get('alt', 'Image')
                })
                self.vs_code.type_string("\n")
            elif element['type'] == 'form':
                self.vs_code.type_string("<form>\n")
                for field in element.get('fields', [{'type': 'text', 'name': 'name', 'label': 'Name'}]):
                    self.vs_code.type_string("  <div class=\"form-group\">\n")
                    self.vs_code.type_string(f"    <label for=\"{field['name']}\">{field['label']}</label>\n")
                    self.vs_code.type_string(f"    <input type=\"{field['type']}\" id=\"{field['name']}\" name=\"{field['name']}\">\n")
                    self.vs_code.type_string("  </div>\n")
                self.vs_code.type_string("  <button type=\"submit\">Submit</button>\n")
                self.vs_code.type_string("</form>\n")

            # Simulate human behavior occasionally
            if random.random() < 0.2:
                self.vs_code.simulate_human_behavior()

    def _generate_bootstrap_html(self, task_description):
        """Generate Bootstrap HTML code based on the task description"""
        print("Generating Bootstrap HTML code...")

        # Check if we need to include Bootstrap CSS and JS
        self.vs_code.search_in_file('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap')

        # If not found, add Bootstrap CSS and JS
        self.vs_code.search_in_file('</head>')
        self.vs_code.type_string("""  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</head>""")

        # Parse the task description to identify required Bootstrap components
        components = self._parse_bootstrap_components(task_description)

        # Type the Bootstrap components
        for component in components:
            if component['type'] == 'container':
                self.vs_code.type_string("<div class=\"container\">\n")
                self.vs_code.type_string("  <div class=\"row\">\n")
                self.vs_code.type_string("    <div class=\"col\">\n")
                self.vs_code.type_string("      <!-- Content here -->\n")
                self.vs_code.type_string("    </div>\n")
                self.vs_code.type_string("  </div>\n")
                self.vs_code.type_string("</div>\n")
            elif component['type'] == 'card':
                # Try to get a Bootstrap card example from the web
                card_example = self.web_learner.get_bootstrap_example('card')

                if card_example:
                    self.vs_code.type_string(card_example['code'])
                    self.vs_code.type_string("\n")
                else:
                    # Fallback to a basic card
                    self.vs_code.type_string("<div class=\"card\">\n")
                    self.vs_code.type_string("  <div class=\"card-body\">\n")
                    self.vs_code.type_string("    <h5 class=\"card-title\">Card title</h5>\n")
                    self.vs_code.type_string("    <p class=\"card-text\">Some quick example text to build on the card title and make up the bulk of the card's content.</p>\n")
                    self.vs_code.type_string("    <a href=\"#\" class=\"btn btn-primary\">Go somewhere</a>\n")
                    self.vs_code.type_string("  </div>\n")
                    self.vs_code.type_string("</div>\n")
            elif component['type'] == 'navbar':
                # Try to get a Bootstrap navbar example from the web
                navbar_example = self.web_learner.get_bootstrap_example('navbar')

                if navbar_example:
                    self.vs_code.type_string(navbar_example['code'])
                    self.vs_code.type_string("\n")
                else:
                    # Fallback to a basic navbar
                    self.vs_code.type_string("<nav class=\"navbar navbar-expand-lg navbar-light bg-light\">\n")
                    self.vs_code.type_string("  <div class=\"container-fluid\">\n")
                    self.vs_code.type_string("    <a class=\"navbar-brand\" href=\"#\">Navbar</a>\n")
                    self.vs_code.type_string("    <button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#navbarNav\" aria-controls=\"navbarNav\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">\n")
                    self.vs_code.type_string("      <span class=\"navbar-toggler-icon\"></span>\n")
                    self.vs_code.type_string("    </button>\n")
                    self.vs_code.type_string("    <div class=\"collapse navbar-collapse\" id=\"navbarNav\">\n")
                    self.vs_code.type_string("      <ul class=\"navbar-nav\">\n")
                    self.vs_code.type_string("        <li class=\"nav-item\">\n")
                    self.vs_code.type_string("          <a class=\"nav-link active\" aria-current=\"page\" href=\"#\">Home</a>\n")
                    self.vs_code.type_string("        </li>\n")
                    self.vs_code.type_string("        <li class=\"nav-item\">\n")
                    self.vs_code.type_string("          <a class=\"nav-link\" href=\"#\">Features</a>\n")
                    self.vs_code.type_string("        </li>\n")
                    self.vs_code.type_string("        <li class=\"nav-item\">\n")
                    self.vs_code.type_string("          <a class=\"nav-link\" href=\"#\">Pricing</a>\n")
                    self.vs_code.type_string("        </li>\n")
                    self.vs_code.type_string("      </ul>\n")
                    self.vs_code.type_string("    </div>\n")
                    self.vs_code.type_string("  </div>\n")
                    self.vs_code.type_string("</nav>\n")

            # Simulate human behavior occasionally
            if random.random() < 0.2:
                self.vs_code.simulate_human_behavior()

    def _generate_css(self, task_description):
        """Generate CSS code based on the task description"""
        print("Generating CSS code...")

        # Parse the task description to identify required CSS rules
        rules = self._parse_css_rules(task_description)

        # Get common CSS patterns from the knowledge base
        patterns = self.knowledge_base.get_common_patterns('CSS', 'patterns')

        # Get the CSS coding style from the knowledge base
        style = self.knowledge_base.get_coding_style('CSS')

        # Type the CSS rules
        for rule in rules:
            selector = rule['selector']
            properties = rule['properties']

            self.vs_code.type_css_rule(selector, properties)

            # Simulate human behavior occasionally
            if random.random() < 0.2:
                self.vs_code.simulate_human_behavior()

    def _generate_javascript(self, task_description):
        """Generate JavaScript code based on the task description"""
        print("Generating JavaScript code...")

        # Parse the task description to identify required JavaScript functionality
        functions = self._parse_js_functions(task_description)

        # Get common JavaScript patterns from the knowledge base
        patterns = self.knowledge_base.get_common_patterns('JavaScript', 'patterns')

        # Get the JavaScript coding style from the knowledge base
        style = self.knowledge_base.get_coding_style('JavaScript')

        # Type the JavaScript code
        for func in functions:
            name = func['name']
            params = func.get('params', [])
            body = func.get('body', '')

            self.vs_code.type_js_function(name, params, body)

            # Simulate human behavior occasionally
            if random.random() < 0.2:
                self.vs_code.simulate_human_behavior()

    def _parse_html_elements(self, task_description):
        """Parse the task description to identify required HTML elements"""
        elements = []

        # This is a simplified implementation
        # In a real implementation, you would use NLP techniques to parse the task

        # Check for common elements
        if 'container' in task_description.lower():
            elements.append({'type': 'container'})

        if 'heading' in task_description.lower() or 'title' in task_description.lower():
            elements.append({'type': 'heading', 'level': 1, 'content': 'Page Title'})

        if 'paragraph' in task_description.lower() or 'text' in task_description.lower():
            elements.append({'type': 'paragraph', 'content': 'This is a paragraph of text.'})

        if 'list' in task_description.lower():
            elements.append({'type': 'list', 'items': ['Item 1', 'Item 2', 'Item 3']})

        if 'link' in task_description.lower():
            elements.append({'type': 'link', 'content': 'Click here', 'href': '#'})

        if 'image' in task_description.lower():
            elements.append({'type': 'image', 'src': 'image.jpg', 'alt': 'Image'})

        if 'form' in task_description.lower():
            elements.append({
                'type': 'form',
                'fields': [
                    {'type': 'text', 'name': 'name', 'label': 'Name'},
                    {'type': 'email', 'name': 'email', 'label': 'Email'},
                    {'type': 'password', 'name': 'password', 'label': 'Password'}
                ]
            })

        return elements

    def _parse_bootstrap_components(self, task_description):
        """Parse the task description to identify required Bootstrap components"""
        components = []

        # This is a simplified implementation
        # In a real implementation, you would use NLP techniques to parse the task

        # Check for common Bootstrap components
        if 'container' in task_description.lower() or 'layout' in task_description.lower():
            components.append({'type': 'container'})

        if 'card' in task_description.lower():
            components.append({'type': 'card'})

        if 'navbar' in task_description.lower() or 'navigation' in task_description.lower():
            components.append({'type': 'navbar'})

        return components

    def _parse_css_rules(self, task_description):
        """Parse the task description to identify required CSS rules"""
        rules = []

        # This is a simplified implementation
        # In a real implementation, you would use NLP techniques to parse the task

        # Check for common CSS rules
        if 'body' in task_description.lower():
            rules.append({
                'selector': 'body',
                'properties': {
                    'font-family': 'Arial, sans-serif',
                    'margin': '0',
                    'padding': '0',
                    'background-color': '#f5f5f5'
                }
            })

        if 'container' in task_description.lower():
            rules.append({
                'selector': '.container',
                'properties': {
                    'max-width': '1200px',
                    'margin': '0 auto',
                    'padding': '20px'
                }
            })

        if 'header' in task_description.lower():
            rules.append({
                'selector': 'header',
                'properties': {
                    'background-color': '#333',
                    'color': '#fff',
                    'padding': '10px 0'
                }
            })

        if 'footer' in task_description.lower():
            rules.append({
                'selector': 'footer',
                'properties': {
                    'background-color': '#333',
                    'color': '#fff',
                    'padding': '10px 0',
                    'text-align': 'center'
                }
            })

        return rules

    def _parse_js_functions(self, task_description):
        """Parse the task description to identify required JavaScript functions"""
        functions = []

        # This is a simplified implementation
        # In a real implementation, you would use NLP techniques to parse the task

        # Check for common JavaScript functionality
        if 'toggle' in task_description.lower():
            functions.append({
                'name': 'toggleElement',
                'params': ['elementId'],
                'body': 'const element = document.getElementById(elementId);\nif (element) {\n  element.classList.toggle("hidden");\n}'
            })

        if 'form' in task_description.lower() and 'submit' in task_description.lower():
            functions.append({
                'name': 'handleFormSubmit',
                'params': ['event'],
                'body': 'event.preventDefault();\nconst form = event.target;\nconst formData = new FormData(form);\n// Process form data here'
            })

        if 'fetch' in task_description.lower() or 'api' in task_description.lower():
            functions.append({
                'name': 'fetchData',
                'params': ['url'],
                'body': 'return fetch(url)\n  .then(response => response.json())\n  .then(data => {\n    // Process data here\n    return data;\n  })\n  .catch(error => {\n    console.error("Error fetching data:", error);\n  });'
            })

        return functions
