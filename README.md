# Riddle - Command Runner from TOML Configuration

## Overview

Riddle is a lightweight yet powerful command execution tool that reads commands from a TOML configuration file and executes them sequentially. Designed for automation workflows, build processes, and task orchestration, Riddle provides a structured way to define and run command sequences with proper error handling.

## Key Features

- **TOML-based configuration** for clean, readable command definitions
- **Sequential command execution** with automatic failure detection
- **Shell command support** for compatibility with existing tools
- **Type checking** to ensure command validity before execution
- **Verbose output** showing each command as it runs
- **Simple installation** with a one-line installer
- **Cross-platform compatibility** through Python

## Installation

Install Riddle with a single command:

```bash
curl -sSL https://raw.githubusercontent.com/funterminal/riddle/refs/heads/main/install.sh | bash
```

This will:
1. Download the latest version of `riddle.py`
2. Place it in your current directory
3. Print installation confirmation

## Usage

### Basic Execution

Run commands defined in your TOML file:

```bash
python3 riddle.py run riddle.toml
```

### Configuration File Format

Create a `riddle.toml` file with the following structure:

```toml
commands = [
    "echo 'Running first command'",
    "python --version",
    "ls -la",
    "docker build -t myapp ."
]
```

### Advanced Configuration

The configuration supports all valid TOML syntax, allowing for complex configurations:

```toml
[metadata]
author = "Your Name"
description = "Build pipeline for project X"

[commands]
main = [
    "echo 'Starting build process'",
    "npm install",
    "npm run build",
    "./deploy.sh"
]

test = [
    "pytest tests/",
    "mypy src/"
]
```

## Error Handling

Riddle implements robust error handling with the following behaviors:

- **Command failure**: Stops execution and exits if any command returns non-zero
- **Configuration errors**: Validates TOML structure before execution
- **Type checking**: Ensures all commands are strings
- **File existence**: Verifies configuration file exists before processing

## Examples

### Development Workflow

```toml
commands = [
    "git pull origin main",
    "pip install -r requirements.txt",
    "pytest tests/",
    "python manage.py migrate",
    "python manage.py runserver"
]
```

### Deployment Pipeline

```toml
commands = [
    "docker stop myapp || true",
    "docker rm myapp || true",
    "docker build -t myapp .",
    "docker run -d --name myapp -p 8000:8000 myapp"
]
```

## Best Practices

1. **Use absolute paths** for commands when possible
2. **Include error handling** in your commands (using `||` operators)
3. **Order commands carefully** as they execute sequentially
4. **Comment your TOML** with `#` for complex configurations
5. **Test commands individually** before adding to the configuration

## Version Information

Current version: 0.1

## License

Riddle is open-source software. See LICENSE file for details.

## Contributing

Contributions are welcome. Please follow standard GitHub pull request procedures.

## Support

For issues or feature requests, please open an issue on the GitHub repository.
