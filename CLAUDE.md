# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server for providing weather information for Japan. The project is in early development stage.

## Development Environment

- **Python Version**: Requires Python >=3.13
- **Project Structure**: Standard Python package using pyproject.toml for configuration
- **Virtual Environment**: .venv/ directory is used for local development

## Common Commands

This project uses `uv` for Python package management:

```bash
# Install the project in development mode
uv pip install -e .

# Install with dependencies (when they exist)
uv pip install -e .[dev]

# Sync dependencies
uv sync
```

## Architecture Notes

- This is designed as an MCP server, which means it should implement the Model Context Protocol specification
- The project name suggests it will provide weather data specifically for Japan
- No source code has been implemented yet - the project is in initial setup phase