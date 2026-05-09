# DevFlow

A Python-based command-line utility built to simplify parts of my local development workflow, including Git management, running local tools/services, and experimenting with AI-assisted development workflows.

## Features

- **Excalocal Integration** — Run local sketching/visualization tools through DevFlow.
- **Aider Integration** — Launch and work with the Aider AI coding assistant.
- **Git Repository Setup** — Automatically initialize Git repositories and create the first commit.
- **Lazy Commit Utility** — Quickly commit all changes or selectively choose files for commits. Use carefully, as this can bypass parts of the normal Git review workflow.

## Current Status

This project is experimental and still under active development.

## Notes

This project was built as part of my learning and experimentation process in Python automation and development tooling.


## External Requirements

### LM Studio
Used for running local LLM models with Aider.

Official website:
https://lmstudio.ai/

### Aider-AI
AI coding assistant used by DevFlow.

Installation and setup:
https://aider.chat/

### Excalocal
Installed through Node.js dependencies using npm install.


## Installation using CLI

1. Ensure you have Python 3.9+ installed.
2. Clone this project on new folder or your current project folder. ```git clone https://github.com/Y9sh/DevFlow.git```
3. cd DevFlow
4. ```python -m venv env-name ``` (setup the python env)
5. ```env-name\Scripts\activate ``` (activate the env)
6. ```pip install -r requirements.txt ```(Python dependencies)
7. ```npm install ``` (Node.js dependencies)
8.  Create a `.env` file inside the DevFlow root directory: ```FILE_PATH=C:/your/project/path```
9.  Install DevFlow in editable mode: ```pip install -e . ```
10. run the tools:```dev_tools ``` 

