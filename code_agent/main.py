#!/usr/bin/env python3
"""
Code Agent - An intelligent agent that analyzes projects, learns coding patterns,
and can automatically write code based on tasks.

This is the main entry point for the agent.
"""

import os
import sys
import argparse
import time
from pathlib import Path

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our modules
try:
    # Try relative imports first
    from .modules.project_analyzer import ProjectAnalyzer
    from .modules.knowledge_base import KnowledgeBase
    from .modules.task_executor import TaskExecutor
    from .modules.code_writer import CodeWriter
    from .modules.vs_code_controller import VSCodeController
    from .modules.web_learner import WebLearner
except ImportError:
    # Fall back to direct imports
    from modules.project_analyzer import ProjectAnalyzer
    from modules.knowledge_base import KnowledgeBase
    from modules.task_executor import TaskExecutor
    from modules.code_writer import CodeWriter
    from modules.vs_code_controller import VSCodeController

    # Handle missing optional dependencies
    try:
        from modules.web_learner import WebLearner
    except ImportError:
        print("Warning: WebLearner module could not be imported. Internet learning features will be disabled.")
        print("To enable these features, install the required dependencies: pip install beautifulsoup4 requests")

        # Create a dummy WebLearner class
        class WebLearner:
            def __init__(self):
                print("WebLearner is disabled due to missing dependencies.")

            def search_code_examples(self, *args, **kwargs):
                print("Cannot search code examples: required dependencies not installed.")
                return []

            def search_documentation(self, *args, **kwargs):
                print("Cannot search documentation: required dependencies not installed.")
                return []

            def get_bootstrap_example(self, *args, **kwargs):
                print("Cannot get Bootstrap examples: required dependencies not installed.")
                return None

def setup_folders(project_path):
    """Set up the necessary folders for the agent"""
    # Create knowledge folder if it doesn't exist
    knowledge_path = os.path.join(project_path, "knowledge")
    if not os.path.exists(knowledge_path):
        os.makedirs(knowledge_path)
        print(f"Created knowledge folder at {knowledge_path}")

    # Create tasks folder if it doesn't exist
    tasks_path = os.path.join(project_path, "tasks")
    if not os.path.exists(tasks_path):
        os.makedirs(tasks_path)
        print(f"Created tasks folder at {tasks_path}")

    return knowledge_path, tasks_path

def main():
    """Main entry point for the agent"""
    parser = argparse.ArgumentParser(description="Code Agent - An intelligent coding assistant")
    parser.add_argument("--project", "-p", help="Path to the project to analyze", default=".")
    parser.add_argument("--task", "-t", help="Task file to execute")
    parser.add_argument("--analyze", "-a", action="store_true", help="Analyze the project and create a summary")
    parser.add_argument("--learn", "-l", action="store_true", help="Learn from the project and update knowledge base")
    parser.add_argument("--execute", "-e", action="store_true", help="Execute a task")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode")

    args = parser.parse_args()

    # Convert to absolute path
    project_path = os.path.abspath(args.project)

    print(f"Code Agent starting...")
    print(f"Project path: {project_path}")

    # Set up folders
    knowledge_path, tasks_path = setup_folders(project_path)

    # Initialize components
    analyzer = ProjectAnalyzer(project_path)
    knowledge_base = KnowledgeBase(knowledge_path)
    vs_code = VSCodeController()
    web_learner = WebLearner()
    code_writer = CodeWriter(knowledge_base, web_learner, vs_code)
    task_executor = TaskExecutor(project_path, tasks_path, code_writer, vs_code)

    # Analyze the project if requested
    if args.analyze:
        print("Analyzing project structure...")
        summary = analyzer.analyze_project()
        summary_path = os.path.join(project_path, "summary.txt")
        with open(summary_path, "w") as f:
            f.write(summary)
        print(f"Project summary written to {summary_path}")

    # Learn from the project if requested
    if args.learn:
        print("Learning from project code...")
        analyzer.extract_code_patterns()
        knowledge_base.update_from_analyzer(analyzer)
        print("Knowledge base updated")

    # Execute a task if requested
    if args.execute and args.task:
        task_file = args.task
        if not os.path.isabs(task_file):
            task_file = os.path.join(tasks_path, task_file)

        if not os.path.exists(task_file):
            print(f"Task file {task_file} does not exist")
            return

        print(f"Executing task from {task_file}...")
        task_executor.execute_task(task_file)

    # Interactive mode
    if args.interactive:
        print("\nEntering interactive mode. Type 'exit' to quit.")
        print("Available commands:")
        print("  analyze - Analyze the project and create a summary")
        print("  learn - Learn from the project and update knowledge base")
        print("  task <description> - Create and execute a new task")
        print("  execute <task_file> - Execute an existing task")
        print("  exit - Exit the program")

        while True:
            command = input("\n> ").strip()

            if command == "exit":
                break
            elif command == "analyze":
                summary = analyzer.analyze_project()
                summary_path = os.path.join(project_path, "summary.txt")
                with open(summary_path, "w") as f:
                    f.write(summary)
                print(f"Project summary written to {summary_path}")
            elif command == "learn":
                analyzer.extract_code_patterns()
                knowledge_base.update_from_analyzer(analyzer)
                print("Knowledge base updated")
            elif command.startswith("task "):
                task_description = command[5:].strip()
                if not task_description:
                    print("Please provide a task description")
                    continue

                # Find the next available task file
                task_number = 1
                while True:
                    task_file = os.path.join(tasks_path, f"task{task_number}.txt")
                    if not os.path.exists(task_file):
                        break
                    task_number += 1

                # Write the task description to the file
                with open(task_file, "w") as f:
                    f.write(task_description)

                print(f"Created task file {task_file}")
                print(f"Executing task...")
                task_executor.execute_task(task_file)
            elif command.startswith("execute "):
                task_file = command[8:].strip()
                if not os.path.isabs(task_file):
                    task_file = os.path.join(tasks_path, task_file)

                if not os.path.exists(task_file):
                    print(f"Task file {task_file} does not exist")
                    continue

                print(f"Executing task from {task_file}...")
                task_executor.execute_task(task_file)
            else:
                print("Unknown command")

    print("Code Agent finished")

if __name__ == "__main__":
    main()
