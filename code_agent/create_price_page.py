#!/usr/bin/env python3
"""
Create Price Page Script

This script analyzes your existing design, creates a price page that matches your style,
and opens it in Live Server.
"""

import os
import sys
import argparse
import time
from pathlib import Path

# Add the parent directory to the path so we can import the modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.design_analyzer import DesignAnalyzer
from modules.page_generator import PageGenerator
from modules.screen_controller import ScreenController

def main():
    """Main entry point for the script"""
    parser = argparse.ArgumentParser(description="Create a price page based on your existing design")
    parser.add_argument("--project", "-p", help="Path to the project", default=".")
    parser.add_argument("--target", "-t", help="Target directory to analyze (e.g., 'dist')", default="dist")
    parser.add_argument("--output", "-o", help="Output directory for the price page", default=".")
    parser.add_argument("--open", "-O", help="Open the page in Live Server after creation", action="store_true")
    
    args = parser.parse_args()
    
    # Convert to absolute paths
    project_path = os.path.abspath(args.project)
    output_path = os.path.abspath(args.output)
    
    print(f"Creating price page based on existing design...")
    print(f"Project path: {project_path}")
    print(f"Target directory: {args.target}")
    print(f"Output path: {output_path}")
    
    # Create the design analyzer
    design_analyzer = DesignAnalyzer(project_path)
    
    # Try to load cached design patterns
    if not design_analyzer.load_design_patterns():
        print(f"Analyzing design patterns in {args.target}...")
        design_analyzer.analyze_project_design(args.target)
    
    # Create the page generator
    page_generator = PageGenerator(project_path, design_analyzer)
    
    # Generate the price page
    html_file_path = page_generator.generate_price_page(output_path)
    
    if html_file_path:
        print(f"Price page created successfully: {html_file_path}")
        
        # Open the page in Live Server if requested
        if args.open:
            print("Opening the page in Live Server...")
            screen_controller = ScreenController()
            screen_controller.start_live_server(html_file_path)
    else:
        print("Failed to create price page")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
