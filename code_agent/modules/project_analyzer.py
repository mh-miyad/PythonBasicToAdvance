"""
Project Analyzer Module

This module analyzes a project's structure and code patterns.
It creates a summary of the project and extracts patterns for the knowledge base.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict, Counter

class ProjectAnalyzer:
    """Analyzes a project's structure and code patterns"""

    def __init__(self, project_path):
        """Initialize the analyzer with the project path"""
        self.project_path = project_path
        self.file_extensions = {
            '.html': 'HTML',
            '.htm': 'HTML',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.sass': 'SASS',
            '.less': 'LESS',
            '.js': 'JavaScript',
            '.jsx': 'React',
            '.ts': 'TypeScript',
            '.tsx': 'React TypeScript',
            '.json': 'JSON',
            '.md': 'Markdown',
            '.py': 'Python',
            '.php': 'PHP',
            '.rb': 'Ruby',
            '.java': 'Java',
            '.c': 'C',
            '.cpp': 'C++',
            '.h': 'C/C++ Header',
            '.cs': 'C#',
            '.go': 'Go',
            '.rs': 'Rust',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.xml': 'XML',
            '.yml': 'YAML',
            '.yaml': 'YAML',
            '.toml': 'TOML',
            '.ini': 'INI',
            '.cfg': 'Config',
            '.conf': 'Config',
            '.sh': 'Shell',
            '.bat': 'Batch',
            '.ps1': 'PowerShell'
        }

        # Initialize data structures for analysis
        self.file_count = 0
        self.directory_count = 0
        self.file_types = Counter()
        self.file_sizes = {}
        self.directory_structure = {}
        self.code_patterns = {
            'HTML': {
                'elements': Counter(),
                'classes': Counter(),
                'ids': Counter(),
                'frameworks': set(),
                'patterns': []
            },
            'CSS': {
                'selectors': Counter(),
                'properties': Counter(),
                'media_queries': Counter(),
                'frameworks': set(),
                'patterns': []
            },
            'JavaScript': {
                'functions': Counter(),
                'classes': Counter(),
                'imports': Counter(),
                'frameworks': set(),
                'patterns': []
            }
        }

    def analyze_project(self):
        """Analyze the project structure and create a summary"""
        print(f"Analyzing project at {self.project_path}...")

        # Reset counters
        self.file_count = 0
        self.directory_count = 0
        self.file_types = Counter()
        self.file_sizes = {}
        self.directory_structure = self._analyze_directory(self.project_path)

        # Create a summary
        summary = self._create_summary()
        return summary

    def _analyze_directory(self, directory, rel_path=""):
        """Recursively analyze a directory and its contents"""
        result = {
            'name': os.path.basename(directory),
            'type': 'directory',
            'children': []
        }

        try:
            items = os.listdir(directory)
            self.directory_count += 1

            for item in items:
                item_path = os.path.join(directory, item)
                item_rel_path = os.path.join(rel_path, item) if rel_path else item

                # Skip hidden files and directories
                if item.startswith('.'):
                    continue

                # Skip node_modules, venv, and other common directories to ignore
                if item in ['node_modules', 'venv', 'env', '__pycache__', '.git']:
                    continue

                if os.path.isdir(item_path):
                    # Recursively analyze subdirectory
                    child = self._analyze_directory(item_path, item_rel_path)
                    result['children'].append(child)
                else:
                    # Analyze file
                    self.file_count += 1
                    file_size = os.path.getsize(item_path)
                    self.file_sizes[item_rel_path] = file_size

                    # Determine file type
                    _, ext = os.path.splitext(item)
                    file_type = self.file_extensions.get(ext.lower(), 'Unknown')
                    self.file_types[file_type] += 1

                    # Add file to directory structure
                    result['children'].append({
                        'name': item,
                        'type': 'file',
                        'file_type': file_type,
                        'size': file_size
                    })
        except Exception as e:
            print(f"Error analyzing directory {directory}: {e}")

        return result

    def _create_summary(self):
        """Create a summary of the project"""
        summary = f"Project Summary for {os.path.basename(self.project_path)}\n"
        summary += "=" * 50 + "\n\n"

        # Basic statistics
        summary += "Basic Statistics:\n"
        summary += f"- Total files: {self.file_count}\n"
        summary += f"- Total directories: {self.directory_count}\n"

        # File types
        summary += "\nFile Types:\n"
        for file_type, count in self.file_types.most_common():
            summary += f"- {file_type}: {count} files\n"

        # Largest files
        summary += "\nLargest Files:\n"
        largest_files = sorted(self.file_sizes.items(), key=lambda x: x[1], reverse=True)[:10]
        for file_path, size in largest_files:
            size_kb = size / 1024
            summary += f"- {file_path}: {size_kb:.2f} KB\n"

        # Directory structure
        summary += "\nDirectory Structure:\n"
        summary += self._format_directory_structure(self.directory_structure)

        return summary

    def _format_directory_structure(self, directory, indent=0):
        """Format the directory structure as a string"""
        result = ""

        # Add the directory name
        if indent > 0:  # Skip for the root directory
            result += "  " * indent + f"- {directory['name']}/\n"

        # Add the children
        for child in sorted(directory['children'], key=lambda x: (x['type'] != 'directory', x['name'])):
            if child['type'] == 'directory':
                result += self._format_directory_structure(child, indent + 1)
            else:
                result += "  " * (indent + 1) + f"- {child['name']} ({child['file_type']})\n"

        return result

    def extract_code_patterns(self):
        """Extract code patterns from the project files"""
        print("Extracting code patterns...")

        # Reset patterns
        self.code_patterns = {
            'HTML': {
                'elements': Counter(),
                'classes': Counter(),
                'ids': Counter(),
                'frameworks': set(),
                'patterns': []
            },
            'CSS': {
                'selectors': Counter(),
                'properties': Counter(),
                'media_queries': Counter(),
                'frameworks': set(),
                'patterns': []
            },
            'JavaScript': {
                'functions': Counter(),
                'classes': Counter(),
                'imports': Counter(),
                'frameworks': set(),
                'patterns': []
            }
        }

        # Walk through the project files
        for root, _, files in os.walk(self.project_path):
            # Skip hidden directories and common directories to ignore
            if any(part.startswith('.') for part in root.split(os.sep)):
                continue
            if any(part in ['node_modules', 'venv', 'env', '__pycache__'] for part in root.split(os.sep)):
                continue

            for file in files:
                # Skip hidden files
                if file.startswith('.'):
                    continue

                file_path = os.path.join(root, file)
                _, ext = os.path.splitext(file)

                try:
                    # Process based on file type
                    if ext.lower() in ['.html', '.htm']:
                        self._analyze_html_file(file_path)
                    elif ext.lower() in ['.css', '.scss', '.sass', '.less']:
                        self._analyze_css_file(file_path)
                    elif ext.lower() in ['.js', '.jsx', '.ts', '.tsx']:
                        self._analyze_js_file(file_path)
                except Exception as e:
                    print(f"Error analyzing file {file_path}: {e}")

        # Detect frameworks
        self._detect_frameworks()

        return self.code_patterns

    def _analyze_html_file(self, file_path):
        """Analyze an HTML file for patterns"""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Extract HTML elements
        element_pattern = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)[^>]*>')
        for match in element_pattern.finditer(content):
            element = match.group(1).lower()
            self.code_patterns['HTML']['elements'][element] += 1

        # Extract classes
        class_pattern = re.compile(r'class=["\']([^"\']+)["\']')
        for match in class_pattern.finditer(content):
            classes = match.group(1).split()
            for cls in classes:
                self.code_patterns['HTML']['classes'][cls] += 1

        # Extract IDs
        id_pattern = re.compile(r'id=["\']([^"\']+)["\']')
        for match in id_pattern.finditer(content):
            id_value = match.group(1)
            self.code_patterns['HTML']['ids'][id_value] += 1

        # Look for common patterns
        if '<div class="container">' in content:
            self.code_patterns['HTML']['patterns'].append('Bootstrap container')
        if '<div class="row">' in content:
            self.code_patterns['HTML']['patterns'].append('Bootstrap grid')
        if '<nav class="navbar">' in content:
            self.code_patterns['HTML']['patterns'].append('Bootstrap navbar')

    def _analyze_css_file(self, file_path):
        """Analyze a CSS file for patterns"""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Extract selectors
        selector_pattern = re.compile(r'([^{]+){[^}]*}')
        for match in selector_pattern.finditer(content):
            selector = match.group(1).strip()
            self.code_patterns['CSS']['selectors'][selector] += 1

        # Extract properties
        property_pattern = re.compile(r'([a-zA-Z-]+)\s*:\s*([^;]+);')
        for match in property_pattern.finditer(content):
            prop = match.group(1).strip()
            value = match.group(2).strip()
            self.code_patterns['CSS']['properties'][f"{prop}: {value}"] += 1

        # Extract media queries
        media_pattern = re.compile(r'@media\s+([^{]+){')
        for match in media_pattern.finditer(content):
            query = match.group(1).strip()
            self.code_patterns['CSS']['media_queries'][query] += 1

        # Look for common patterns
        if '.container' in content:
            self.code_patterns['CSS']['patterns'].append('Container class')
        if 'display: flex' in content:
            self.code_patterns['CSS']['patterns'].append('Flexbox layout')
        if 'display: grid' in content:
            self.code_patterns['CSS']['patterns'].append('Grid layout')

    def _analyze_js_file(self, file_path):
        """Analyze a JavaScript file for patterns"""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Extract functions
        function_pattern = re.compile(r'function\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\(')
        for match in function_pattern.finditer(content):
            func_name = match.group(1)
            self.code_patterns['JavaScript']['functions'][func_name] += 1

        # Extract arrow functions
        arrow_func_pattern = re.compile(r'(const|let|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*=\s*\([^)]*\)\s*=>')
        for match in arrow_func_pattern.finditer(content):
            func_name = match.group(2)
            self.code_patterns['JavaScript']['functions'][func_name] += 1

        # Extract classes
        class_pattern = re.compile(r'class\s+([a-zA-Z_$][a-zA-Z0-9_$]*)')
        for match in class_pattern.finditer(content):
            class_name = match.group(1)
            self.code_patterns['JavaScript']['classes'][class_name] += 1

        # Extract imports
        import_pattern = re.compile(r'import\s+(?:{[^}]*}|[a-zA-Z_$][a-zA-Z0-9_$]*)\s+from\s+[\'"]([^\'"]+)[\'"]')
        for match in import_pattern.finditer(content):
            module = match.group(1)
            self.code_patterns['JavaScript']['imports'][module] += 1

        # Look for common patterns
        if 'document.querySelector' in content:
            self.code_patterns['JavaScript']['patterns'].append('DOM manipulation')
        if 'addEventListener' in content:
            self.code_patterns['JavaScript']['patterns'].append('Event listeners')
        if 'fetch(' in content:
            self.code_patterns['JavaScript']['patterns'].append('Fetch API')

    def _detect_frameworks(self):
        """Detect frameworks used in the project"""
        # HTML frameworks
        if self.code_patterns['HTML']['classes'].get('container', 0) > 0 and self.code_patterns['HTML']['classes'].get('row', 0) > 0:
            self.code_patterns['HTML']['frameworks'].add('Bootstrap')

        if self.code_patterns['HTML']['classes'].get('mui', 0) > 0 or self.code_patterns['HTML']['classes'].get('MuiButton', 0) > 0:
            self.code_patterns['HTML']['frameworks'].add('Material-UI')

        # CSS frameworks
        if '.container' in self.code_patterns['CSS']['selectors'] and '.row' in self.code_patterns['CSS']['selectors']:
            self.code_patterns['CSS']['frameworks'].add('Bootstrap')

        if '@tailwind' in ' '.join(self.code_patterns['CSS']['selectors'].keys()):
            self.code_patterns['CSS']['frameworks'].add('Tailwind CSS')

        # JavaScript frameworks
        if 'react' in ' '.join(self.code_patterns['JavaScript']['imports'].keys()):
            self.code_patterns['JavaScript']['frameworks'].add('React')

        if 'vue' in ' '.join(self.code_patterns['JavaScript']['imports'].keys()):
            self.code_patterns['JavaScript']['frameworks'].add('Vue.js')

        if 'angular' in ' '.join(self.code_patterns['JavaScript']['imports'].keys()):
            self.code_patterns['JavaScript']['frameworks'].add('Angular')

        if 'jquery' in ' '.join(self.code_patterns['JavaScript']['imports'].keys()) or '$(' in ' '.join(self.code_patterns['JavaScript']['functions'].keys()):
            self.code_patterns['JavaScript']['frameworks'].add('jQuery')

    def get_code_patterns(self):
        """Get the extracted code patterns"""
        return self.code_patterns
