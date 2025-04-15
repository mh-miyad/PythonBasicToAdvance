#!/usr/bin/env python3
"""
Simple Code Agent - A lightweight version that doesn't require external dependencies.

This script analyzes your project structure, creates a summary, and learns from your code
without requiring external dependencies like BeautifulSoup or requests.
"""

import os
import sys
import argparse
import time
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

def analyze_project(project_path):
    """Analyze the project structure and create a summary"""
    print(f"Analyzing project at {project_path}...")
    
    # Initialize counters
    file_count = 0
    directory_count = 0
    file_types = Counter()
    file_sizes = {}
    
    # Walk through the project
    for root, dirs, files in os.walk(project_path):
        # Skip hidden directories and common directories to ignore
        dirs[:] = [d for d in dirs if not d.startswith('.') and 
                  d not in ['node_modules', 'venv', 'env', '__pycache__', 'dist', 'build', '.git']]
        
        directory_count += 1
        
        for file in files:
            # Skip hidden files
            if file.startswith('.'):
                continue
            
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, project_path)
            
            # Count the file
            file_count += 1
            
            # Get the file size
            file_size = os.path.getsize(file_path)
            file_sizes[rel_path] = file_size
            
            # Determine file type
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            
            if ext in ['.html', '.htm']:
                file_type = 'HTML'
            elif ext in ['.css', '.scss', '.sass', '.less']:
                file_type = 'CSS'
            elif ext in ['.js', '.jsx']:
                file_type = 'JavaScript'
            elif ext in ['.ts', '.tsx']:
                file_type = 'TypeScript'
            elif ext == '.py':
                file_type = 'Python'
            elif ext in ['.java', '.kt']:
                file_type = 'Java'
            elif ext in ['.c', '.cpp', '.h', '.hpp']:
                file_type = 'C/C++'
            elif ext == '.cs':
                file_type = 'C#'
            elif ext == '.go':
                file_type = 'Go'
            elif ext == '.rb':
                file_type = 'Ruby'
            elif ext == '.php':
                file_type = 'PHP'
            elif ext == '.swift':
                file_type = 'Swift'
            elif ext in ['.json', '.xml', '.yml', '.yaml']:
                file_type = ext[1:].upper()
            elif ext == '.md':
                file_type = 'Markdown'
            else:
                file_type = 'Other'
            
            file_types[file_type] += 1
    
    # Create a summary
    summary = f"Project Summary for {os.path.basename(project_path)}\n"
    summary += "=" * 50 + "\n\n"
    
    # Basic statistics
    summary += "Basic Statistics:\n"
    summary += f"- Total files: {file_count}\n"
    summary += f"- Total directories: {directory_count}\n"
    
    # File types
    summary += "\nFile Types:\n"
    for file_type, count in file_types.most_common():
        summary += f"- {file_type}: {count} files\n"
    
    # Largest files
    summary += "\nLargest Files:\n"
    largest_files = sorted(file_sizes.items(), key=lambda x: x[1], reverse=True)[:10]
    for file_path, size in largest_files:
        size_kb = size / 1024
        summary += f"- {file_path}: {size_kb:.2f} KB\n"
    
    return summary

def extract_code_patterns(project_path):
    """Extract code patterns from the project files"""
    print("Extracting code patterns...")
    
    # Initialize patterns
    code_patterns = {
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
    for root, _, files in os.walk(project_path):
        # Skip hidden directories and common directories to ignore
        if any(part.startswith('.') for part in root.split(os.sep)):
            continue
        if any(part in ['node_modules', 'venv', 'env', '__pycache__', 'dist', 'build'] for part in root.split(os.sep)):
            continue
        
        for file in files:
            # Skip hidden files
            if file.startswith('.'):
                continue
            
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            
            try:
                # Process based on file type
                if ext in ['.html', '.htm']:
                    _analyze_html_file(file_path, code_patterns)
                elif ext in ['.css', '.scss', '.sass', '.less']:
                    _analyze_css_file(file_path, code_patterns)
                elif ext in ['.js', '.jsx', '.ts', '.tsx']:
                    _analyze_js_file(file_path, code_patterns)
            except Exception as e:
                print(f"Error analyzing file {file_path}: {e}")
    
    # Detect frameworks
    _detect_frameworks(code_patterns)
    
    return code_patterns

def _analyze_html_file(file_path, code_patterns):
    """Analyze an HTML file for patterns"""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Extract HTML elements
    element_pattern = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)[^>]*>')
    for match in element_pattern.finditer(content):
        element = match.group(1).lower()
        code_patterns['HTML']['elements'][element] += 1
    
    # Extract classes
    class_pattern = re.compile(r'class=["\']([^"\']+)["\']')
    for match in class_pattern.finditer(content):
        classes = match.group(1).split()
        for cls in classes:
            code_patterns['HTML']['classes'][cls] += 1
    
    # Extract IDs
    id_pattern = re.compile(r'id=["\']([^"\']+)["\']')
    for match in id_pattern.finditer(content):
        id_value = match.group(1)
        code_patterns['HTML']['ids'][id_value] += 1
    
    # Look for common patterns
    if '<div class="container">' in content:
        code_patterns['HTML']['patterns'].append('Bootstrap container')
    if '<div class="row">' in content:
        code_patterns['HTML']['patterns'].append('Bootstrap grid')
    if '<nav class="navbar">' in content:
        code_patterns['HTML']['patterns'].append('Bootstrap navbar')

def _analyze_css_file(file_path, code_patterns):
    """Analyze a CSS file for patterns"""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Extract selectors
    selector_pattern = re.compile(r'([^{]+){[^}]*}')
    for match in selector_pattern.finditer(content):
        selector = match.group(1).strip()
        code_patterns['CSS']['selectors'][selector] += 1
    
    # Extract properties
    property_pattern = re.compile(r'([a-zA-Z-]+)\s*:\s*([^;]+);')
    for match in property_pattern.finditer(content):
        prop = match.group(1).strip()
        value = match.group(2).strip()
        code_patterns['CSS']['properties'][f"{prop}: {value}"] += 1
    
    # Extract media queries
    media_pattern = re.compile(r'@media\s+([^{]+){')
    for match in media_pattern.finditer(content):
        query = match.group(1).strip()
        code_patterns['CSS']['media_queries'][query] += 1
    
    # Look for common patterns
    if '.container' in content:
        code_patterns['CSS']['patterns'].append('Container class')
    if 'display: flex' in content:
        code_patterns['CSS']['patterns'].append('Flexbox layout')
    if 'display: grid' in content:
        code_patterns['CSS']['patterns'].append('Grid layout')

def _analyze_js_file(file_path, code_patterns):
    """Analyze a JavaScript file for patterns"""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Extract functions
    function_pattern = re.compile(r'function\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\(')
    for match in function_pattern.finditer(content):
        func_name = match.group(1)
        code_patterns['JavaScript']['functions'][func_name] += 1
    
    # Extract arrow functions
    arrow_func_pattern = re.compile(r'(const|let|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*=\s*\([^)]*\)\s*=>')
    for match in arrow_func_pattern.finditer(content):
        func_name = match.group(2)
        code_patterns['JavaScript']['functions'][func_name] += 1
    
    # Extract classes
    class_pattern = re.compile(r'class\s+([a-zA-Z_$][a-zA-Z0-9_$]*)')
    for match in class_pattern.finditer(content):
        class_name = match.group(1)
        code_patterns['JavaScript']['classes'][class_name] += 1
    
    # Extract imports
    import_pattern = re.compile(r'import\s+(?:{[^}]*}|[a-zA-Z_$][a-zA-Z0-9_$]*)\s+from\s+[\'"]([^\'"]+)[\'"]')
    for match in import_pattern.finditer(content):
        module = match.group(1)
        code_patterns['JavaScript']['imports'][module] += 1
    
    # Look for common patterns
    if 'document.querySelector' in content:
        code_patterns['JavaScript']['patterns'].append('DOM manipulation')
    if 'addEventListener' in content:
        code_patterns['JavaScript']['patterns'].append('Event listeners')
    if 'fetch(' in content:
        code_patterns['JavaScript']['patterns'].append('Fetch API')

def _detect_frameworks(code_patterns):
    """Detect frameworks used in the project"""
    # HTML frameworks
    if code_patterns['HTML']['classes'].get('container', 0) > 0 and code_patterns['HTML']['classes'].get('row', 0) > 0:
        code_patterns['HTML']['frameworks'].add('Bootstrap')
    
    if code_patterns['HTML']['classes'].get('mui', 0) > 0 or code_patterns['HTML']['classes'].get('MuiButton', 0) > 0:
        code_patterns['HTML']['frameworks'].add('Material-UI')
    
    # CSS frameworks
    if '.container' in code_patterns['CSS']['selectors'] and '.row' in code_patterns['CSS']['selectors']:
        code_patterns['CSS']['frameworks'].add('Bootstrap')
    
    if '@tailwind' in ' '.join(code_patterns['CSS']['selectors'].keys()):
        code_patterns['CSS']['frameworks'].add('Tailwind CSS')
    
    # JavaScript frameworks
    if 'react' in ' '.join(code_patterns['JavaScript']['imports'].keys()):
        code_patterns['JavaScript']['frameworks'].add('React')
    
    if 'vue' in ' '.join(code_patterns['JavaScript']['imports'].keys()):
        code_patterns['JavaScript']['frameworks'].add('Vue.js')
    
    if 'angular' in ' '.join(code_patterns['JavaScript']['imports'].keys()):
        code_patterns['JavaScript']['frameworks'].add('Angular')
    
    if 'jquery' in ' '.join(code_patterns['JavaScript']['imports'].keys()) or '$(' in ' '.join(code_patterns['JavaScript']['functions'].keys()):
        code_patterns['JavaScript']['frameworks'].add('jQuery')

def save_knowledge(knowledge_path, code_patterns):
    """Save the knowledge to files"""
    # Create the knowledge directory if it doesn't exist
    os.makedirs(knowledge_path, exist_ok=True)
    
    # Save code patterns
    patterns_file = os.path.join(knowledge_path, 'code_patterns.json')
    try:
        # Convert sets to lists for JSON serialization
        patterns_copy = {}
        for lang, data in code_patterns.items():
            patterns_copy[lang] = {}
            for key, value in data.items():
                if key == 'frameworks':
                    patterns_copy[lang][key] = list(value)
                elif isinstance(value, Counter):
                    patterns_copy[lang][key] = dict(value)
                else:
                    patterns_copy[lang][key] = value
        
        with open(patterns_file, 'w') as f:
            json.dump(patterns_copy, f, indent=2)
        print(f"Saved code patterns to {patterns_file}")
    except Exception as e:
        print(f"Error saving code patterns: {e}")

def main():
    """Main entry point for the simple agent"""
    parser = argparse.ArgumentParser(description="Simple Code Agent - A lightweight code analyzer")
    parser.add_argument("--project", "-p", help="Path to the project to analyze", default=".")
    
    args = parser.parse_args()
    
    # Convert to absolute path
    project_path = os.path.abspath(args.project)
    
    print(f"Simple Code Agent starting...")
    print(f"Project path: {project_path}")
    
    # Set up folders
    knowledge_path = os.path.join(project_path, "knowledge")
    os.makedirs(knowledge_path, exist_ok=True)
    
    # Analyze the project
    print("Analyzing project structure...")
    summary = analyze_project(project_path)
    summary_path = os.path.join(project_path, "summary.txt")
    with open(summary_path, "w") as f:
        f.write(summary)
    print(f"Project summary written to {summary_path}")
    
    # Extract code patterns
    print("Learning from project code...")
    code_patterns = extract_code_patterns(project_path)
    save_knowledge(knowledge_path, code_patterns)
    print("Knowledge base updated")
    
    print("Simple Code Agent finished")

if __name__ == "__main__":
    main()
