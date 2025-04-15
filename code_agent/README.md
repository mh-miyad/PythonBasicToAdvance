# Code Agent

An intelligent agent that analyzes projects, learns coding patterns, and automatically writes code based on tasks.

## Features

- **Project Analysis**: Analyzes your project structure and creates a summary
- **Knowledge Base**: Learns from your existing code and stores patterns
- **Task Execution**: Executes tasks based on natural language descriptions
- **Code Writing**: Automatically writes HTML, CSS, and JavaScript code
- **VS Code Integration**: Controls VS Code to navigate and edit files like a human
- **Web Learning**: Searches the internet for code examples and documentation

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/code-agent.git
   cd code-agent
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Simple Agent (No Dependencies Required)

If you don't want to install all the dependencies, you can use the simple agent which only requires Python:

1. On Windows, simply run the `analyze_project.bat` file
2. On Linux/Mac, run:
   ```
   python simple_agent.py --project /path/to/your/project
   ```

The simple agent will analyze your project and create a summary without requiring any external dependencies.

## Usage

### Basic Usage

```
python main.py --project /path/to/your/project --analyze --learn
```

This will analyze your project, create a summary, and learn from your existing code.

### Execute a Task

```
python main.py --project /path/to/your/project --task "Create a new HTML file named index.html with a Bootstrap layout"
```

This will create a new HTML file with a Bootstrap layout based on the task description.

### Interactive Mode

```
python main.py --project /path/to/your/project --interactive
```

This will start the agent in interactive mode, allowing you to enter commands and tasks.

## Command Line Options

- `--project`, `-p`: Path to the project to analyze (default: current directory)
- `--task`, `-t`: Task file to execute
- `--analyze`, `-a`: Analyze the project and create a summary
- `--learn`, `-l`: Learn from the project and update knowledge base
- `--execute`, `-e`: Execute a task
- `--interactive`, `-i`: Run in interactive mode

## Project Structure

- `main.py`: Main entry point for the agent
- `modules/`: Contains the modules used by the agent
  - `project_analyzer.py`: Analyzes project structure and code patterns
  - `knowledge_base.py`: Stores and manages knowledge learned from the project
  - `task_executor.py`: Executes tasks by parsing task descriptions
  - `code_writer.py`: Writes code based on the knowledge base and web learning
  - `vs_code_controller.py`: Controls VS Code to navigate and edit files
  - `web_learner.py`: Learns from the internet by searching for code examples

## Examples

### Example 1: Create a simple HTML page

```
python main.py --project /path/to/your/project --task "Create a new HTML file named index.html with a heading, paragraph, and a list"
```

### Example 2: Create a Bootstrap layout

```
python main.py --project /path/to/your/project --task "Create a new HTML file named dashboard.html with a Bootstrap layout including a navbar and cards"
```

### Example 3: Add CSS styles

```
python main.py --project /path/to/your/project --task "Create a new CSS file named styles.css with styles for the body, container, and header"
```

## Requirements

- Python 3.6+
- PyAutoGUI
- Requests
- BeautifulSoup4

## License

This project is licensed under the MIT License - see the LICENSE file for details.
