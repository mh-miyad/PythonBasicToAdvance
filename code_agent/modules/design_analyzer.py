"""
Design Analyzer Module

This module analyzes existing HTML and CSS files to extract design patterns,
color schemes, and layout structures to maintain consistency in new files.
"""

import os
import re
import json
import time
from pathlib import Path
from collections import defaultdict, Counter
import shutil

class DesignAnalyzer:
    """Analyzes existing design patterns in HTML and CSS files"""
    
    def __init__(self, project_path):
        """Initialize the design analyzer with the project path"""
        self.project_path = project_path
        self.design_patterns = {
            'colors': {},
            'fonts': [],
            'spacing': {},
            'layout': {},
            'components': {},
            'css_classes': Counter(),
            'css_files': [],
            'bootstrap_version': None,
            'frameworks': set()
        }
        
        # Create a cache directory if it doesn't exist
        self.cache_dir = os.path.join(project_path, 'knowledge', 'design_cache')
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def analyze_project_design(self, target_dir=None):
        """Analyze the design patterns in the project"""
        print(f"Analyzing design patterns in {self.project_path}...")
        
        # If target_dir is specified, focus on that directory
        if target_dir:
            search_path = os.path.join(self.project_path, target_dir)
            if not os.path.exists(search_path):
                print(f"Target directory {target_dir} does not exist")
                return self.design_patterns
        else:
            search_path = self.project_path
        
        # Find all HTML and CSS files
        html_files = []
        css_files = []
        
        for root, _, files in os.walk(search_path):
            for file in files:
                file_path = os.path.join(root, file)
                
                if file.endswith('.html') or file.endswith('.htm'):
                    html_files.append(file_path)
                elif file.endswith('.css'):
                    css_files.append(file_path)
        
        # Store the CSS files for later reference
        self.design_patterns['css_files'] = [os.path.relpath(f, self.project_path) for f in css_files]
        
        # Analyze CSS files first to extract design patterns
        for css_file in css_files:
            self._analyze_css_file(css_file)
        
        # Then analyze HTML files to extract layout and component patterns
        for html_file in html_files:
            self._analyze_html_file(html_file)
        
        # Save the design patterns to cache
        self._save_design_patterns()
        
        return self.design_patterns
    
    def _analyze_css_file(self, css_file):
        """Analyze a CSS file to extract design patterns"""
        print(f"Analyzing CSS file: {os.path.basename(css_file)}")
        
        try:
            with open(css_file, 'r', encoding='utf-8', errors='ignore') as f:
                css_content = f.read()
            
            # Extract color values
            color_pattern = re.compile(r'(?:color|background|background-color|border-color|box-shadow):\s*(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)|hsla?\([^)]+\)|[a-zA-Z]+)')
            for match in color_pattern.finditer(css_content):
                color_value = match.group(1).strip().lower()
                if color_value not in ['inherit', 'initial', 'unset', 'transparent', 'currentcolor']:
                    self.design_patterns['colors'][color_value] = self.design_patterns['colors'].get(color_value, 0) + 1
            
            # Extract font families
            font_pattern = re.compile(r'font-family:\s*([^;]+)')
            for match in font_pattern.finditer(css_content):
                font_value = match.group(1).strip()
                if font_value not in self.design_patterns['fonts']:
                    self.design_patterns['fonts'].append(font_value)
            
            # Extract spacing values
            spacing_pattern = re.compile(r'(?:margin|padding|gap)(?:-[a-z]+)?:\s*([^;]+)')
            for match in spacing_pattern.finditer(css_content):
                spacing_value = match.group(1).strip()
                self.design_patterns['spacing'][spacing_value] = self.design_patterns['spacing'].get(spacing_value, 0) + 1
            
            # Extract layout patterns
            layout_pattern = re.compile(r'(?:display|flex-direction|justify-content|align-items|grid-template-columns):\s*([^;]+)')
            for match in layout_pattern.finditer(css_content):
                layout_value = match.group(0).strip()
                self.design_patterns['layout'][layout_value] = self.design_patterns['layout'].get(layout_value, 0) + 1
            
            # Extract CSS classes
            class_pattern = re.compile(r'\.([a-zA-Z0-9_-]+)')
            for match in class_pattern.finditer(css_content):
                class_name = match.group(1)
                self.design_patterns['css_classes'][class_name] += 1
            
            # Check for Bootstrap
            if 'bootstrap' in css_content.lower():
                self.design_patterns['frameworks'].add('Bootstrap')
                
                # Try to determine Bootstrap version
                version_match = re.search(r'Bootstrap\s+v?(\d+\.\d+\.\d+)', css_content, re.IGNORECASE)
                if version_match:
                    self.design_patterns['bootstrap_version'] = version_match.group(1)
                elif 'bs5' in css_content.lower() or 'v5' in css_content.lower():
                    self.design_patterns['bootstrap_version'] = '5.x'
                elif 'bs4' in css_content.lower() or 'v4' in css_content.lower():
                    self.design_patterns['bootstrap_version'] = '4.x'
            
            # Check for other frameworks
            if 'tailwind' in css_content.lower():
                self.design_patterns['frameworks'].add('Tailwind CSS')
            if 'bulma' in css_content.lower():
                self.design_patterns['frameworks'].add('Bulma')
            if 'foundation' in css_content.lower():
                self.design_patterns['frameworks'].add('Foundation')
            
        except Exception as e:
            print(f"Error analyzing CSS file {css_file}: {e}")
    
    def _analyze_html_file(self, html_file):
        """Analyze an HTML file to extract layout and component patterns"""
        print(f"Analyzing HTML file: {os.path.basename(html_file)}")
        
        try:
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()
            
            # Extract component patterns
            component_patterns = {
                'navbar': r'<nav[^>]*class="[^"]*navbar[^"]*"[^>]*>',
                'card': r'<div[^>]*class="[^"]*card[^"]*"[^>]*>',
                'button': r'<button[^>]*class="[^"]*btn[^"]*"[^>]*>',
                'form': r'<form[^>]*>',
                'table': r'<table[^>]*>',
                'footer': r'<footer[^>]*>',
                'header': r'<header[^>]*>',
                'modal': r'<div[^>]*class="[^"]*modal[^"]*"[^>]*>',
                'carousel': r'<div[^>]*class="[^"]*carousel[^"]*"[^>]*>',
                'accordion': r'<div[^>]*class="[^"]*accordion[^"]*"[^>]*>'
            }
            
            for component, pattern in component_patterns.items():
                matches = re.findall(pattern, html_content, re.IGNORECASE)
                if matches:
                    self.design_patterns['components'][component] = self.design_patterns['components'].get(component, 0) + len(matches)
            
            # Extract CSS classes from HTML
            class_pattern = re.compile(r'class="([^"]+)"')
            for match in class_pattern.finditer(html_content):
                classes = match.group(1).split()
                for class_name in classes:
                    self.design_patterns['css_classes'][class_name] += 1
            
            # Check for Bootstrap
            if 'bootstrap' in html_content.lower():
                self.design_patterns['frameworks'].add('Bootstrap')
                
                # Try to determine Bootstrap version from link tag
                version_match = re.search(r'bootstrap@(\d+\.\d+\.\d+)', html_content)
                if version_match:
                    self.design_patterns['bootstrap_version'] = version_match.group(1)
            
            # Check for other frameworks
            if 'tailwind' in html_content.lower():
                self.design_patterns['frameworks'].add('Tailwind CSS')
            if 'bulma' in html_content.lower():
                self.design_patterns['frameworks'].add('Bulma')
            if 'foundation' in html_content.lower():
                self.design_patterns['frameworks'].add('Foundation')
            
        except Exception as e:
            print(f"Error analyzing HTML file {html_file}: {e}")
    
    def _save_design_patterns(self):
        """Save the design patterns to a cache file"""
        cache_file = os.path.join(self.cache_dir, 'design_patterns.json')
        
        # Convert sets to lists for JSON serialization
        patterns_copy = {}
        for key, value in self.design_patterns.items():
            if isinstance(value, set):
                patterns_copy[key] = list(value)
            elif isinstance(value, Counter):
                patterns_copy[key] = dict(value)
            else:
                patterns_copy[key] = value
        
        try:
            with open(cache_file, 'w') as f:
                json.dump(patterns_copy, f, indent=2)
            print(f"Saved design patterns to {cache_file}")
        except Exception as e:
            print(f"Error saving design patterns: {e}")
    
    def load_design_patterns(self):
        """Load design patterns from cache"""
        cache_file = os.path.join(self.cache_dir, 'design_patterns.json')
        
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    patterns = json.load(f)
                
                # Convert lists back to sets where needed
                if 'frameworks' in patterns:
                    patterns['frameworks'] = set(patterns['frameworks'])
                
                # Convert dictionaries to Counters where needed
                if 'css_classes' in patterns:
                    patterns['css_classes'] = Counter(patterns['css_classes'])
                
                self.design_patterns = patterns
                print(f"Loaded design patterns from {cache_file}")
                return True
            except Exception as e:
                print(f"Error loading design patterns: {e}")
                return False
        else:
            print(f"No cached design patterns found at {cache_file}")
            return False
    
    def copy_css_files(self, target_dir):
        """Copy CSS files to the target directory"""
        if not self.design_patterns['css_files']:
            print("No CSS files found in design patterns")
            return False
        
        os.makedirs(target_dir, exist_ok=True)
        
        for css_file in self.design_patterns['css_files']:
            source_path = os.path.join(self.project_path, css_file)
            target_path = os.path.join(target_dir, os.path.basename(css_file))
            
            if os.path.exists(source_path):
                try:
                    shutil.copy2(source_path, target_path)
                    print(f"Copied CSS file: {css_file} to {target_path}")
                except Exception as e:
                    print(f"Error copying CSS file {css_file}: {e}")
            else:
                print(f"CSS file not found: {source_path}")
        
        return True
    
    def get_primary_color(self):
        """Get the most commonly used color"""
        if not self.design_patterns['colors']:
            return "#4361ee"  # Default blue if no colors found
        
        # Sort colors by frequency
        sorted_colors = sorted(self.design_patterns['colors'].items(), key=lambda x: x[1], reverse=True)
        
        # Filter out black, white, and transparent
        filtered_colors = [color for color, _ in sorted_colors if color not in ['#000', '#000000', '#fff', '#ffffff', 'transparent']]
        
        if filtered_colors:
            return filtered_colors[0]
        else:
            return sorted_colors[0][0]
    
    def get_font_family(self):
        """Get the primary font family"""
        if not self.design_patterns['fonts']:
            return "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"  # Default font if none found
        
        return self.design_patterns['fonts'][0]
    
    def get_bootstrap_version(self):
        """Get the Bootstrap version"""
        if self.design_patterns['bootstrap_version']:
            return self.design_patterns['bootstrap_version']
        elif 'Bootstrap' in self.design_patterns['frameworks']:
            return "5.1.3"  # Default to latest stable version
        else:
            return None
    
    def get_common_classes(self, limit=10):
        """Get the most commonly used CSS classes"""
        if not self.design_patterns['css_classes']:
            return []
        
        return [cls for cls, _ in self.design_patterns['css_classes'].most_common(limit)]
