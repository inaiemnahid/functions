"""
Command list and helper utilities
"""

import os
import platform
import subprocess
from typing import Dict, List, Optional


def get_common_commands() -> Dict[str, List[Dict[str, str]]]:
    """
    Get a list of common useful commands organized by category
    
    Returns:
        dict: Dictionary of command categories with command details
    
    Example:
        >>> commands = get_common_commands()
        >>> print(commands['file_operations'])
    """
    commands = {
        "file_operations": [
            {
                "command": "ls -lah",
                "description": "List all files with details and hidden files",
                "platform": "Linux/Mac"
            },
            {
                "command": "dir",
                "description": "List files in directory",
                "platform": "Windows"
            },
            {
                "command": "cp -r source dest",
                "description": "Copy directory recursively",
                "platform": "Linux/Mac"
            },
            {
                "command": "mv source dest",
                "description": "Move or rename files",
                "platform": "Linux/Mac"
            },
            {
                "command": "rm -rf directory",
                "description": "Remove directory and contents",
                "platform": "Linux/Mac"
            },
            {
                "command": "find . -name '*.txt'",
                "description": "Find all .txt files in current directory",
                "platform": "Linux/Mac"
            }
        ],
        "system_info": [
            {
                "command": "uname -a",
                "description": "Display system information",
                "platform": "Linux/Mac"
            },
            {
                "command": "systeminfo",
                "description": "Display detailed system information",
                "platform": "Windows"
            },
            {
                "command": "df -h",
                "description": "Display disk usage in human-readable format",
                "platform": "Linux/Mac"
            },
            {
                "command": "free -h",
                "description": "Display memory usage",
                "platform": "Linux"
            },
            {
                "command": "top",
                "description": "Display running processes",
                "platform": "Linux/Mac"
            }
        ],
        "network": [
            {
                "command": "ping google.com",
                "description": "Test network connectivity",
                "platform": "All"
            },
            {
                "command": "curl -I https://example.com",
                "description": "Get HTTP headers from URL",
                "platform": "Linux/Mac"
            },
            {
                "command": "wget https://example.com/file",
                "description": "Download file from URL",
                "platform": "Linux/Mac"
            },
            {
                "command": "ifconfig",
                "description": "Display network interface configuration",
                "platform": "Linux/Mac"
            },
            {
                "command": "ipconfig",
                "description": "Display network configuration",
                "platform": "Windows"
            }
        ],
        "git": [
            {
                "command": "git status",
                "description": "Check repository status",
                "platform": "All"
            },
            {
                "command": "git add .",
                "description": "Stage all changes",
                "platform": "All"
            },
            {
                "command": "git commit -m 'message'",
                "description": "Commit staged changes",
                "platform": "All"
            },
            {
                "command": "git push",
                "description": "Push commits to remote",
                "platform": "All"
            },
            {
                "command": "git pull",
                "description": "Pull changes from remote",
                "platform": "All"
            },
            {
                "command": "git log --oneline",
                "description": "View commit history (compact)",
                "platform": "All"
            }
        ],
        "package_management": [
            {
                "command": "pip install package_name",
                "description": "Install Python package",
                "platform": "All"
            },
            {
                "command": "npm install package_name",
                "description": "Install Node.js package",
                "platform": "All"
            },
            {
                "command": "apt-get update && apt-get install package",
                "description": "Update and install package (Debian/Ubuntu)",
                "platform": "Linux"
            },
            {
                "command": "brew install package",
                "description": "Install package using Homebrew",
                "platform": "Mac"
            }
        ],
        "compression": [
            {
                "command": "tar -czf archive.tar.gz folder/",
                "description": "Create compressed tar.gz archive",
                "platform": "Linux/Mac"
            },
            {
                "command": "tar -xzf archive.tar.gz",
                "description": "Extract tar.gz archive",
                "platform": "Linux/Mac"
            },
            {
                "command": "zip -r archive.zip folder/",
                "description": "Create zip archive",
                "platform": "All"
            },
            {
                "command": "unzip archive.zip",
                "description": "Extract zip archive",
                "platform": "All"
            }
        ],
        "text_processing": [
            {
                "command": "grep 'pattern' file.txt",
                "description": "Search for pattern in file",
                "platform": "Linux/Mac"
            },
            {
                "command": "sed 's/old/new/g' file.txt",
                "description": "Replace text in file",
                "platform": "Linux/Mac"
            },
            {
                "command": "awk '{print $1}' file.txt",
                "description": "Print first column of file",
                "platform": "Linux/Mac"
            },
            {
                "command": "cat file1.txt file2.txt > combined.txt",
                "description": "Concatenate files",
                "platform": "Linux/Mac"
            }
        ]
    }
    
    return commands


def execute_command(command: str, shell: bool = True, capture_output: bool = True) -> Dict[str, any]:
    """
    Execute a shell command and return the result
    
    Args:
        command: Command to execute
        shell: Whether to execute through shell (default: True)
        capture_output: Whether to capture stdout/stderr (default: True)
    
    Returns:
        dict: Dictionary with 'returncode', 'stdout', 'stderr', and 'success' keys
    
    Example:
        >>> result = execute_command('ls -l')
        >>> if result['success']:
        ...     print(result['stdout'])
    """
    try:
        if capture_output:
            result = subprocess.run(
                command,
                shell=shell,
                capture_output=True,
                text=True
            )
        else:
            result = subprocess.run(command, shell=shell)
        
        return {
            'returncode': result.returncode,
            'stdout': result.stdout if capture_output else None,
            'stderr': result.stderr if capture_output else None,
            'success': result.returncode == 0
        }
    except Exception as e:
        return {
            'returncode': -1,
            'stdout': None,
            'stderr': str(e),
            'success': False
        }


def get_system_info() -> Dict[str, str]:
    """
    Get detailed system information
    
    Returns:
        dict: Dictionary with system information
    
    Example:
        >>> info = get_system_info()
        >>> print(f"OS: {info['system']} {info['release']}")
    """
    try:
        info = {
            'system': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python_version': platform.python_version(),
            'hostname': platform.node(),
        }
        
        # Add platform-specific information
        if platform.system() == 'Linux':
            try:
                with open('/etc/os-release', 'r') as f:
                    for line in f:
                        if line.startswith('PRETTY_NAME='):
                            info['distribution'] = line.split('=')[1].strip().strip('"')
                            break
            except:
                pass
        
        return info
    except Exception as e:
        return {'error': str(e)}


def print_commands_by_category(category: Optional[str] = None) -> None:
    """
    Print common commands, optionally filtered by category
    
    Args:
        category: Optional category to filter by (e.g., 'file_operations', 'git')
    
    Example:
        >>> print_commands_by_category('git')
        >>> print_commands_by_category()  # Print all categories
    """
    commands = get_common_commands()
    
    if category:
        if category in commands:
            print(f"\n{'=' * 60}")
            print(f"{category.upper().replace('_', ' ')}")
            print(f"{'=' * 60}\n")
            
            for cmd in commands[category]:
                print(f"Command:     {cmd['command']}")
                print(f"Description: {cmd['description']}")
                print(f"Platform:    {cmd['platform']}")
                print("-" * 60)
        else:
            print(f"✗ Category '{category}' not found")
            print(f"Available categories: {', '.join(commands.keys())}")
    else:
        for cat_name, cat_commands in commands.items():
            print(f"\n{'=' * 60}")
            print(f"{cat_name.upper().replace('_', ' ')}")
            print(f"{'=' * 60}\n")
            
            for cmd in cat_commands:
                print(f"Command:     {cmd['command']}")
                print(f"Description: {cmd['description']}")
                print(f"Platform:    {cmd['platform']}")
                print("-" * 60)
