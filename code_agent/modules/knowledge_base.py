"""
Knowledge Base Module

This module stores and manages the knowledge learned from the project.
It provides methods to update, query, and use the knowledge base.
"""

import os
import json
import pickle
from datetime import datetime
from collections import defaultdict

class KnowledgeBase:
    """Stores and manages knowledge learned from the project"""
    
    def __init__(self, knowledge_path):
        """Initialize the knowledge base with the path to store knowledge"""
        self.knowledge_path = knowledge_path
        self.code_patterns = {
            'HTML': {
                'elements': {},
                'classes': {},
                'ids': {},
                'frameworks': set(),
                'patterns': []
            },
            'CSS': {
                'selectors': {},
                'properties': {},
                'media_queries': {},
                'frameworks': set(),
                'patterns': []
            },
            'JavaScript': {
                'functions': {},
                'classes': {},
                'imports': {},
                'frameworks': set(),
                'patterns': []
            }
        }
        self.file_templates = {
            'HTML': [],
            'CSS': [],
            'JavaScript': []
        }
        self.coding_style = {
            'HTML': {
                'indentation': 2,
                'attribute_quotes': 'double',  # 'single' or 'double'
                'self_closing': True  # Whether to use self-closing tags
            },
            'CSS': {
                'indentation': 2,
                'property_newline': True,  # Whether to put each property on a new line
                'bracket_style': 'same-line'  # 'same-line' or 'new-line'
            },
            'JavaScript': {
                'indentation': 2,
                'semicolons': True,  # Whether to use semicolons
                'quotes': 'single',  # 'single' or 'double'
                'bracket_style': 'same-line'  # 'same-line' or 'new-line'
            }
        }
        
        # Load existing knowledge if available
        self.load_knowledge()
    
    def load_knowledge(self):
        """Load existing knowledge from files"""
        # Load code patterns
        patterns_file = os.path.join(self.knowledge_path, 'code_patterns.json')
        if os.path.exists(patterns_file):
            try:
                with open(patterns_file, 'r') as f:
                    patterns = json.load(f)
                    
                    # Convert sets from lists
                    for lang in ['HTML', 'CSS', 'JavaScript']:
                        if lang in patterns and 'frameworks' in patterns[lang]:
                            patterns[lang]['frameworks'] = set(patterns[lang]['frameworks'])
                    
                    self.code_patterns.update(patterns)
                print(f"Loaded code patterns from {patterns_file}")
            except Exception as e:
                print(f"Error loading code patterns: {e}")
        
        # Load file templates
        templates_file = os.path.join(self.knowledge_path, 'file_templates.pickle')
        if os.path.exists(templates_file):
            try:
                with open(templates_file, 'rb') as f:
                    self.file_templates = pickle.load(f)
                print(f"Loaded file templates from {templates_file}")
            except Exception as e:
                print(f"Error loading file templates: {e}")
        
        # Load coding style
        style_file = os.path.join(self.knowledge_path, 'coding_style.json')
        if os.path.exists(style_file):
            try:
                with open(style_file, 'r') as f:
                    self.coding_style.update(json.load(f))
                print(f"Loaded coding style from {style_file}")
            except Exception as e:
                print(f"Error loading coding style: {e}")
    
    def save_knowledge(self):
        """Save the current knowledge to files"""
        # Create the knowledge directory if it doesn't exist
        os.makedirs(self.knowledge_path, exist_ok=True)
        
        # Save code patterns
        patterns_file = os.path.join(self.knowledge_path, 'code_patterns.json')
        try:
            # Convert sets to lists for JSON serialization
            patterns_copy = {}
            for lang, data in self.code_patterns.items():
                patterns_copy[lang] = {}
                for key, value in data.items():
                    if key == 'frameworks':
                        patterns_copy[lang][key] = list(value)
                    else:
                        patterns_copy[lang][key] = value
            
            with open(patterns_file, 'w') as f:
                json.dump(patterns_copy, f, indent=2)
            print(f"Saved code patterns to {patterns_file}")
        except Exception as e:
            print(f"Error saving code patterns: {e}")
        
        # Save file templates
        templates_file = os.path.join(self.knowledge_path, 'file_templates.pickle')
        try:
            with open(templates_file, 'wb') as f:
                pickle.dump(self.file_templates, f)
            print(f"Saved file templates to {templates_file}")
        except Exception as e:
            print(f"Error saving file templates: {e}")
        
        # Save coding style
        style_file = os.path.join(self.knowledge_path, 'coding_style.json')
        try:
            with open(style_file, 'w') as f:
                json.dump(self.coding_style, f, indent=2)
            print(f"Saved coding style to {style_file}")
        except Exception as e:
            print(f"Error saving coding style: {e}")
        
        # Save a snapshot with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        snapshot_dir = os.path.join(self.knowledge_path, 'snapshots', timestamp)
        os.makedirs(snapshot_dir, exist_ok=True)
        
        try:
            with open(os.path.join(snapshot_dir, 'code_patterns.json'), 'w') as f:
                json.dump(patterns_copy, f, indent=2)
            
            with open(os.path.join(snapshot_dir, 'file_templates.pickle'), 'wb') as f:
                pickle.dump(self.file_templates, f)
            
            with open(os.path.join(snapshot_dir, 'coding_style.json'), 'w') as f:
                json.dump(self.coding_style, f, indent=2)
            
            print(f"Created knowledge snapshot at {snapshot_dir}")
        except Exception as e:
            print(f"Error creating knowledge snapshot: {e}")
    
    def update_from_analyzer(self, analyzer):
        """Update the knowledge base from a ProjectAnalyzer"""
        # Get the code patterns from the analyzer
        analyzer_patterns = analyzer.get_code_patterns()
        
        # Update our code patterns
        for lang in ['HTML', 'CSS', 'JavaScript']:
            if lang in analyzer_patterns:
                # Update elements, classes, ids, etc.
                for key in self.code_patterns[lang]:
                    if key in analyzer_patterns[lang]:
                        if key == 'frameworks':
                            # Merge sets
                            self.code_patterns[lang][key].update(analyzer_patterns[lang][key])
                        elif key == 'patterns':
                            # Merge lists, avoiding duplicates
                            existing_patterns = set(self.code_patterns[lang][key])
                            for pattern in analyzer_patterns[lang][key]:
                                if pattern not in existing_patterns:
                                    self.code_patterns[lang][key].append(pattern)
                                    existing_patterns.add(pattern)
                        else:
                            # Merge dictionaries, adding counts
                            for item, count in analyzer_patterns[lang][key].items():
                                if item in self.code_patterns[lang][key]:
                                    self.code_patterns[lang][key][item] += count
                                else:
                                    self.code_patterns[lang][key][item] = count
        
        # Infer coding style from the analyzer's data
        self._infer_coding_style(analyzer)
        
        # Extract file templates from the analyzer
        self._extract_file_templates(analyzer)
        
        # Save the updated knowledge
        self.save_knowledge()
    
    def _infer_coding_style(self, analyzer):
        """Infer coding style from the analyzer's data"""
        # This is a simplified implementation
        # In a real implementation, you would analyze the code more thoroughly
        
        # For now, we'll just use some defaults
        self.coding_style = {
            'HTML': {
                'indentation': 2,
                'attribute_quotes': 'double',
                'self_closing': True
            },
            'CSS': {
                'indentation': 2,
                'property_newline': True,
                'bracket_style': 'same-line'
            },
            'JavaScript': {
                'indentation': 2,
                'semicolons': True,
                'quotes': 'single',
                'bracket_style': 'same-line'
            }
        }
    
    def _extract_file_templates(self, analyzer):
        """Extract file templates from the analyzer"""
        # This is a simplified implementation
        # In a real implementation, you would analyze the files more thoroughly
        
        # For now, we'll just use some defaults
        self.file_templates = {
            'HTML': [
                {
                    'name': 'Basic HTML5 Template',
                    'content': """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>"""
                }
            ],
            'CSS': [
                {
                    'name': 'Basic CSS Reset',
                    'content': """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
}"""
                }
            ],
            'JavaScript': [
                {
                    'name': 'Basic JavaScript Module',
                    'content': """// Module pattern
(function() {
  'use strict';
  
  // Your code here
  
})();"""
                }
            ]
        }
    
    def get_template(self, file_type, template_name=None):
        """Get a template for a specific file type"""
        if file_type not in self.file_templates or not self.file_templates[file_type]:
            return None
        
        if template_name:
            # Find a template with the given name
            for template in self.file_templates[file_type]:
                if template['name'] == template_name:
                    return template['content']
        
        # Return the first template if no name is specified or no match is found
        return self.file_templates[file_type][0]['content']
    
    def get_coding_style(self, language):
        """Get the coding style for a specific language"""
        return self.coding_style.get(language, {})
    
    def get_common_patterns(self, language, category, limit=10):
        """Get the most common patterns for a specific language and category"""
        if language not in self.code_patterns:
            return []
        
        if category not in self.code_patterns[language]:
            return []
        
        patterns = self.code_patterns[language][category]
        
        if isinstance(patterns, dict):
            # Sort by count in descending order
            sorted_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)
            return sorted_patterns[:limit]
        elif isinstance(patterns, list):
            return patterns[:limit]
        elif isinstance(patterns, set):
            return list(patterns)[:limit]
        
        return []
    
    def get_frameworks(self, language):
        """Get the frameworks used for a specific language"""
        if language not in self.code_patterns:
            return []
        
        return list(self.code_patterns[language].get('frameworks', set()))
    
    def search_patterns(self, query):
        """Search for patterns matching the query"""
        results = []
        
        for language, categories in self.code_patterns.items():
            for category, patterns in categories.items():
                if isinstance(patterns, dict):
                    for pattern, count in patterns.items():
                        if query.lower() in str(pattern).lower():
                            results.append({
                                'language': language,
                                'category': category,
                                'pattern': pattern,
                                'count': count
                            })
                elif isinstance(patterns, list):
                    for pattern in patterns:
                        if query.lower() in str(pattern).lower():
                            results.append({
                                'language': language,
                                'category': category,
                                'pattern': pattern
                            })
                elif isinstance(patterns, set):
                    for pattern in patterns:
                        if query.lower() in str(pattern).lower():
                            results.append({
                                'language': language,
                                'category': category,
                                'pattern': pattern
                            })
        
        return results
